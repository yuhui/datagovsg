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

from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_THIRTY_SECONDS, CACHE_ONE_MINUTE
from ..datagovsg import DataGovSg

from .constants import (
    TAXI_AVAILABILITY_API_ENDPOINT,
    TRAFFIC_IMAGES_API_ENDPOINT,
)
from .types_args import TransportArgsDict
from .types import (
    TaxiAvailabilityDict,
    TrafficImagesDict,
)

class Client(DataGovSg):
    """Interact with the transport-related endpoints.

    Reference: \
        https://data.gov.sg/datasets?formats=API&topics=transport
    """

    @typechecked
    def taxi_availability(
        self,
        **kwargs: Unpack[TransportArgsDict],
    ) -> TaxiAvailabilityDict:
        """Get locations of available taxis in Singapore.

        Retrieved every 30 seconds from LTA's Datamall.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: TransportArgsDict

        :return: GeoJSON of the taxi availabilities. (Cached for 30 seconds.)
        :rtype: TaxiAvailabilityDict
        """
        taxi_availability: TaxiAvailabilityDict

        params = self.build_params(kwargs)

        taxi_availability = self.send_request(
            TAXI_AVAILABILITY_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_THIRTY_SECONDS,
        )

        return taxi_availability

    @typechecked
    def traffic_images(
        self,
        **kwargs: Unpack[TransportArgsDict],
    ) -> TrafficImagesDict:
        """Get the latest images from traffic cameras all around Singapore.

        Retrieved every 20 seconds from LTA's Datamall. But it is recommended \
            to retrieve the data every minute.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: TransportArgsDict

        :return: Images from traffic cameras. (Cached for 1 minute.)
        :rtype: TrafficImagesDict
        """
        traffic_images: TrafficImagesDict

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
