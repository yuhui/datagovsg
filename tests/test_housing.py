# Copyright 2025-2026 Yuhui
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

"""Test that the Housing class is working properly."""

from datetime import datetime
from os import getenv
from unittest.mock import Mock
from zoneinfo import ZoneInfo

import pytest
from dotenv import load_dotenv
from requests_cache import CachedSession
from typeguard import check_type

from datagovsg import Housing
from datagovsg.housing.types import CarparkAvailabilityItemDict

from .mocks.api_response_housing import APIResponseCarparkAvailability

TEST_DATETIME = datetime(
    2026, 1, 12, 0, 15, 0,
    tzinfo=ZoneInfo('Asia/Singapore'),
)
TEST_DATETIME_STRING = TEST_DATETIME.strftime('%Y-%m-%dT%H:%M:%S')

TEST_PARAMETERS_AND_MOCKS = [
    (
        'carpark_availability',
        list[CarparkAvailabilityItemDict],
        APIResponseCarparkAvailability,
    )
]

@pytest.fixture(scope='module')
def client():
    load_dotenv()
    api_key = getenv('DATAGOVSG_API_KEY')
    return Housing(api_key)

@pytest.mark.parametrize(
    (
        'method',
        'expected_type',
        'mocked_response_method',
    ),
    TEST_PARAMETERS_AND_MOCKS,
)
def test_housing_methods(
    client,
    method,
    expected_type,
    mocked_response_method,
):
    data = getattr(client, method, None)()

    assert check_type(data, expected_type) == data

@pytest.mark.parametrize(
    (
        'method',
        'expected_type',
        'mocked_response_method',
    ),
    TEST_PARAMETERS_AND_MOCKS,
)
def test_housing_methods_with_datetime(
    client,
    method,
    expected_type,
    mocked_response_method,
    monkeypatch,
):
    def mock_requests_get(*args, **kwargs):
        return mocked_response_method()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    original_send_request = client.send_request
    client.send_request = Mock(side_effect=original_send_request)

    _ = getattr(client, method, None)(date_time=TEST_DATETIME)

    client.send_request.assert_called_once()
    _, kwargs = client.send_request.call_args
    assert kwargs['params']['date_time'] == TEST_DATETIME_STRING
