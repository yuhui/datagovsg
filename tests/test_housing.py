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
from datagovsg.housing.constants import INVALID_DATETIME_ERROR_MESSAGE
from datagovsg.housing.types import CarparkAvailabilityItemDict

from .mocks.api_response_housing import APIResponseCarparkAvailability

BAD_DATETIME = datetime(
    2000, 1, 1, 0, 0, 0,
    tzinfo=ZoneInfo('Asia/Singapore'),
)
GOOD_DATETIME = datetime.now(ZoneInfo('Asia/Singapore'))
GOOD_DATETIME_STRING = GOOD_DATETIME.strftime('%Y-%m-%dT%H:%M:%S')

TEST_DATA = [
    (
        'carpark_availability',
        list[CarparkAvailabilityItemDict],
        APIResponseCarparkAvailability,
    ),
]
TEST_METHODS = [method for method, _, _ in TEST_DATA]
TEST_METHODS_AND_EXPECTED_TYPES = [
    (method, expected_type) for method, expected_type, _ in TEST_DATA
]
TEST_METHODS_AND_MOCK_RESPONSE_METHODS = [
    (method, mock_response_method) \
        for method, _, mock_response_method in TEST_DATA
]

@pytest.fixture(scope='module')
def client():
    load_dotenv()
    api_key = getenv('DATAGOVSG_API_KEY')
    return Housing(api_key)

@pytest.mark.parametrize(
    ('method', 'expected_type'),
    TEST_METHODS_AND_EXPECTED_TYPES,
)
def test_housing_methods(client, method, expected_type):
    data = getattr(client, method, None)()

    assert check_type(data, expected_type) == data

@pytest.mark.parametrize(
    ('method', 'mock_response_method'),
    TEST_METHODS_AND_MOCK_RESPONSE_METHODS,
)
def test_housing_methods_with_good_datetime(
    client,
    method,
    mock_response_method,
    monkeypatch,
):
    def mock_requests_get(*args, **kwargs):
        return mock_response_method()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    original_send_request = client.send_request
    client.send_request = Mock(side_effect=original_send_request)

    try:
        _ = getattr(client, method, None)(date_time=GOOD_DATETIME)
    except ValueError as excinfo:
        pytest.fail(f'Unexpected ValueError raised: {excinfo}')

    client.send_request.assert_called_once()
    _, kwargs = client.send_request.call_args
    assert kwargs['params']['date_time'] == GOOD_DATETIME_STRING

@pytest.mark.parametrize(
    ('method'),
    TEST_METHODS,
)
def test_economy_methods_with_bad_datetime(client, method):
    with pytest.raises(ValueError) as excinfo:
        _ = getattr(client, method, None)(date_time=BAD_DATETIME)

    assert str(excinfo.value) == INVALID_DATETIME_ERROR_MESSAGE
