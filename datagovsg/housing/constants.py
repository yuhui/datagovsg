# Copyright 2025-2026 Yuhui
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

"""Constants for all Housing-related APIs."""

from datetime import datetime

from ..constants import BASE_V1_API_ENDPOINT
from ..timezone import datetime_as_sgt

TRANSPORT_API_ENDPOINT = f'{BASE_V1_API_ENDPOINT}/transport'

CARPARK_AVAILABILITY_API_ENDPOINT = \
    f'{TRANSPORT_API_ENDPOINT}/carpark-availability'

CARPARK_AVAILABILITY_SANITISE_IGNORE_KEYS = [
    '[].carpark_data[].carpark_number',
]

MIN_DATETIME = datetime_as_sgt(datetime(2018, 1, 1, 0, 0, 0))

INVALID_DATETIME_ERROR_MESSAGE_FORMAT = 'date_time must be on or after {}.'
INVALID_DATETIME_ERROR_MESSAGE = INVALID_DATETIME_ERROR_MESSAGE_FORMAT.format(
    MIN_DATETIME,
)

__all__ = [
    'CARPARK_AVAILABILITY_API_ENDPOINT',

    'CARPARK_AVAILABILITY_SANITISE_IGNORE_KEYS',

    'MIN_DATETIME',
    'INVALID_DATETIME_ERROR_MESSAGE',
]
