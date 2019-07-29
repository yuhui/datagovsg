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

"""Constants for all Environment-related APIs."""

from datagovsg.constants import *

ENVIRONMENT_API_ENDPOINT = '{}/environment'.format(BASE_API_ENDPOINT)
AIR_TEMPERATURE_API_ENDPOINT = '{}/air-temperature'.format(
    ENVIRONMENT_API_ENDPOINT,
)
PM25_API_ENDPOINT = '{}/pm25'.format(ENVIRONMENT_API_ENDPOINT)
PSI_API_ENDPOINT = '{}/psi'.format(ENVIRONMENT_API_ENDPOINT)
RAINFALL_API_ENDPOINT = '{}/rainfall'.format(ENVIRONMENT_API_ENDPOINT)
RELATIVE_HUMIDITY_API_ENDPOINT = '{}/relative-humidity'.format(
    ENVIRONMENT_API_ENDPOINT,
)
UV_INDEX_API_ENDPOINT = '{}/uv-index'.format(ENVIRONMENT_API_ENDPOINT)
TWO_HOUR_WEATHER_FORECAST_API_ENDPOINT = '{}/2-hour-weather-forecast'.format(
    ENVIRONMENT_API_ENDPOINT,
)
TWENTY_FOUR_HOUR_WEATHER_FORECAST_API_ENDPOINT = \
    '{}/24-hour-weather-forecast'.format(
        ENVIRONMENT_API_ENDPOINT,
    )
FOUR_DAY_WEATHER_FORECAST_API_ENDPOINT = '{}/4-day-weather-forecast'.format(
    ENVIRONMENT_API_ENDPOINT,
)
WIND_DIRECTION_API_ENDPOINT = '{}/wind-direction'.format(
    ENVIRONMENT_API_ENDPOINT,
)
WIND_SPEED_API_ENDPOINT = '{}/wind-speed'.format(ENVIRONMENT_API_ENDPOINT)
