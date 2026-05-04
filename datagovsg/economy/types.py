# Copyright 2025-2026 Yuhui. All rights reserved.
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

"""Data.gov.sg custom types for Economy client methods' responses.

Due to the poor state of the documentation provided by Data.gov.sg, the types \
are purposely left as general ``dict`` or ``list[dict]`` where possible to \
avoid overfitting to the current implementation of the API responses, which \
may change without notice and break the type definitions.
"""

from datetime import date
from typing import Any, TypedDict

class EconomyDict(TypedDict):
    """Type definition for designs(), patents() and trademarks()"""

    lodgement_date: date
    """Date of lodgement of application from IPOS.

    :example: date(2025, 1, 12, tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    count: int
    """Count."""
    items: list[dict[str, Any]]
    """Items."""

__all__ = [
    'EconomyDict',
]
