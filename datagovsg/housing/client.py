# Copyright 2025 Yuhui
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

"""Client for interacting with the Housing APIs."""

from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_ONE_MINUTE
from ..datagovsg import DataGovSg

from .constants import (
    CARPARK_AVAILABILITY_API_ENDPOINT,

    CARPARK_AVAILABILITY_SANITISE_IGNORE_KEYS,
)
from .types_args import HousingArgsDict
from .types import CarparkAvailabilityItemDict

class Client(DataGovSg):
    """Interact with the housing-related endpoints.

    Reference: \
        https://data.gov.sg/datasets?formats=API&topics=housing
    """

    @typechecked
    def carpark_availability(
        self,
        **kwargs: Unpack[HousingArgsDict],
    ) -> list[CarparkAvailabilityItemDict]:
        """Get the latest carpark availability in Singapore.

        Retrieved every minute.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: HousingArgsDict

        :return: Available carpark spaces. (Cached for 1 minute.)
        :rtype: CarparkAvailabilityDict
        """
        carpark_availability: list[CarparkAvailabilityItemDict]

        params = self.build_params(
            params_expected_type=HousingArgsDict,
            original_params=kwargs,
        )

        data = self.send_request(
            CARPARK_AVAILABILITY_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_ONE_MINUTE,
            sanitise=False,
        )

        items = data.get('items', [])

        carpark_availability = self.sanitise_data(
            items,
            ignore_keys=CARPARK_AVAILABILITY_SANITISE_IGNORE_KEYS,
        )

        return carpark_availability

__all__ = [
    'Client',
]
