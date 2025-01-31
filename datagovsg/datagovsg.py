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

"""Client mixin for interacting with all of the API endpoints."""

from datetime import date, datetime
from typing import Any, Optional

from requests import codes as requests_codes
from requests.adapters import HTTPAdapter, Retry
from requests_cache import CachedSession
from typeguard import typechecked

from .constants import CACHE_NAME, USER_AGENT
from .timezone import datetime_from_string
from .types import Url

class DataGovSg:
    """Client mixin for other API Clients.

    Normally, it does not need to be created by applications. But \
        applications may use the public methods provided here.

    The constructor sets the following:

    - Connection retries using exponential backoff. \
        (Reference: https://stackoverflow.com/a/35504626.)
    - Cache (cache duration/expiry is set in ``send_request()``).
    - User-agent header.
    """

    @typechecked
    def __init__(self) -> None:
        """Constructor method"""
        retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504]
        )

        self.session = CachedSession(CACHE_NAME, stale_if_error=False)
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': USER_AGENT,
        })

    @typechecked
    def __repr__(self) -> str:
        """String representation"""
        return f'{self.__class__}'

    @typechecked
    def build_params(
        self,
        original_params: Any,
        default_params: dict | None=None,
    ) -> dict:
        """Build the list of parameters that are compatible for use with the \
            endpoint URLs, e.g. datetime objects to strings.

        :param original_params: The set of parameters to use for building.
        :type original_params: Any but should really be dict

        :param default_params: The set of parameters' default values. \
            Defaults to None.
        :type default_params: dict or None

        :return: The set of parameters that can be used with the API endpoints.
        :rtype: dict
        """
        if default_params is None:
            default_params = {}
        joined_params = default_params | original_params

        params: dict = {}
        for key, value in joined_params.items():
            # Convert date and datetime to ISO format strings
            # Leave all other types as-is
            # IMPORTANT! Test for `datetime` before `date`!
            if isinstance(value, datetime):
                params[key] = value.strftime('%Y-%m-%dT%H:%M:%S')
            elif isinstance(value, date):
                params[key] = value.isoformat()
            else:
                params[key] = value

        return params

    @typechecked
    def sanitise_data(
        self,
        value: Any,
        iterate: bool=True,
        sanitise_numbers: bool=False,
    ) -> Any:
        """Convert the following:

        - String that is like date or datetime: convert to ``datetime.date`` \
            or ``datetime.datetime`` object respectively.

        :param value: Value to sanitise.
        :type value: Any

        :param iterate: If True, then ``list`` and ``dict`` objects are \
            sanitised recursively. Defaults to True.
        :type iterate: bool

        :param sanitise_numbers: If True, then strings that are like numbers \
            are converted to ``int`` or ``float`` appropriately. Defaults to \
            False.
        :type sanitise_numbers: bool

        :return: The sanitised value.
        :rtype: Any
        """
        sanitised_value: Any = value

        if iterate and isinstance(value, list):
            sanitised_value = [
                self.sanitise_data(
                    v,
                    iterate=iterate,
                    sanitise_numbers=sanitise_numbers,
                ) for v in value
            ]
        elif iterate and isinstance(value, dict):
            sanitised_value = {}
            for k, v in value.items():
                sanitised_value[k] = self.sanitise_data(
                    v,
                    iterate=iterate,
                    sanitise_numbers=sanitise_numbers,
                )
        elif isinstance(value, str):
            try:
                # pylint: disable=broad-exception-caught

                # Convert to a date/datetime.
                sanitised_value = datetime_from_string(value)
            except Exception:
                if sanitise_numbers:
                    try:
                        # Convert to an integer
                        sanitised_value = int(value)
                    except Exception:
                        try:
                            # Convert to a float
                            sanitised_value = float(value)
                        except Exception:
                            pass

        return sanitised_value

    @typechecked
    def send_request(
        self,
        url: Url,
        params: Optional[dict | str]=None,
        cache_duration: Optional[int]=0,
        sanitise: bool=True,
        sanitise_numbers: bool=False,
    ) -> Any:
        """Send a request to an endpoint.

        Normally, this method does not need to be called directly. However, \
            if SingStat were to change their API specification but this \
            package has not yet been updated to support that change, then \
            applications may use this method to call the changed endpoints.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters or parameter string to be passed to \
            the endpoint URL. Parameter names **must** match the names \
            required by the endpoints, particularly with typecase (e.g. \
            camelCase). Defaults to None.
        :type params: dict | str

        :param cache_duration: Number of seconds before the cache expires. \
            Defaults to 0, i.e. do not cache.
        :type cache_duration: int

        :param sanitise: If true, then the response's values are sanitised \
            using the ``sanitise_data()`` method. Defaults to True.
        :type iterate: bool

        :param sanitise_numbers: If True, then sanitises number-like strings. \
            Applicable only when ``sanitise`` argument is True. Defaults to \
            False.
        :type sanitise_numbers: bool

        :raises HTTPError: Error occurred during the request process.

        :return: Response JSON content of the request.
        :rtype: Any
        """
        data: Any

        if params is None:
            params = {}

        response = self.session.get(
            url,
            params=params,
            expire_after=cache_duration,
        )
        if response.status_code != requests_codes['ok']:
            response.raise_for_status()

        response_json = {}
        try:
            response_json = response.json()
        except ValueError:
            pass

        data = self.sanitise_data(
            response_json,
            sanitise_numbers=sanitise_numbers,
        ) if sanitise else response_json

        return data

__all__ = [
    'DataGovSg',
]
