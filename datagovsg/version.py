# Copyright 2026 Yuhui. All rights reserved.
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

"""Package version."""

from datetime import datetime

VERSION = '2.1.0' # Production
# VERSION = f'{VERSION}.dev{datetime.now().strftime("%Y%m%d%H%M")}' # Development

__all__ = [
    'VERSION',
]
