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

"""Data.gov.sg custom types for Housing client methods' arguments."""

from datetime import datetime
from typing import NotRequired
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

class HousingArgsDict(TypedDict):
    """Type definition for carpark_availability() input arguments"""

    date_time: NotRequired[datetime]
    """Retrieve the latest availability at that moment in time.

    :example: datetime(2024, 7, 16, 23, 59, 0)
    """

__all__ = [
    'HousingArgsDict',
]
