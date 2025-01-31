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

"""Constants that can be used anywhere."""

BASE_V1_API_ENDPOINT = 'https://api.data.gov.sg/v1'
BASE_V2_API_ENDPOINT = 'https://api-open.data.gov.sg/v2/real-time/api'

CACHE_NAME = 'datagovsg_cache'

CACHE_THIRTY_SECONDS = 30
CACHE_ONE_MINUTE = CACHE_THIRTY_SECONDS * 2
CACHE_FIVE_MINUTES = CACHE_ONE_MINUTE * 5
CACHE_THIRTY_MINUTES = CACHE_ONE_MINUTE * 30
CACHE_ONE_HOUR = CACHE_ONE_MINUTE * 60
CACHE_TWELVE_HOURS = CACHE_ONE_HOUR * 12
CACHE_ONE_DAY = CACHE_ONE_HOUR * 24

USER_AGENT = 'Data.gov.sg Python package/2.0.0 https://pypi.org/project/datagovsg'

__all__ = [
    'BASE_V1_API_ENDPOINT',
    'BASE_V2_API_ENDPOINT',

    'CACHE_NAME',

    'CACHE_THIRTY_SECONDS',
    'CACHE_ONE_MINUTE',
    'CACHE_FIVE_MINUTES',
    'CACHE_THIRTY_MINUTES',
    'CACHE_ONE_HOUR',
    'CACHE_TWELVE_HOURS',
    'CACHE_ONE_DAY',

    'USER_AGENT',
]
