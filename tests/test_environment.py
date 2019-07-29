# Copyright 2019 Yuhui
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

"""Test that the Environment class is working properly."""

import pytest
from requests.exceptions import HTTPError

from datagovsg import Environment

@pytest.fixture(scope='module')
def client():
    return Environment()

def test_air_temperature(client):
    air_temperature = client.air_temperature()

    assert isinstance(air_temperature, dict)

def test_pm25(client):
    pm25 = client.pm25()

    assert isinstance(pm25, dict)

def test_psi(client):
    psi = client.psi()

    assert isinstance(psi, dict)

def test_rainfall(client):
    rainfall = client.rainfall()

    assert isinstance(rainfall, dict)

def test_relative_humidity(client):
    relative_humidity = client.relative_humidity()

    assert isinstance(relative_humidity, dict)

def test_uv_index(client):
    uv_index = client.uv_index()

    assert isinstance(uv_index, dict)

def test_two_hour_weather_forecast(client):
    two_hour_weather_forecast = client.two_hour_weather_forecast()

    assert isinstance(two_hour_weather_forecast, dict)

def test_twenty_four_hour_weather_forecast(client):
    twenty_four_hour_weather_forecast = \
        client.twenty_four_hour_weather_forecast()

    assert isinstance(twenty_four_hour_weather_forecast, dict)

def test_four_day_weather_forecast(client):
    four_day_weather_forecast = client.four_day_weather_forecast()

    assert isinstance(four_day_weather_forecast, dict)

def test_wind_direction(client):
    wind_direction = client.wind_direction()

    assert isinstance(wind_direction, dict)

def test_wind_speed(client):
    wind_speed = client.wind_speed()

    assert isinstance(wind_speed, dict)
