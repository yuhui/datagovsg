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

# pylint: disable=broad-exception-caught,invalid-name,missing-function-docstring,redefined-outer-name,unused-argument

"""Test that the Environment class is working properly."""

from datetime import date, datetime, time, timedelta
from time import sleep
from zoneinfo import ZoneInfo

import pytest

from datagovsg import Environment

METHODS_RETURNING_ENVIRONMENT_READINGS_PER_MINUTE = [
    'air_temperature',
    'rainfall',
    'relative_humidity',
    'wind_direction',
    'wind_speed',
]
METHODS_RETURNING_ENVIRONMENT_ITEMS_PER_HOUR = [
    'pm25',
    'psi',
]
METHODS_RETURNING_ENVIRONMENT_RECORDS_PER_HOUR = [
    'uv_index',
]
METHODS_RETURNING_ENVIRONMENT_READINGS = \
    METHODS_RETURNING_ENVIRONMENT_READINGS_PER_MINUTE \
    + METHODS_RETURNING_ENVIRONMENT_ITEMS_PER_HOUR \
    + METHODS_RETURNING_ENVIRONMENT_RECORDS_PER_HOUR
TEST_DATE = date.today() - timedelta(1)
TEST_DATETIME = datetime.combine(
    TEST_DATE,
    time(23, 45, 16, tzinfo=ZoneInfo('Asia/Singapore'))
)

@pytest.fixture(scope='module')
def client():
    return Environment()

@pytest.mark.parametrize(
    ('method'),
    METHODS_RETURNING_ENVIRONMENT_READINGS,
)
def test_environment_readings(client, method):
    try:
        data = getattr(client, method, None)()
    except Exception:
        # try again
        sleep(5)
        data = getattr(client, method, None)()

    assert data is not None

@pytest.mark.parametrize(
    ('method', 'data_items_name'),
    [
        (method, 'readings') \
            for method in METHODS_RETURNING_ENVIRONMENT_READINGS_PER_MINUTE
    ]
    + [
        (method, 'items') \
            for method in METHODS_RETURNING_ENVIRONMENT_ITEMS_PER_HOUR
    ]
    + [
        (method, 'records') \
            for method in METHODS_RETURNING_ENVIRONMENT_RECORDS_PER_HOUR
    ],
)
def test_environment_readings_with_date(client, method, data_items_name):
    try:
        data = getattr(client, method, None)(date=TEST_DATE)
    except Exception:
        # try again
        sleep(5)
        data = getattr(client, method, None)(date=TEST_DATE)

    assert all(
        data_item['timestamp'].date() == TEST_DATE \
            for data_item in data[data_items_name]
    )

@pytest.mark.parametrize(
    ('method', 'data_items_name'),
    [
        (method, 'readings') \
            for method in METHODS_RETURNING_ENVIRONMENT_READINGS_PER_MINUTE
    ]
    + [
        (method, 'items') \
            for method in METHODS_RETURNING_ENVIRONMENT_ITEMS_PER_HOUR
    ]
    + [
        (method, 'records') \
            for method in METHODS_RETURNING_ENVIRONMENT_RECORDS_PER_HOUR
    ],
)
def test_environment_readings_with_datetime(client, method, data_items_name):
    try:
        data = getattr(client, method, None)(date=TEST_DATETIME)
    except Exception:
        # try again
        sleep(5)
        data = getattr(client, method, None)(date=TEST_DATETIME)

    assert len(data[data_items_name]) == 1

    timestamp = data[data_items_name][0]['timestamp']
    assert timestamp <= TEST_DATETIME

def test_two_hour_weather_forecast(client):
    two_hour_weather_forecast = client.two_hour_weather_forecast()

    assert two_hour_weather_forecast is not None

def test_two_hour_weather_forecast_with_date(client):
    two_hour_weather_forecast = client.two_hour_weather_forecast(
        date=TEST_DATE,
    )

    assert all(
        item['timestamp'].date() <= TEST_DATE \
            for item in two_hour_weather_forecast['items']
    )

def test_two_hour_weather_forecast_with_datetime(client):
    two_hour_weather_forecast = client.two_hour_weather_forecast(
        date=TEST_DATETIME,
    )

    assert len(two_hour_weather_forecast['items']) == 1

    item = two_hour_weather_forecast['items'][0]

    assert item['timestamp'] <= TEST_DATETIME

def test_twenty_four_hour_weather_forecast(client):
    twenty_four_hour_weather_forecast = \
        client.twenty_four_hour_weather_forecast()

    assert twenty_four_hour_weather_forecast is not None

def test_twenty_four_hour_weather_forecast_with_date(client):
    twenty_four_hour_weather_forecast = \
        client.twenty_four_hour_weather_forecast(date=TEST_DATE)

    for record in twenty_four_hour_weather_forecast['records']:
        assert all(
            TEST_DATE <= period['timePeriod']['end'].date() \
                for period in record['periods']
        )

def test_twenty_four_hour_weather_forecast_with_datetime(client):
    twenty_four_hour_weather_forecast = \
        client.twenty_four_hour_weather_forecast(date=TEST_DATETIME)

    assert len(twenty_four_hour_weather_forecast['records']) == 1

    record = twenty_four_hour_weather_forecast['records'][0]

    assert all(
        TEST_DATETIME <= period['timePeriod']['end'] \
            for period in record['periods']
    )

def test_four_day_weather_forecast(client):
    four_day_weather_forecast = client.four_day_weather_forecast()

    assert four_day_weather_forecast is not None

def test_four_day_weather_forecast_with_date(client):
    four_day_weather_forecast = client.four_day_weather_forecast(
        date=TEST_DATE,
    )

    for record in four_day_weather_forecast['records']:
        assert all(
            forecast['timestamp'].date() >= TEST_DATE \
                for forecast in record['forecasts']
        )

def test_four_day_weather_forecast_with_datetime(client):
    four_day_weather_forecast = client.four_day_weather_forecast(
        date=TEST_DATETIME,
    )

    assert len(four_day_weather_forecast['records']) == 1

    record = four_day_weather_forecast['records'][0]

    assert all(
        forecast['timestamp'] >= TEST_DATETIME \
            for forecast in record['forecasts']
    )
