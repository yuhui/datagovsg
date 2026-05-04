# Copyright 2019-2026 Yuhui
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

"""Constants for all Economy-related APIs."""

from datetime import datetime

from ..constants import BASE_V1_API_ENDPOINT
from ..timezone import datetime_as_sgt

ECONOMY_API_ENDPOINT = f'{BASE_V1_API_ENDPOINT}/technology'

IPOS_API_ENDPOINT = f'{ECONOMY_API_ENDPOINT}/ipos'

IPOS_DESIGNS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/designs'
IPOS_PATENTS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/patents'
IPOS_TRADEMARKS_API_ENDPOINT = f'{IPOS_API_ENDPOINT}/trademarks'

MIN_DATETIME = datetime_as_sgt(datetime(2018, 8, 1, 0, 0, 0))
MAX_DATETIME = datetime_as_sgt(datetime(2020, 10, 31, 23, 59, 59))

INVALID_DATE_ERROR_MESSAGE_FORMAT = \
    'lodgement_date must be between {} and {} (inclusive)'
INVALID_DATE_ERROR_MESSAGE = INVALID_DATE_ERROR_MESSAGE_FORMAT.format(
    MIN_DATETIME,
    MAX_DATETIME,
)

__all__ = [
    'IPOS_DESIGNS_API_ENDPOINT',
    'IPOS_PATENTS_API_ENDPOINT',
    'IPOS_TRADEMARKS_API_ENDPOINT',

    'MIN_DATETIME',
    'MAX_DATETIME',
    'INVALID_DATE_ERROR_MESSAGE',
]
