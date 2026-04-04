# Copyright 2019-2026 Yuhui
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

"""Test that the DataGovSg class is working properly."""

from datetime import date, datetime
from os import getenv
from zoneinfo import ZoneInfo

import pytest
from dotenv import load_dotenv
from requests import HTTPError
from requests_cache import CachedSession

from datagovsg.datagovsg import DataGovSg
from datagovsg.constants import USER_AGENT
from datagovsg.exceptions import APIError

from .mocks.types_args import MockArgsDict
from .mocks.api_response_datagovsg import (
    APIResponseDefault,
    APIResponseBadRequest,
    APIResponseNotFound,
    APIResponseRateLimitExceeded,
    APIResponseTrafficImages,
)

MOCKED_ERROR_RESPONSE_METHODS_AND_ERROR_VALUES = [
    (APIResponseDefault, '...'),
    (
        APIResponseBadRequest,
        'Invalid date format. Date format must be YYYY-MM-DD (2024-06-01) or YYYY-MM-DDTHH:mm:ss (2024-06-01T08:30:00).',
    ),
    (APIResponseNotFound, 'Data not found'),
    (APIResponseRateLimitExceeded, 'Rate limit exceeded'),
]

SANITISE_DATA_DICT = {
    'value_str': 'foo bar',
    'value_ignore': '37',
    'value_int': 42,
    'value_bool': True,
    'value_date': '1/7/2019',
    'value_blank': '',
    'value_list': [1, '2', {
        'key1': '205',
        'date_time': '2024-12-01T09:57:45+08:00',
    }],
    'value_dict': {
        'key1': '316',
        'date_time': '2024-12-01 09:57:45.789',
    },
}

# constants for testing date as date object
GOOD_DATE = date(2019, 7, 13)
GOOD_DATE_STR = '2019-07-13'
GOOD_DATETIME = datetime(2019, 7, 13, 4, 56, 8)
GOOD_DATETIME_STR = '2019-07-13T04:56:08'

@pytest.fixture(scope='module')
def client():
    # There is no need to test for a valid API key, because all endpoints will
    # always run regardless of what key has been supplied.
    load_dotenv()
    api_key = getenv('DATAGOVSG_API_KEY')
    return DataGovSg(api_key)

def test_repr(client):
    assert repr(client).startswith(str(client.__class__))
    assert USER_AGENT in repr(client)

@pytest.mark.parametrize(
    ('original_params', 'default_params', 'key_map', 'expected_params'),
    [
        (
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE,
                'datetime': GOOD_DATETIME,
            },
            {
                'foobar': 'foo and bar',
                'meaning_of_universe': 42,
            },
            {
                'datetime': 'DATE_TIME',
                'meaning_of_universe': 'meaningOfUniverse',
            },
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE_STR,
                'DATE_TIME': GOOD_DATETIME_STR,
                'meaningOfUniverse': 42,
            },
        ),
        (
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE,
                'datetime': GOOD_DATETIME,
            },
            None,
            None,
            {
                'foobar': 'foo bar',
                'date': GOOD_DATE_STR,
                'datetime': GOOD_DATETIME_STR,
            },
        ),
    ],
)
def test_build_params(
    client,
    original_params,
    default_params,
    key_map,
    expected_params,
):
    params = client.build_params(MockArgsDict, original_params, default_params, key_map)
    assert params == expected_params

@pytest.mark.parametrize(
    ('kwargs', 'expected_result'),
    [
        (
            {},
            {
                'value_str': 'foo bar',
                'value_ignore': 37,
                'value_int': 42,
                'value_bool': True,
                'value_date': '1/7/2019',
                'value_blank': None,
                'value_list': [1, 2, {
                    'key1': 205,
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, tzinfo=ZoneInfo(key='Asia/Singapore')),
                }],
                'value_dict': {
                    'key1': 316,
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, 789000, tzinfo=ZoneInfo(key='Asia/Singapore')),
                },
            },
        ),
        (
            {'iterate': False},
            SANITISE_DATA_DICT,
        ),
        (
            {
                'ignore_keys': [
                    'value_ignore',
                    'value_dict.date_time',
                    'value_list[].key1',
                ]
            },
            {
                'value_str': 'foo bar',
                'value_ignore': '37',
                'value_int': 42,
                'value_bool': True,
                'value_date': '1/7/2019',
                'value_blank': None,
                'value_list': [1, 2, {
                    'key1': '205',
                    'date_time': datetime(2024, 12, 1, 9, 57, 45, tzinfo=ZoneInfo(key='Asia/Singapore')),
                }],
                'value_dict': {
                    'key1': 316,
                    'date_time': '2024-12-01 09:57:45.789',
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
    ],
)
def test_send_request(client, url, params):
    data = client.send_request(url, params)
    assert isinstance(data, dict)

def test_send_request_with_sanitise_ignored_keys(
    client,
    monkeypatch,
):
    def mock_requests_get(*args, **kwargs):
        return APIResponseTrafficImages()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    response_content = client.send_request(
        'https://api.data.gov.sg/v1/transport/traffic-images',
        sanitise_ignore_keys=[
            'items[].cameras[].camera_id',
        ],
    )

    camera_id = response_content['items'][0]['cameras'][0].get('camera_id', None)
    assert isinstance(camera_id, str)

def test_send_request_with_invalid_endpoint(client):
    with pytest.raises(HTTPError):
        _ = client.send_request(
            'https://api-open.data.gov.sg/v2/real-time/api/foo',
        )

@pytest.mark.parametrize(
    ('mocked_response_method', 'error_value'),
    MOCKED_ERROR_RESPONSE_METHODS_AND_ERROR_VALUES,
)
def test_send_request_with_error_response(
    client,
    mocked_response_method,
    error_value,
    monkeypatch,
):
    def mock_requests_get(*args, **kwargs):
        return mocked_response_method()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    def send_error_request():
        _ = client.send_request(
            'https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast?date=2026-01-10',
        )

    with pytest.raises(APIError) as excinfo:
        send_error_request()

    assert error_value in str(excinfo.value)
