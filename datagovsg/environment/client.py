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

"""Client for interacting with the Environment APIs."""

from cachetools import cached, TTLCache
from datetime import date, datetime

from datagovsg import net
from datagovsg.client import __Client
from datagovsg.environment.constants import *

class Client(__Client):
    """Interact with the environment-related endpoints."""

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def air_temperature(self, date_time=None, dt=None):
        """Get air temperature readings across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of air temperature by station.

        References:
            https://data.gov.sg/dataset/realtime-weather-readings?resource_id=17494bed-23e9-4b3b-ae89-232f87987163
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
       }
        kwargs = self.prepare_kwargs(kwargs)

        air_temperature = net.send_request(
            AIR_TEMPERATURE_API_ENDPOINT,
            **kwargs,
        )

        return air_temperature

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_HOUR))
    def pm25(self, date_time=None, dt=None):
        """Retrieve the latest PM2.5 information in Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of PM2.5 by region.

        References:
            https://data.gov.sg/dataset/pm2-5
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        pm25_information = net.send_request(
            PM25_API_ENDPOINT,
            **kwargs,
        )

        return pm25_information

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_HOUR))
    def psi(self, date_time=None, dt=None):
        """Retrieve the latest PSI information in Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of PSI by region.

        References:
            https://data.gov.sg/dataset/psi
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        psi_information = net.send_request(
            PSI_API_ENDPOINT,
            **kwargs,
        )

        return psi_information

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_FIVE_MINUTES))
    def rainfall(self, date_time=None, dt=None):
        """Get rainfall readings across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of rainfall by station.

        References:
            https://data.gov.sg/dataset/realtime-weather-readings?resource_id=8bd37e06-cdd7-4ca4-9ad8-5754eb70a33d
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        rainfall = net.send_request(
            RAINFALL_API_ENDPOINT,
            **kwargs,
        )

        return rainfall

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def relative_humidity(self, date_time=None, dt=None):
        """Get relative humidity readings across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of relative humidity by station.

        References:
            https://data.gov.sg/dataset/realtime-weather-readings?resource_id=59eb2883-2ceb-4d16-85f0-7e3a3176ef46
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        relative_humidity = net.send_request(
            RELATIVE_HUMIDITY_API_ENDPOINT,
            **kwargs,
        )

        return relative_humidity

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_HOUR))
    def uv_index(self, date_time=None):
        """Retrieve the latest UV index information in Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.

        Returns:
            (dict) Readings of UV Index by station.

        References:
            https://data.gov.sg/dataset/ultraviolet-index-uvi
        """
        uv_index_information = net.send_request(
            UV_INDEX_API_ENDPOINT,
            date_time=date_time,
        )

        return uv_index_information

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_THIRTY_MINUTES))
    def two_hour_weather_forecast(self, date_time=None, dt=None):
        """Retrieve the latest two hour weather forecast across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Weather forecast for the next 2 hours by area.

        References:
            https://data.gov.sg/dataset/weather-forecast?resource_id=571ef5fb-ed31-48b2-85c9-61677de42ca9
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        two_hour_weather_forecast = net.send_request(
            TWO_HOUR_WEATHER_FORECAST_API_ENDPOINT,
            **kwargs,
        )

        return two_hour_weather_forecast

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_HOUR))
    def twenty_four_hour_weather_forecast(self, date_time=None, dt=None):
        """Retrieve the latest 24 hour weather forecast across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Weather forecast for the next 24 hours by area.

        References:
            https://data.gov.sg/dataset/weather-forecast?resource_id=9a8bd97e-0e38-46b7-bc39-9a2cb4a53a62
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        twenty_four_hour_weather_forecast = net.send_request(
            TWENTY_FOUR_HOUR_WEATHER_FORECAST_API_ENDPOINT,
            **kwargs,
        )

        return twenty_four_hour_weather_forecast

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TWELVE_HOURS))
    def four_day_weather_forecast(self, date_time=None, dt=None):
        """Retrieve the latest 4 day weather forecast.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Weather forecast for the next 4 days by area.

        References:
            https://data.gov.sg/dataset/weather-forecast?resource_id=4df6d890-f23e-47f0-add1-fd6d580447d1
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        four_day_weather_forecast = net.send_request(
            FOUR_DAY_WEATHER_FORECAST_API_ENDPOINT,
            **kwargs,
        )

        return four_day_weather_forecast

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def wind_direction(self, date_time=None, dt=None):
        """Get wind direction readings across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of wind direction by station.

        References:
            https://data.gov.sg/dataset/realtime-weather-readings?resource_id=5dcf8aa5-cf6a-44e4-b359-1173eecfdf4c
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        wind_direction = net.send_request(
            WIND_DIRECTION_API_ENDPOINT,
            **kwargs,
        )

        return wind_direction

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def wind_speed(self, date_time=None, dt=None):
        """Get wind speed readings across Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the readings.
                Will be standardised to SGT timezone.
                If both `dt` and `date_time` are specified, then `date_time`
                is used.
            dt (date):
                (optional) Specific date to retrieve the readings.
                If both `dt` and `date_time` are specified, then `dt`
                is NOT used.

        Returns:
            (dict) Readings of wind speed by station.

        References:
            https://data.gov.sg/dataset/realtime-weather-readings?resource_id=16035f22-37b4-4a5c-b024-ca2381f11b48
        """
        kwargs = {
            'date_time': date_time,
            'date': dt,
        }
        kwargs = self.prepare_kwargs(kwargs)

        wind_speed = net.send_request(
            WIND_SPEED_API_ENDPOINT,
            **kwargs,
        )

        return wind_speed
