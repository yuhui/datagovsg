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

from typing import Any, Unpack
from urllib.parse import urlencode

from typeguard import typechecked

from ..constants import (
    CACHE_ONE_MINUTE,
    CACHE_FIVE_MINUTES,
    CACHE_THIRTY_MINUTES,
    CACHE_ONE_HOUR,
    CACHE_TWELVE_HOURS,
)
from ..datagovsg import DataGovSg
from ..exceptions import APIError
from ..types import Url

from .constants import (
    AIR_TEMPERATURE_API_ENDPOINT,
    FOUR_DAY_WEATHER_FORECAST_API_ENDPOINT,
    PM25_API_ENDPOINT,
    PSI_API_ENDPOINT,
    RAINFALL_API_ENDPOINT,
    RELATIVE_HUMIDITY_API_ENDPOINT,
    TWENTY_FOUR_HOUR_WEATHER_FORECAST_API_ENDPOINT,
    TWO_HOUR_WEATHER_FORECAST_API_ENDPOINT,
    UV_INDEX_API_ENDPOINT,
    WIND_DIRECTION_API_ENDPOINT,
    WIND_SPEED_API_ENDPOINT,
)
from .types_args import EnvironmentArgsDict
from .types import (
    EnvironmentReadingDict,
    PM25Dict,
    PSIDict,
    UVIndexDict,
    WeatherForecastTwoHourDict,
    WeatherForecastTwentyFourHourDict,
    WeatherForecastFourDayDict,
)

class Client(DataGovSg):
    """Interact with the environment-related endpoints."""

    @typechecked
    def air_temperature(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> EnvironmentReadingDict:
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
        air_temperature: EnvironmentReadingDict

        params = self.build_params(kwargs)

        air_temperature = self.__collect_environment_data(
            AIR_TEMPERATURE_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return air_temperature

    @typechecked
    def pm25(self, **kwargs: Unpack[EnvironmentArgsDict]) -> PM25Dict:
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
        pm25: PM25Dict

        params = self.build_params(kwargs)

        pm25 = self.__collect_environment_data(
            PM25_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_HOUR,
        )

        return pm25

    @typechecked
    def psi(self, **kwargs: Unpack[EnvironmentArgsDict]) -> PSIDict:
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
        psi: PSIDict

        params = self.build_params(kwargs)

        psi = self.__collect_environment_data(
            PSI_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_HOUR,
        )

        return psi

    @typechecked
    def rainfall(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> EnvironmentReadingDict:
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
        rainfall: EnvironmentReadingDict

        params = self.build_params(kwargs)

        rainfall = self.__collect_environment_data(
            RAINFALL_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_FIVE_MINUTES,
        )

        return rainfall

    @typechecked
    def relative_humidity(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> EnvironmentReadingDict:
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
        relative_humidity: EnvironmentReadingDict

        params = self.build_params(kwargs)

        relative_humidity = self.__collect_environment_data(
            RELATIVE_HUMIDITY_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return relative_humidity

    @typechecked
    def uv_index(self, **kwargs: Unpack[EnvironmentArgsDict]) -> UVIndexDict:
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
        uv_index: UVIndexDict

        params = self.build_params(kwargs)

        uv_index = self.__collect_environment_data(
            UV_INDEX_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_HOUR,
        )

        return uv_index

    @typechecked
    def two_hour_weather_forecast(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> WeatherForecastTwoHourDict:
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
        two_hour_weather_forecast: WeatherForecastTwoHourDict

        params = self.build_params(kwargs)

        two_hour_weather_forecast = self.__collect_environment_data(
            TWO_HOUR_WEATHER_FORECAST_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_THIRTY_MINUTES,
        )

        return two_hour_weather_forecast

    @typechecked
    def twenty_four_hour_weather_forecast(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> WeatherForecastTwentyFourHourDict:
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
        twenty_four_hour_weather_forecast: WeatherForecastTwentyFourHourDict

        params = self.build_params(kwargs)

        twenty_four_hour_weather_forecast = self.__collect_environment_data(
            TWENTY_FOUR_HOUR_WEATHER_FORECAST_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_HOUR,
        )

        return twenty_four_hour_weather_forecast

    @typechecked
    def four_day_weather_forecast(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> WeatherForecastFourDayDict:
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
        four_day_weather_forecast: WeatherForecastFourDayDict

        params = self.build_params(kwargs)

        four_day_weather_forecast = self.__collect_environment_data(
            FOUR_DAY_WEATHER_FORECAST_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return four_day_weather_forecast

    @typechecked
    def wind_direction(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> EnvironmentReadingDict:
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
        wind_direction: EnvironmentReadingDict

        params = self.build_params(kwargs)

        wind_direction = self.__collect_environment_data(
            WIND_DIRECTION_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return wind_direction

    @typechecked
    def wind_speed(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> EnvironmentReadingDict:
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
        wind_speed: EnvironmentReadingDict

        params = self.build_params(kwargs)

        wind_speed = self.__collect_environment_data(
            WIND_SPEED_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return wind_speed

    # private

    def __collect_environment_data(
        self,
        url: Url,
        params: dict,
        cache_duration: int,
    ) -> Any:
        """Get environment data from the specified endpoint URL.

        If there are pages of 'readings' data, then compiles all of those \
            pages into one big list.

        (Since this method has to call `send_request()`, so the parameters \
            are similar to that method's.)

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires.
        :type cache_duration: int

        :return: data from the endpoint, compiling all pages of readings.
        :rtype: Any (but really a dict)
        """
        params_str = urlencode(params, safe=':+')
        response = self.send_request(
            url,
            params=params_str,
            cache_duration=cache_duration,
        )

        if 'data' not in response:
            error_message = 'Unexpected error occurred'
            if 'errorMsg' in response:
                error_message = response['errorMsg']
            raise APIError(error_message, response)

        data = response['data']

        if 'paginationToken' in data:
            pagination_token = data.pop('paginationToken')

            # Collect the next page of data and append it to this one
            params['paginationToken'] = pagination_token
            response_data = self.__collect_environment_data(
                url,
                params=params,
                cache_duration=cache_duration,
            )

            data_items_name = ''
            if 'items' in data and 'items' in response_data:
                data_items_name = 'items'
            elif 'readings' in data and 'readings' in response_data:
                data_items_name = 'readings'
            elif 'records' in data and 'records' in response_data:
                data_items_name = 'records'
            if data_items_name != '':
                data[data_items_name].extend(response_data[data_items_name])

            # Merge and keep unique values
            data_centre_name = ''
            data_centre_field = ''
            if 'area_metadata' in data and 'area_metadata' in response_data:
                data_centre_name = 'area_metadata'
                data_centre_field = 'name'
            elif 'regionMetadata' in data and 'regionMetadata' in response_data:
                data_centre_name = 'regionMetadata'
                data_centre_field = 'name'
            elif 'stations' in data and 'stations' in response_data:
                data_centre_name = 'stations'
                data_centre_field = 'id'
            if data_centre_name != '' and data_centre_field != '':
                centres = [
                    centre[data_centre_field] \
                        for centre in data[data_centre_name]
                ]
                for centre in response_data[data_centre_name]:
                    if centre[data_centre_field] not in centres:
                        data[data_centre_name].append(centre)

        return data

__all__ = [
    'Client',
]
