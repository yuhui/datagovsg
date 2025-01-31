# Copyright 2025 Yuhui. All rights reserved.
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

"""Data.gov.sg custom types for Housing client methods' responses."""

from datetime import datetime
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

# Carpark Availability

class _CarparkAvailabilityItemDataInfoDict(TypedDict):
    """Type definition for _CarparkAvailabilityItemDataDict"""

    total_lots: int
    """Total number of carpark lots.

    :example: 105
    """
    lot_type: str
    """Type of carpark lot.

    :example: "C"
    """
    lots_available: int
    """Total number of available carpark lots.

    :example: 86
    """

class _CarparkAvailabilityItemDataDict(TypedDict):
    """Type definition for _CarparkAvailabilityItemDict"""

    carpark_info: list[_CarparkAvailabilityItemDataInfoDict]
    """Carpark information."""
    carpark_number: str
    """Carpark number.

    :example: "HE12"
    """
    update_datetime: datetime
    """Update date-time.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """

class _CarparkAvailabilityItemDict(TypedDict):
    """Type definition for CarparkAvailabilityDict"""

    timestamp: datetime
    """Time of acquisition of data.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    carpark_data: list[_CarparkAvailabilityItemDataDict]
    """Carpark availability information per carpark."""

class CarparkAvailabilityDict(TypedDict):
    """Type definition for carpark_availability()"""

    items: list[_CarparkAvailabilityItemDict]
    """Items."""

__all__ = [
    'CarparkAvailabilityDict',
]
