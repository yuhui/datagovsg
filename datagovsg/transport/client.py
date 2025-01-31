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

from ..constants import CACHE_THIRTY_SECONDS, CACHE_ONE_MINUTE
from ..datagovsg import DataGovSg

from .constants import (
    CARPARK_AVAILABILITY_API_ENDPOINT,
    TAXI_AVAILABILITY_API_ENDPOINT,
    TRAFFIC_IMAGES_API_ENDPOINT,
)

class Client(DataGovSg):
    """Interact with the transport-related endpoints."""

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
        params = self.build_params(kwargs)

        carpark_availabilities = self.send_request(
            CARPARK_AVAILABILITY_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
            sanitise_numbers=True,
        )

        return carpark_availabilities

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
        params = self.build_params(kwargs)

        taxi_availabilities = self.send_request(
            TAXI_AVAILABILITY_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_THIRTY_SECONDS,
        )

        return taxi_availabilities

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
        params = self.build_params(kwargs)

        traffic_images = self.send_request(
            TRAFFIC_IMAGES_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
        )

        return traffic_images

__all__ = [
    'Client',
]
