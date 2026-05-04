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

"""Test that the Economy class is working properly."""

from datetime import date
from os import getenv
from unittest.mock import Mock

import pytest
from dotenv import load_dotenv
from requests_cache import CachedSession
from typeguard import check_type

from datagovsg import Economy
from datagovsg.economy.constants import INVALID_DATE_ERROR_MESSAGE
from datagovsg.economy.types import EconomyDict

from .mocks.api_response_economy import (
    APIResponseDesigns,
    APIResponsePatents,
    APIResponseTrademarks,
)

BAD_DATE = date(2000, 1, 1)
GOOD_DATE = date(2020, 1, 12)
GOOD_DATE_STRING = GOOD_DATE.strftime('%Y-%m-%d')

TEST_DATA = [
    ('designs', EconomyDict, APIResponseDesigns),
    ('patents', EconomyDict, APIResponsePatents),
    ('trademarks', EconomyDict, APIResponseTrademarks),
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
    return Economy(api_key)

@pytest.mark.parametrize(
    ('method', 'expected_type'),
    TEST_METHODS_AND_EXPECTED_TYPES,
)
def test_economy_methods(client, method, expected_type):
    data = getattr(client, method, None)(lodgement_date=GOOD_DATE)

    assert check_type(data, expected_type) == data

@pytest.mark.parametrize(
    ('method', 'mock_response_method'),
    TEST_METHODS_AND_MOCK_RESPONSE_METHODS,
)
def test_economy_methods_with_good_date(
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
        _ = getattr(client, method, None)(lodgement_date=GOOD_DATE)
    except ValueError as excinfo:
        pytest.fail(f'Unexpected ValueError raised: {excinfo}')

    client.send_request.assert_called_once()
    _, kwargs = client.send_request.call_args
    assert kwargs['params']['lodgement_date'] == GOOD_DATE_STRING

@pytest.mark.parametrize('method', TEST_METHODS)
def test_economy_methods_with_bad_date(client, method):
    with pytest.raises(ValueError) as excinfo:
        _ = getattr(client, method, None)(lodgement_date=BAD_DATE)

    assert str(excinfo.value) == INVALID_DATE_ERROR_MESSAGE
