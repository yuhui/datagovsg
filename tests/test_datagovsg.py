# Copyright 2019-2025 Yuhui
#
# Licensed under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=invalid-name,missing-function-docstring,redefined-outer-name,unused-argument

"""Test that the net functions are working properly."""

from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
from requests import HTTPError
from typeguard import TypeCheckError

from datagovsg.datagovsg import DataGovSg

SANITISE_DATA_DICT = {
    'value_str': 'foo bar',
    'value_int': 42,
    'value_bool': True,
    'value_date': '1/7/2019',
    'value_list': [1, '2', {
        'date_time': '2024-12-01 09:57:45',
    }],
    'value_dict': {
        'key1': '316',
        'date_time': '2024-12-01T09:57:45.789',
    },
}

@pytest.fixture(scope='module')
def client():
    return DataGovSg()

def test_repr(client):
    assert repr(client) == str(client.__class__)

@pytest.mark.parametrize(
    ('original_params', 'default_params', 'expected_params'),
    [
        (
            {'foobar': 'foo bar'},
            {'meaning_of_universe': 42},
            {
                'foobar': 'foo bar',
                'meaning_of_universe': 42,
            },
        ),
        (
            {
                'foobar': 'foo bar',
                'date_time': datetime(2021, 3, 12, 9, 57, 45, 789)
            },
            None,
            {
                'foobar': 'foo bar',
                'date_time': '2021-03-12T09:57:45'
            },
        ),
    ],
)
def test_build_params(
    client,
    original_params,
    default_params,
    expected_params,
):
    params = client.build_params(original_params, default_params)
    assert params == expected_params

@pytest.mark.parametrize(
    ('kwargs', 'expected_result'),
    [
        (
            {},
            {
                'value_str': 'foo bar',
                'value_int': 42,
                'value_bool': True,
                'value_date': '1/7/2019',
                'value_list': [1, '2', {
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, tzinfo=ZoneInfo(key='Asia/Singapore')),
                }],
                'value_dict': {
                    'key1': '316',
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, 789000, tzinfo=ZoneInfo(key='Asia/Singapore')),
                },
            },
        ),
        (
            {'iterate': False},
            SANITISE_DATA_DICT,
        ),
        (
            {'sanitise_numbers': True},
            {
                'value_str': 'foo bar',
                'value_int': 42,
                'value_bool': True,
                'value_date': '1/7/2019',
                'value_list': [1, 2, {
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, tzinfo=ZoneInfo(key='Asia/Singapore')),
                }],
                'value_dict': {
                    'key1': 316,
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, 789000, tzinfo=ZoneInfo(key='Asia/Singapore')),
                },
            },
        ),
    ],
)
def test_sanitise_data(
    client,
    kwargs,
    expected_result,
):
    result = client.sanitise_data(value=SANITISE_DATA_DICT, **kwargs)
    assert result == expected_result

@pytest.mark.parametrize(
    ('url', 'params'),
    [
        (
            'https://api-open.data.gov.sg/v2/real-time/api/psi',
            {},
        ),
        (
            'https://api-open.data.gov.sg/v2/real-time/api/psi?date=2024-07-13T08:13:27',
            {},
        ),
        (
            'https://api-open.data.gov.sg/v2/real-time/api/psi',
            {'date': '2024-07-13'},
        ),
        (
            'https://api.data.gov.sg/v1/transport/taxi-availability',
            {},
        ),
        (
            'https://api.data.gov.sg/v1/transport/taxi-availability',
            {'date_time': '2024-07-13T08:32:17'},
        ),
        (
            'https://api.data.gov.sg/v1/transport/taxi-availability',
            'date_time=2024-07-13T08:32:17',
        ),
    ],
)
def test_send_request(client, url, params):
    data = client.send_request(url, params)
    assert isinstance(data, dict)

def test_send_request_with_invalid_endpoint(client):
    with pytest.raises(HTTPError):
        _ = client.send_request(
            'https://api-open.data.gov.sg/v2/real-time/api/foo',
        )
