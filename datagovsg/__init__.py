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

name = 'datagovsg'
version = '1.0.0'
author = 'Yuhui'
author_email = 'yuhuibc@gmail.com'

from datagovsg.ckan import Client as Ckan
from datagovsg.environment import Client as Environment
from datagovsg.technology import Client as Technology
from datagovsg.transport import Client as Transport

__all__ = [
    'Ckan',
    'Environment',
    'Technology',
    'Transport',
]