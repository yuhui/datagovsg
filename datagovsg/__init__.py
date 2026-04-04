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

"""Package init."""

from datetime import datetime

from .economy import Client as Economy
from .environment import Client as Environment
from .housing import Client as Housing
from .transport import Client as Transport

from .author import AUTHOR
from .version import VERSION

__all__ = [
    'Economy',
    'Environment',
    'Housing',
    'Transport',
]
__author__ = AUTHOR
__version__ = VERSION
