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

"""Constants for all CKAN-related APIs."""

from datagovsg.constants import *

DATASOURCE_SEARCH_CKAN_ENDPOINT = '{}/datastore_search'.format(
    BASE_CKAN_ENDPOINT,
)
PACKAGE_LIST_CKAN_ENDPOINT = '{}/package_list'.format(BASE_CKAN_ENDPOINT)
PACKAGE_SHOW_CKAN_ENDPOINT = '{}/package_show'.format(BASE_CKAN_ENDPOINT)
RESOURCE_SHOW_CKAN_ENDPOINT = '{}/resource_show'.format(BASE_CKAN_ENDPOINT)
