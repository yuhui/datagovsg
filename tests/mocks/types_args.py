# Copyright 2024-2026 Yuhui. All rights reserved.
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

"""Mock custom input types."""

from datetime import date, datetime
from typing import NotRequired, TypedDict

class MockArgsDict(TypedDict):
    """Type definition for unit testing"""
    foobar: str
    date: date
    datetime: datetime
    meaning_of_universe: NotRequired[int]
    none_value: NotRequired[None]

__all__ = [
    'MockArgsDict',
]
