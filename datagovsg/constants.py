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

BASE_API_DOMAIN = 'https://api.data.gov.sg'
BASE_API_ENDPOINT = '{}/v1'.format(BASE_API_DOMAIN)

BASE_CKAN_DOMAIN = 'https://data.gov.sg'
BASE_CKAN_ENDPOINT = '{}/api/action'.format(BASE_CKAN_DOMAIN)

CACHE_MAXSIZE = 1024
CACHE_ONE_MINUTE = 60
CACHE_FIVE_MINUTES = CACHE_ONE_MINUTE * 5
CACHE_THIRTY_MINUTES = CACHE_ONE_MINUTE * 30
CACHE_ONE_HOUR = CACHE_ONE_MINUTE * 60
CACHE_TWELVE_HOURS = CACHE_ONE_HOUR * 12
CACHE_ONE_DAY = CACHE_ONE_HOUR * 24
