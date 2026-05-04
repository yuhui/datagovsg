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

"""Client mixin for interacting with all of the API endpoints."""

from datetime import date, datetime
from typing import Any

from requests import codes as requests_codes
from requests.adapters import HTTPAdapter, Retry
from requests_cache import BaseCache, CachedSession
from typeguard import check_type, typechecked, TypeCheckError

from .constants import CACHE_NAME, USER_AGENT
from .exceptions import APIError
from .timezone import (
    datetime_from_string,
    datetime_to_string,
)
from .types import Url

class DataGovSg:
    """Client mixin for other API Clients.

    Normally, it does not need to be created by applications. But \
        applications may use the public methods provided here.

    The constructor sets the following:

    - Connection retries using exponential backoff. \
        (Reference: https://stackoverflow.com/a/35504626.)
    - Cache (cache duration/expiry is set in ``send_request()``).
    - API key that can be used with api.data.gov.sg. \
        Create a key for api.data.gov.sg: \
        https://guide.data.gov.sg/developer-guide/api-overview/how-to-request-an-api-key.
    - User-agent header.

    :param api_key: The assigned API key for api.data.gov.sg. Defaults to None.
    :type api_key: str or None

    :param cache_backend: Cache backend name or instance to use. Refer to \
        https://requests-cache.readthedocs.io/en/stable/user_guide/backends.html \
        for more information and allowed values. Defaults to "sqlite".
    :type cache_backend: str or BaseCache
    """

    @typechecked
    def __init__(
        self,
        api_key: str | None=None,
        cache_backend: str | BaseCache='sqlite',
    ) -> None:
        """Constructor method"""
        headers = {
            'Accept': 'application/json',
            'User-Agent': USER_AGENT,
        }
        if api_key is not None:
            headers['x-api-key'] = api_key

        retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504]
        )

        self.session = CachedSession(
            CACHE_NAME,
            backend=cache_backend,
            stale_if_error=False,
        )
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.headers.update(headers)

    @typechecked
    def __repr__(self) -> str:
        """String representation"""
        return f'{self.__class__} ({USER_AGENT})'

    @typechecked
    def build_params(
        self,
        params_expected_type: Any,
        original_params: Any,
        default_params: dict | None=None,
        key_map: dict[str, str] | None=None,
    ) -> dict:
        """Build the list of parameters that are compatible for use with the \
            endpoint URLs, e.g. camelCase parameter names instead of Python's \
            snake_case, datetime objects to strings.

        :param params_expected_type: The expected type of \
            ``original_params``. Should be one of the importable types from \
            the client's ``types_args``.
        :type params_expected_type: Any

        :param original_params: The set of parameters to use for building.
        :type original_params: Any but should really be dict

        :param default_params: The set of parameters' default values. Should \
            be of the same type as what is specified in \
            ``params_expected_type``. Defaults to None.
        :type default_params: dict or None

        :param key_map: Mapping of keys used in ``params_expected_types`` to \
            keys expected by the endpoint. Defaults to None.
        :type key_map: dict[str, str] or None

        :return: The set of parameters that can be used with the API endpoints.
        :rtype: dict
        """
        if default_params is None:
            default_params = {}
        if key_map is None:
            key_map = {}

        joined_params = default_params | original_params

        # Ensure that the parameters match the expected input parameter types.
        _ = check_type(joined_params, params_expected_type)

        params: dict = {}
        for key, value in joined_params.items():
            param_key = key_map[key] if key in key_map else key

            # Convert date and datetime to ISO format strings
            # Leave all other types as-is
            try:
                params[param_key] = datetime_to_string(value)
            except TypeCheckError:
                params[param_key] = value

        return params

    @typechecked
    def sanitise_data(
        self,
        value: Any,
        iterate: bool=True,
        ignore_keys: list[str] | None=None,
        key_path: str='',
    ) -> Any:
        """Convert the following:

        - If ``iterate`` is True and value is a ``dict`` or ``list``: \
            sanitise the value's contents.
        - Blank string: convert to None.
        - String that is like date or datetime: convert to ``datetime.date`` \
            or ``datetime.datetime`` object respectively.
        - String that is number-like: convert to ``int`` or ``float`` \
            appropriately.
        - Finally: Leave the value as-is.

        :param value: Value to sanitise.
        :type value: Any

        :param iterate: If True, then ``list`` and ``dict`` objects are \
            sanitised recursively. Defaults to True.
        :type iterate: bool

        :param ignore_keys: List of dict keys to ignore when sanitising, if \
            value is a ``dict``. Defaults to [].
        :type ignore_keys: list[str]

        :param key_path: Current path of key in the dict. Defaults to blank \
            string.
        :type key_path: str

        :return: The sanitised value.
        :rtype: Any
        """
        if ignore_keys is None:
            ignore_keys = []

        sanitised_value: Any = value

        if iterate and isinstance(value, list):
            sanitised_value = [
                self.sanitise_data(
                    v,
                    iterate=iterate,
                    ignore_keys=ignore_keys,
                    key_path=f'{key_path}[]'
                ) for v in value
            ]
        elif iterate and isinstance(value, dict):
            sanitised_value = {}
            for k, v in value.items():
                current_key_path = '.'.join([key_path, k]) if key_path else k
                if isinstance(v, str) and v == '':
                    sanitised_value[k] = self.sanitise_data(v)
                elif current_key_path in ignore_keys:
                    sanitised_value[k] = v
                else:
                    sanitised_value[k] = self.sanitise_data(
                        v,
                        iterate=iterate,
                        ignore_keys=ignore_keys,
                        key_path=current_key_path,
                    )
        elif isinstance(value, str):
            if value == '':
                sanitised_value = None
            else:
                try:
                    # pylint: disable=broad-exception-caught

                    # Convert to a date/datetime.
                    sanitised_value = datetime_from_string(value)
                except Exception:
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
        params: dict | None=None,
        cache_duration: int=0,
        sanitise: bool=True,
        sanitise_ignore_keys: list[str] | None=None,
    ) -> Any:
        """Send a request to an endpoint and return its response.

        Normally, this method does not need to be called directly. However, \
            if Data.gov.sg were to change their API specification but this \
            package has not yet been updated to support that change, then \
            applications may use this method to call the changed endpoints.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL. \
            Parameter names **must** match the names required by the \
            endpoints, particularly with typecase (e.g. camelCase). Defaults \
            to {}.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires. \
            Defaults to 0, i.e. do not cache.
        :type cache_duration: int

        :param sanitise: If true, then the response's values are sanitised \
            using the ``sanitise_data()`` method. Defaults to True.
        :type sanitise: bool

        :param sanitise_ignore_keys: List of keys to ignore in the response \
            value during sanitising when that response value is a ``dict``. \
            Defaults to [].
        :type sanitise_ignore_keys: list[str]

        :raises HTTPError: Error occurred during the request process.

        :return: Results from the response.
        :rtype: Any
        """
        data: Any

        if params is None:
            params = {}

        if sanitise_ignore_keys is None:
            sanitise_ignore_keys = []

        response_val = self.__collect_response_value(
            url,
            params=params,
            cache_duration=cache_duration,
        )

        data = self.sanitise_data(
            response_val,
            ignore_keys=sanitise_ignore_keys,
        ) if sanitise else response_val

        return data

