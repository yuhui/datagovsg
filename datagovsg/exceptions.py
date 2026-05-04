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

"""Exceptions that could occur when interacting with any API endpoint."""

from typing import Any

from typeguard import typechecked

ERRORS_MESSAGE = 'Inspect the "errors" attribute for error details.'
DATA_MESSAGE = 'Inspect the "data" attribute for the response data.'

@typechecked
class APIError(Exception):
    """Error when the API returns an error.

    :param message: The general error message to display when the error is \
        raised. Defaults to ``"Unexpected error occurred."``.
    :type message: str
\
    :param data: Data response obtained by the calling method. Defaults to \
        None.
    :type data: Any

    :param errors: Other messages that were part of the raised error. \
        Defaults to None.
    :type message: Any
    """
    def __init__(
        self,
        message: str='Unexpected error occurred.',
        data: Any=None,
        errors: Any=None,
    ) -> None:
        """Constructor method"""
        error_message = message
        if errors is not None:
            error_message = f'{error_message} {ERRORS_MESSAGE}'
        if data is not None:
            error_message = f'{error_message} {DATA_MESSAGE}'

        super().__init__(error_message)
        self.message = error_message
        if errors is not None:
            self.errors = errors
        if data is not None:
            self.data = data

__all__ = [
    'APIError',
]
