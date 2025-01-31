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

from datetime import datetime

from .ckan import Client as Ckan
from .environment import Client as Environment
from .technology import Client as Technology
from .transport import Client as Transport

NAME = 'datagovsg'
VERSION = '2.0.0' # Production
VERSION = f'{VERSION}.{datetime.now().strftime("%Y%m%d%H%M")}' # Development
AUTHOR = 'Yuhui'
AUTHOR_EMAIL = 'yuhuibc@gmail.com'

__all__ = [
    'Ckan',
    'Environment',
    'Technology',
    'Transport',
]
__version__ = VERSION
