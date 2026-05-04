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

# pylint: disable=invalid-name,missing-function-docstring,redefined-outer-name,unused-argument

"""Test that the Exceptions are working properly."""

import pytest

from datagovsg.exceptions import APIError

DEFAULT_MESSAGE = 'Unexpected error occurred.'
ERRORS_MESSAGE = 'Inspect the "errors" attribute for error details.'
DATA_MESSAGE = 'Inspect the "data" attribute for the response data.'

@pytest.mark.parametrize(
    ('message', 'data', 'errors'),
    [
        ('pytest', {'Message': 'pytest message'}, {'error': 'pytest error'}),
        ('pytest', {'Message': 'pytest message'}, None),
        ('pytest', None, {'error': 'pytest error'}),
        (None, {'Message': 'pytest message'}, {'error': 'pytest error'}),
        ('pytest', None, None),
        (None, {'Message': 'pytest message'}, None),
        (None, None, {'error': 'pytest error'}),
        (None, None, None),
    ],
)
def test_raising_APIError(message, data, errors):
    with pytest.raises(APIError) as excinfo:
        if message and data and errors:
            raise APIError(message=message, data=data, errors=errors)
        elif message and data:
            raise APIError(message=message, data=data)
        elif message and errors:
            raise APIError(message=message, errors=errors)
        elif data and errors:
            raise APIError(data=data, errors=errors)
        elif message:
            raise APIError(message=message)
        elif data:
            raise APIError(data=data)
        elif errors:
            raise APIError(errors=errors)
        else:
            raise APIError()

    expected_error_message = message if message else DEFAULT_MESSAGE

    if errors is None:
        assert not hasattr(excinfo.value, 'errors')
    else:
        expected_error_message = f'{expected_error_message} {ERRORS_MESSAGE}'
        assert excinfo.value.errors == errors

    if data is None:
        assert not hasattr(excinfo.value, 'data')
    else:
        expected_error_message = f'{expected_error_message} {DATA_MESSAGE}'
        assert excinfo.value.data == data

    assert excinfo.value.message == expected_error_message
