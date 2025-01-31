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

"""Data.gov.sg custom types for Technology client methods' arguments."""

from datetime import date
from typing import NotRequired
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

class TechnologyArgsDict(TypedDict):
    """Type definition for designs(), patents() and trademarks() input \
        arguments
    """

    lodgement_date: NotRequired[date]
    """Retrieve applications lodged at that moment in time.

    :example: date(2025, 1, 12)
    """

__all__ = [
    'TechnologyArgsDict',
]
