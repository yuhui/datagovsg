# Copyright 2019-2025 Yuhui
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

"""Constants for all Traffic-related APIs."""

from ..constants import BASE_V1_API_ENDPOINT

TRANSPORT_API_ENDPOINT = f'{BASE_V1_API_ENDPOINT}/transport'

TAXI_AVAILABILITY_API_ENDPOINT = f'{TRANSPORT_API_ENDPOINT}/taxi-availability'
TRAFFIC_IMAGES_API_ENDPOINT = f'{TRANSPORT_API_ENDPOINT}/traffic-images'

__all__ = [
    'TAXI_AVAILABILITY_API_ENDPOINT',
    'TRAFFIC_IMAGES_API_ENDPOINT',
]