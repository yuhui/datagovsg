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

# pylint: disable=broad-exception-caught,invalid-name,missing-function-docstring,redefined-outer-name,unused-argument

"""Test that the Environment class is working properly."""

from datetime import date, datetime, time, timedelta
from time import sleep
from os import getenv
from unittest.mock import Mock
from zoneinfo import ZoneInfo

import pytest
from dotenv import load_dotenv
from requests_cache import CachedSession
from typeguard import check_type

from datagovsg import Environment
from datagovsg.environment.types import (
    EnvironmentReadingDict,
    PM25Dict,
    PSIDict,
    UVIndexDict,
    WeatherDict,
    WeatherForecastTwoHourDict,
    WeatherForecastTwentyFourHourDict,
    WeatherForecastFourDayDict,
)

from .mocks.api_response_environment import (
    APIResponseAirTemperature,
    APIResponseAirTemperaturePage1,
    APIResponseAirTemperaturePage2,
    APIResponseAirTemperaturePage3,
    APIResponseFloodAlerts,
    APIResponseLightning,
    APIResponsePM25,
    APIResponsePM25Page1,
    APIResponsePM25Page2,
    APIResponsePM25Page3,
    APIResponsePSI,
    APIResponseRainfall,
    APIResponseRelativeHumidity,
    APIResponseUVIndex,
    APIResponseUVIndexPage1,
    APIResponseUVIndexPage2,
    APIResponseUVIndexPage3,
    APIResponseWBGT,
    APIResponseTwoHourWeatherForecast,
    APIResponseTwoHourWeatherForecastPage1,
    APIResponseTwoHourWeatherForecastPage2,
    APIResponseTwentyFourHourWeatherForecast,
    APIResponseFourDayWeatherForecast,
    APIResponseWindDirection,
    APIResponseWindSpeed,
)

TEST_DATE = date(2026, 1, 12)
TEST_DATETIME = datetime.combine(
    TEST_DATE,
    time(10, 15, 0, tzinfo=ZoneInfo('Asia/Singapore'))
)
TEST_DATE_YESTERDAY = TEST_DATE - timedelta(days=1)
TEST_DATE_STRING = TEST_DATE.strftime('%Y-%m-%d')
TEST_DATETIME_STRING = TEST_DATETIME.strftime('%Y-%m-%dT%H:%M:%S')

TEST_DATA = [
    (
        'air_temperature',
        EnvironmentReadingDict,
        APIResponseAirTemperature,
    ),
    (
        'flood_alerts',
        WeatherDict,
        APIResponseFloodAlerts,
    ),
    (
        'lightning',
        WeatherDict,
        APIResponseLightning,
    ),
    (
        'pm25',
        PM25Dict,
        APIResponsePM25,
    ),
    (
        'psi',
        PSIDict,
        APIResponsePSI,
    ),
    (
        'rainfall',
        EnvironmentReadingDict,
        APIResponseRainfall,
    ),
    (
        'relative_humidity',
        EnvironmentReadingDict,
        APIResponseRelativeHumidity,
    ),
    (
        'uv_index',
        UVIndexDict,
        APIResponseUVIndex,
    ),
    (
        'wbgt',
        WeatherDict,
        APIResponseWBGT,
    ),
    (
        'two_hour_weather_forecast',
        WeatherForecastTwoHourDict,
        APIResponseTwoHourWeatherForecast,
    ),
    (
        'twenty_four_hour_weather_forecast',
        WeatherForecastTwentyFourHourDict,
        APIResponseTwentyFourHourWeatherForecast,
    ),
    (
        'four_day_weather_forecast',
        WeatherForecastFourDayDict,
        APIResponseFourDayWeatherForecast,
    ),
    (
        'wind_direction',
        EnvironmentReadingDict,
        APIResponseWindDirection,
    ),
    (
        'wind_speed',
        EnvironmentReadingDict,
        APIResponseWindSpeed,
    ),
]
TEST_METHODS_AND_EXPECTED_TYPES = [
    (method, expected_type) for method, expected_type, _ in TEST_DATA
]
TEST_METHODS_AND_MOCKS = [
    (method, mocked_response) for method, _, mocked_response in TEST_DATA
]

