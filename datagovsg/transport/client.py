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

"""Client for interacting with the Transport APIs."""

from cachetools import cached, TTLCache

from datagovsg import net
from datagovsg.client import __Client
from datagovsg.transport.constants import *

class Client(__Client):
    """Interact with the transport-related endpoints."""

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def carpark_availability(self, date_time=None):
        """Get the latest carpark availability in Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the availabilities
                at that time.
                Can be in any timezone (will be standardised to SGT.)

        Returns:
            (dict) Available carpark spaces.

        References:
            https://data.gov.sg/dataset/carpark-availability
        """
        carpark_availabilities = net.send_request(
            CARPARK_AVAILABILITY_API_ENDPOINT,
            date_time=date_time,
        )

        return carpark_availabilities

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def taxi_availability(self, date_time=None):
        """Get locations of available taxis in Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the availabilities
                at that time.
                Can be in any timezone (will be standardised to SGT.)

        Returns:
            (dict) GeoJSON of the taxi availabilities.

        References:
            https://data.gov.sg/dataset/taxi-availability
        """
        taxi_availabilities = net.send_request(
            TAXI_AVAILABILITY_API_ENDPOINT,
            accept_type='vnd.geo+json',
            date_time=date_time,
        )

        return taxi_availabilities

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_MINUTE))
    def traffic_images(self, date_time=None):
        """Get the latest images from traffic cameras all around Singapore.

        Arguments:
            date_time (datetime):
                (optional) Specific date-time to retrieve the images
                at that time.
                Can be in any timezone (will be standardised to SGT.)

        Returns:
            (dict) Images from traffic cameras.

        References:
            https://data.gov.sg/dataset/traffic-images
        """
        traffic_images = net.send_request(
            TRAFFIC_IMAGES_API_ENDPOINT,
            date_time=date_time,
        )

        return traffic_images