# private

    @typechecked
    def __collect_response_value(
        self,
        url: Url,
        params: dict,
        cache_duration: int,
    ) -> Any:
        """Collect response value from an endpoint.

        :param url: The endpoint URL to send the request to.
        :type url: Url

        :param params: List of parameters to be passed to the endpoint URL.
        :type params: dict

        :param cache_duration: Number of seconds before the cache expires.
        :type cache_duration: int

        :raises HTTPError: Error occurred during the request process.

        :return: Results from the response.
        :rtype: Any
        """
        response_value: Any

        response = self.session.get(
            url,
            params=params,
            expire_after=cache_duration,
        )

        response_json = {}
        try:
            response_json = response.json()
        except ValueError:
            pass

        if response.status_code == requests_codes['bad_request'] \
            or response.status_code == requests_codes['not_found'] \
            or response.status_code == requests_codes['too_many_requests']:
            error_message = response_json.get(
                'errorMsg',
                'Unexpected error occurred',
            )
            raise APIError(
                message=error_message,
                data=response_json,
            )

        if response.status_code != requests_codes['ok']:
            response.raise_for_status()

        # handle Data.gov.sg API's default response
        if response_json.get('code', 0) != 0:
            error_message = response_json.get(
                'message',
                'Unexpected error occurred',
            )
            raise APIError(
                message=error_message,
                data=response_json,
            )

        response_value = response_json

        return response_value

__all__ = [
    'DataGovSg',
]