@pytest.fixture(scope='module')
def client():
    load_dotenv()
    api_key = getenv('DATAGOVSG_API_KEY')
    return Environment(api_key)

@pytest.mark.parametrize(
    ('method', 'expected_type'),
    TEST_METHODS_AND_EXPECTED_TYPES,
)
def test_environment_methods(client, method, expected_type):
    try:
        data = getattr(client, method, None)()
    except Exception:
        # try again
        sleep(5)
        data = getattr(client, method, None)()

    assert check_type(data, expected_type) == data

@pytest.mark.parametrize(
    ('method', 'mocked_response'),
    TEST_METHODS_AND_MOCKS,
)
def test_environment_methods_with_date(
    client,
    method,
    mocked_response,
    monkeypatch,
):
    def mock_requests_get(*args, **kwargs):
        return mocked_response()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    original_send_request = client.send_request
    client.send_request = Mock(side_effect=original_send_request)

    _ = getattr(client, method, None)(date=TEST_DATE)

    client.send_request.assert_called_once()
    _, kwargs = client.send_request.call_args
    assert kwargs['params']['date'] == TEST_DATE_STRING

@pytest.mark.parametrize(
    ('method', 'mocked_response'),
    TEST_METHODS_AND_MOCKS,
)
def test_environment_methods_with_datetime(
    client,
    method,
    mocked_response,
    monkeypatch,
):
    def mock_requests_get(*args, **kwargs):
        return mocked_response()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    original_send_request = client.send_request
    client.send_request = Mock(side_effect=original_send_request)

    _ = getattr(client, method, None)(date=TEST_DATETIME)

    client.send_request.assert_called_once()
    _, kwargs = client.send_request.call_args
    assert kwargs['params']['date'] == TEST_DATETIME_STRING

def test_air_temperature_with_pagination(client, monkeypatch):
    def mock_requests_get(*args, **kwargs):
        params = kwargs.get('params', {})
        pagination_token = params.get('paginationToken', None)
        if pagination_token is None:
            return APIResponseAirTemperaturePage1()
        elif pagination_token == 'b2Zmc2V0PTI1':
            return APIResponseAirTemperaturePage2()
        elif pagination_token == 'b2Zmc2V0PTUw':
            return APIResponseAirTemperaturePage3()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    data = client.air_temperature()

    assert len(data['stations']) == 8
    assert len(data['readings']) == 9

def test_pm25_with_pagination(client, monkeypatch):
    def mock_requests_get(*args, **kwargs):
        params = kwargs.get('params', {})
        pagination_token = params.get('paginationToken', None)
        if pagination_token is None:
            return APIResponsePM25Page1()
        elif pagination_token == 'b2Zmc2V0PTI1':
            return APIResponsePM25Page2()
        elif pagination_token == 'b2Zmc2V0PTUw':
            return APIResponsePM25Page3()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    data = client.pm25()

    assert len(data['regionMetadata']) == 5
    assert len(data['items']) == 6

def test_two_hour_weather_forecast_with_pagination(client, monkeypatch):
    def mock_requests_get(*args, **kwargs):
        params = kwargs.get('params', {})
        pagination_token = params.get('paginationToken', None)
        if pagination_token is None:
            return APIResponseTwoHourWeatherForecastPage1()
        elif pagination_token == 'b2Zmc2V0PTI1':
            return APIResponseTwoHourWeatherForecastPage2()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    data = client.two_hour_weather_forecast()

    assert len(data['area_metadata']) == 4
    assert len(data['items']) == 8

def test_uv_index_with_pagination(client, monkeypatch):
    def mock_requests_get(*args, **kwargs):
        params = kwargs.get('params', {})
        pagination_token = params.get('paginationToken', None)
        if pagination_token is None:
            return APIResponseUVIndexPage1()
        elif pagination_token == 'b2Zmc2V0PTI1':
            return APIResponseUVIndexPage2()
        elif pagination_token == 'b2Zmc2V0PTUw':
            return APIResponseUVIndexPage3()

    monkeypatch.setattr(CachedSession, 'get', mock_requests_get)

    data = client.uv_index()

    assert len(data['records']) == 13
