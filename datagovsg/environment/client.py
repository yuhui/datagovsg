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

"""Client for interacting with the Environment APIs."""

from time import sleep
from typing import Any, Unpack

from typeguard import typechecked

from ..constants import (
    CACHE_ONE_MINUTE,
    CACHE_FIVE_MINUTES,
    CACHE_THIRTY_MINUTES,
    CACHE_ONE_HOUR,
    CACHE_TWELVE_HOURS,
)
from ..datagovsg import DataGovSg
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

    WEATHER_API_ENDPOINT,
    FLOOD_ALERTS_API_ENDPOINT,

    LIGHTNING_DEFAULT_PARAMS,
    WBGT_DEFAULT_PARAMS,

    WIND_SPEED_SANITISE_IGNORE_KEYS,
)
from .types_args import EnvironmentArgsDict, WeatherArgsDict
from .types import (
    EnvironmentReadingDict,
    PM25Dict,
    PSIDict,
    UVIndexDict,
    WeatherDict,
    WeatherForecastTwoHourDict,
    WeatherForecastTwentyFourHourDict,
    WeatherForecastFourDayDict,
)

class Client(DataGovSg):
    """Interact with the environment-related endpoints.

    Reference: \
        https://data.gov.sg/datasets?formats=API&topics=environment
    """

    @typechecked
    def air_temperature(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> EnvironmentReadingDict:
        """Get air temperature readings across Singapore.

        Has per-minute readings from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: Air Temperature Information. (Cached for 1 minute.)
        :rtype: EnvironmentReadingDict
        """
        air_temperature: EnvironmentReadingDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

        air_temperature = self.__collect_environment_data(
            AIR_TEMPERATURE_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return air_temperature

    @typechecked
    def flood_alerts(
        self,
        **kwargs: Unpack[EnvironmentArgsDict]
    ) -> WeatherDict:
        """Get flood alert information across Singapore.

        Update frequency is not specified, so defaults to half hourly.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: Flood alert Information. (Cached for 30 minutse.)
        :rtype: WeatherDict
        """
        flood_alerts: WeatherDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

        flood_alerts = self.__collect_environment_data(
            FLOOD_ALERTS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_THIRTY_MINUTES,
        )

        return flood_alerts

    @typechecked
    def lightning(self, **kwargs: Unpack[WeatherArgsDict]) -> WeatherDict:
        """Retrieve the latest lightning observation.

        Update frequency is not specified, so defaults to half hourly.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: WeatherArgsDict

        :return: Lightning Information. (Cached for 30 minutse.)
        :rtype: WeatherDict
        """
        lightning: WeatherDict

        params = self.build_params(
            params_expected_type=WeatherArgsDict,
            original_params=kwargs,
            default_params=LIGHTNING_DEFAULT_PARAMS,
        )

        lightning = self.__collect_environment_data(
            WEATHER_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_THIRTY_MINUTES,
        )

        return lightning

    @typechecked
    def pm25(self, **kwargs: Unpack[EnvironmentArgsDict]) -> PM25Dict:
        """Retrieve the latest PM2.5 information in Singapore.

        Updated hourly from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: PM 2.5 Information. (Cached for 1 hour.)
        :rtype: PM25Dict
        """
        pm25: PM25Dict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

        pm25 = self.__collect_environment_data(
            PM25_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_HOUR,
        )

        return pm25

    @typechecked
    def psi(self, **kwargs: Unpack[EnvironmentArgsDict]) -> PSIDict:
        """Retrieve the latest PSI information in Singapore.

        Updated hourly from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: PSI Information. (Cached for 1 hour.)
        :rtype: PSIDict
        """
        psi: PSIDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

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

        5-minute readings from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: Rainfall Information. (Cached for 5 minutes.)
        :rtype: EnvironmentReadingDict
        """
        rainfall: EnvironmentReadingDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

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
        """Get relative humidity readings.

        Has per-minute readings from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: Relative Humidity Information. (Cached for 1 minute.)
        :rtype: EnvironmentReadingDict
        """
        relative_humidity: EnvironmentReadingDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

        relative_humidity = self.__collect_environment_data(
            RELATIVE_HUMIDITY_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return relative_humidity

    @typechecked
    def uv_index(self, **kwargs: Unpack[EnvironmentArgsDict]) -> UVIndexDict:
        """Retrieve the latest UV index information in Singapore.

        Updated every hour between 7 AM and 7 PM everyday. The UV index value \
            is averaged over the preceding hour.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: UV Index Information. (Cached for 1 hour.)
        :rtype: UVIndexDict
        """
        uv_index: UVIndexDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

        uv_index = self.__collect_environment_data(
            UV_INDEX_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_HOUR,
        )

        return uv_index

    @typechecked
    def wbgt(self, **kwargs: Unpack[WeatherArgsDict]) -> WeatherDict:
        """Retrieve the latest WBGT data for accurate heat stress assessment.

        Update frequency is not specified, so defaults to half hourly.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: WeatherArgsDict

        :return: Wet Bulb Globe Temperature Information. (Cached for 30 \
            minutse.)
        :rtype: WeatherDict
        """
        wbgt: WeatherDict

        params = self.build_params(
            params_expected_type=WeatherArgsDict,
            original_params=kwargs,
            default_params=WBGT_DEFAULT_PARAMS,
        )

        wbgt = self.__collect_environment_data(
            WEATHER_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_THIRTY_MINUTES,
        )

        return wbgt

    @typechecked
    def two_hour_weather_forecast(
        self,
        **kwargs: Unpack[EnvironmentArgsDict],
    ) -> WeatherForecastTwoHourDict:
        """Retrieve the latest two hour weather forecast.

        Updated half-hourly from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: 2 Hour Weather Forecast. (Cached for 30 minutes.)
        :rtype: WeatherForecastTwoHourDict
        """
        two_hour_weather_forecast: WeatherForecastTwoHourDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

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
        """Retrieve the latest 24 hour weather forecast.

        Updated multiple times throughout the day.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: 24 Hour Weather Forecast. (Cached for 1 hour.)
        :rtype: WeatherForecastTwentyFourHourDict
        """
        twenty_four_hour_weather_forecast: WeatherForecastTwentyFourHourDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

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

        Updated twice a day from NEA. The forecast is for the next 4 days.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: 4 Day Weather Forecast. (Cached for 12 hours.)
        :rtype: WeatherForecastFourDayDict
        """
        four_day_weather_forecast: WeatherForecastFourDayDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

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

        Has per-minute readings from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: Wind Direction Information. (Cached for 1 minute.)
        :rtype: EnvironmentReadingDict
        """
        wind_direction: EnvironmentReadingDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

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

        Has per-minute readings from NEA.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EnvironmentArgsDict

        :return: Wind Speed Information. (Cached for 1 minute.)
        :rtype: EnvironmentReadingDict
        """
        wind_speed: EnvironmentReadingDict

        params = self.build_params(
            params_expected_type=EnvironmentArgsDict,
            original_params=kwargs,
        )

        data = self.__collect_environment_data(
            WIND_SPEED_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
            sanitise=False,
        )

        wind_speed = self.sanitise_data(
            data,
            ignore_keys=WIND_SPEED_SANITISE_IGNORE_KEYS,
        )

        return wind_speed

    # private

    def __collect_environment_data(
        self,
        url: Url,
        params: dict,
        cache_duration: int,
        sanitise=True,
    ) -> Any:
        """Get environment data from the specified endpoint URL.

        If there are pages of data, then compile all of those pages into one \
            big list.

        (Since this method has to call `send_request()`, so the parameters \
            are similar to that method's.)

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires.
        :type cache_duration: int

        :param sanitise: If true, then the response's values are sanitised \
            using the ``sanitise_data()`` method. Defaults to True.
        :type iterate: bool

        :return: data from the endpoint, compiling all pages of readings.
        :rtype: Any (but really a dict)
        """
        response = self.send_request(
            url,
            params=params,
            cache_duration=cache_duration,
            sanitise=sanitise,
        )

        data = response.get('data', {})

        if 'paginationToken' in data:
            pagination_token = data.pop('paginationToken')

            # Collect the next page of data and append it to this one
            params['paginationToken'] = pagination_token

            # Sleep for a bit to avoid hitting the rate limit
            sleep(0.5)

            response_data = self.__collect_environment_data(
                url,
                params=params,
                cache_duration=cache_duration,
                sanitise=sanitise,
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
            if 'area_metadata' in data and 'area_metadata' in response_data:
                data_centre_name = 'area_metadata'
            elif 'regionMetadata' in data and 'regionMetadata' in response_data:
                data_centre_name = 'regionMetadata'
            elif 'stations' in data and 'stations' in response_data:
                data_centre_name = 'stations'
            if data_centre_name != '':
                for data_centre in response_data[data_centre_name]:
                    if data_centre not in data[data_centre_name]:
                        data[data_centre_name].append(data_centre)

        return data

__all__ = [
    'Client',
]
