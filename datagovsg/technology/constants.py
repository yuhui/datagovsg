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

"""Constants for all Technology-related APIs."""

from datagovsg.constants import *

TECHNOLOGY_API_ENDPOINT = '{}/technology'.format(BASE_API_ENDPOINT)

IPOS_API_ENDPOINT = '{}/ipos'.format(TECHNOLOGY_API_ENDPOINT)
IPOS_DESIGNS_API_ENDPOINT = '{}/designs'.format(IPOS_API_ENDPOINT)
IPOS_PATENTS_API_ENDPOINT = '{}/patents'.format(IPOS_API_ENDPOINT)
IPOS_TRADEMARKS_API_ENDPOINT = '{}/trademarks'.format(IPOS_API_ENDPOINT)
