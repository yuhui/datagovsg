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

from ..constants import BASE_V1_API_ENDPOINT

TECHNOLOGY_API_ENDPOINT = f'{BASE_V1_API_ENDPOINT}/technology'

IPOS_API_ENDPOINT = f'{TECHNOLOGY_API_ENDPOINT}/ipos'

IPOS_DESIGNS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/designs'
IPOS_PATENTS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/patents'
IPOS_TRADEMARKS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/trademarks'IPOS_TRADEMARKS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/trademarks'