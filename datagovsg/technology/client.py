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

"""Client for interacting with the Technology APIs."""

from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_TWELVE_HOURS
from ..datagovsg import DataGovSg

from .constants import (
    IPOS_DESIGNS_API_ENDPOINT,
    IPOS_PATENTS_API_ENDPOINT,
    IPOS_TRADEMARKS_API_ENDPOINT,
)
from .types_args import TechnologyArgsDict
from .types import (
    DesignsDict,
    PatentsDict,
    TrademarksDict,
)

class Client(DataGovSg):
    """Interact with the technology-related endpoints."""

    @typechecked
    def designs(self, **kwargs: Unpack[TechnologyArgsDict]) -> DesignsDict:
        """Get design applications lodged with IPOS in Singapore.

        Arguments:
            date (date):
                (optional) Specific date to retrieve the lodged designs
                on that date.
                Can be in any timezone (will be standardised to SGT.)

        Returns:
            (dict) Design applications that have been lodged.

        References:
            https://data.gov.sg/dataset/ipos-apis?resource_id=adf6222f-955b-4a76-892f-802a396844a1
        """
        designs: DesignsDict

        params = self.build_params(kwargs)

        designs = self.send_request(
            IPOS_DESIGNS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return designs

    @typechecked
    def patents(self, **kwargs: Unpack[TechnologyArgsDict]) -> PatentsDict:
        """Get patent applications lodged with IPOS in Singapore.

        Arguments:
            date (date):
                (optional) Specific date to retrieve the lodged patents
                on that date.
                Can be in any timezone (will be standardised to SGT.)

        Returns:
            (dict) Patent applications that have been lodged.

        References:
            https://data.gov.sg/dataset/ipos-apis?resource_id=6a030bf2-22da-4621-8ab0-9a5956a30ef3
        """
        patents: PatentsDict

        params = self.build_params(kwargs)

        patents = self.send_request(
            IPOS_PATENTS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return patents

    @typechecked
    def trademarks(self, **kwargs: Unpack[TechnologyArgsDict]) -> TrademarksDict:
        """Get trademark applications lodged with IPOS in Singapore.

        Arguments:
            date (date):
                (optional) Specific date to retrieve the lodged trademarks
                on that date.
                Can be in any timezone (will be standardised to SGT.)

        Returns:
            (dict) Trademark applications that have been lodged.

        References:
            https://data.gov.sg/dataset/ipos-apis?resource_id=1522db0e-808b-48ea-9869-fe5adc566585
        """
        trademarks: TrademarksDict

        params = self.build_params(kwargs)

        trademarks = self.send_request(
            IPOS_TRADEMARKS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return trademarks

__all__ = [
    'Client',
]
