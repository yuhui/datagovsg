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

from ..constants import BASE_V2_API_ENDPOINT

AIR_TEMPERATURE_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/air-temperature'
FOUR_DAY_WEATHER_FORECAST_API_ENDPOINT = \
    f'{BASE_V2_API_ENDPOINT}/four-day-outlook'
PM25_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/pm25'
PSI_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/psi'
RAINFALL_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/rainfall'
RELATIVE_HUMIDITY_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/relative-humidity'
TWENTY_FOUR_HOUR_WEATHER_FORECAST_API_ENDPOINT = \
    f'{BASE_V2_API_ENDPOINT}/twenty-four-hr-forecast'
TWO_HOUR_WEATHER_FORECAST_API_ENDPOINT = \
    f'{BASE_V2_API_ENDPOINT}/two-hr-forecast'
UV_INDEX_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/uv'
WIND_DIRECTION_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/wind-direction'
WIND_SPEED_API_ENDPOINT = f'{BASE_V2_API_ENDPOINT}/wind-speed'
