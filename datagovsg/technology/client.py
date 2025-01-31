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
    """Interact with the technology-related endpoints.

    Reference: \
        https://data.gov.sg/datasets?formats=API&topics=technology
    """

    @typechecked
    def designs(self, **kwargs: Unpack[TechnologyArgsDict]) -> DesignsDict:
        """Get design applications lodged with IPOS in Singapore.

        Updated daily from IPOS.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: TechnologyArgsDict

        :return: Design application information. (Cached for 12 hours.)
        :rtype: DesignsDict
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

        Updated daily from IPOS.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: TechnologyArgsDict

        :return: Patent application information. (Cached for 12 hours.)
        :rtype: PatentsDict
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

        Updated daily from IPOS.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: TechnologyArgsDict

        :return: Trademark application information. (Cached for 12 hours.)
        :rtype: TrademarksDict
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
