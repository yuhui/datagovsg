# Copyright 2019-2026 Yuhui
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

"""Client for interacting with the Economy APIs."""

from typing import Unpack

from typeguard import typechecked

from ..constants import CACHE_TWELVE_HOURS
from ..datagovsg import DataGovSg

from .constants import (
    IPOS_DESIGNS_API_ENDPOINT,
    IPOS_PATENTS_API_ENDPOINT,
    IPOS_TRADEMARKS_API_ENDPOINT,

    MIN_DATETIME,
    MAX_DATETIME,

    INVALID_DATE_ERROR_MESSAGE,
)
from .types_args import EconomyArgsDict
from .types import EconomyDict

class Client(DataGovSg):
    """Interact with the economy-related endpoints.

    Reference: \
        https://data.gov.sg/datasets?formats=API&topics=economy
    """

    @typechecked
    def designs(self, **kwargs: Unpack[EconomyArgsDict]) -> EconomyDict:
        """Get design applications lodged with IPOS in Singapore.

        Updated daily from IPOS.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EconomyArgsDict

        :raises ValueError: ``lodgement_date`` argument is not between 1 \
            August 2018 and 31 October 2020 (start and end dates inclusive).

        :return: Design application information. (Cached for 12 hours.)
        :rtype: EconomyDict
        """
        self.validate_date(
            kwargs=kwargs,
            date_key='lodgement_date',
            error_message=INVALID_DATE_ERROR_MESSAGE,
            min_dt=MIN_DATETIME,
            max_dt=MAX_DATETIME,
        )

        designs: EconomyDict

        params = self.build_params(
            params_expected_type=EconomyArgsDict,
            original_params=kwargs,
        )

        designs = self.send_request(
            IPOS_DESIGNS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return designs

    @typechecked
    def patents(self, **kwargs: Unpack[EconomyArgsDict]) -> EconomyDict:
        """Get patent applications lodged with IPOS in Singapore.

        Updated daily from IPOS.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EconomyArgsDict

        :raises ValueError: ``lodgement_date`` argument is not between 1 \
            August 2018 and 31 October 2020 (start and end dates inclusive).

        :return: Patent application information. (Cached for 12 hours.)
        :rtype: EconomyDict
        """
        self.validate_date(
            kwargs=kwargs,
            date_key='lodgement_date',
            error_message=INVALID_DATE_ERROR_MESSAGE,
            min_dt=MIN_DATETIME,
            max_dt=MAX_DATETIME,
        )

        patents: EconomyDict

        params = self.build_params(
            params_expected_type=EconomyArgsDict,
            original_params=kwargs,
        )

        patents = self.send_request(
            IPOS_PATENTS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return patents

    @typechecked
    def trademarks(self, **kwargs: Unpack[EconomyArgsDict]) -> EconomyDict:
        """Get trademark applications lodged with IPOS in Singapore.

        Updated daily from IPOS.

        :param kwargs: Key-value arguments to be passed as parameters to the \
            endpoint URL.
        :type kwargs: EconomyArgsDict

        :raises ValueError: ``lodgement_date`` argument is not between 1 \
            August 2018 and 31 October 2020 (start and end dates inclusive).

        :return: Trademark application information. (Cached for 12 hours.)
        :rtype: EconomyDict
        """
        self.validate_date(
            kwargs=kwargs,
            date_key='lodgement_date',
            error_message=INVALID_DATE_ERROR_MESSAGE,
            min_dt=MIN_DATETIME,
            max_dt=MAX_DATETIME,
        )

        trademarks: EconomyDict

        params = self.build_params(
            params_expected_type=EconomyArgsDict,
            original_params=kwargs,
        )

        trademarks = self.send_request(
            IPOS_TRADEMARKS_API_ENDPOINT,
            params=params,
            cache_duration=CACHE_TWELVE_HOURS,
        )

        return trademarks

__all__ = [
    'Client',
]
