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

"""Constants for all Traffic-related APIs."""

from datagovsg.constants import *

TRANSPORT_API_ENDPOINT = '{}/transport'.format(BASE_API_ENDPOINT)
CARPARK_AVAILABILITY_API_ENDPOINT = '{}/carpark-availability'.format(
    TRANSPORT_API_ENDPOINT,
)
TAXI_AVAILABILITY_API_ENDPOINT = '{}/taxi-availability'.format(
    TRANSPORT_API_ENDPOINT,
)
TRAFFIC_IMAGES_API_ENDPOINT = '{}/traffic-images'.format(
    TRANSPORT_API_ENDPOINT,
)
