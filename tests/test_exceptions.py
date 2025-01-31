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

# pylint: disable=invalid-name,missing-function-docstring,redefined-outer-name,unused-argument

"""Test that the Exceptions are working properly."""

import pytest

from datagovsg.exceptions import APIError

@pytest.mark.parametrize(
    ('message', 'data', 'errors'),
    [
        ('pytest', None, None),
        ('pytest', {'Message': 'pytest message'}, None),
        ('pytest', None, {'error': 'pytest error'}),
        ('pytest', {'Message': 'pytest message'}, {'error': 'pytest error'}),
    ],
)
def test_raising_APIError(message, data, errors):
    with pytest.raises(APIError) as excinfo:
        raise APIError(message=message, data=data, errors=errors)

    assert excinfo.value.args[0] == message
    assert excinfo.value.message == message
    if data is None:
        assert not hasattr(excinfo.value, 'data')
    else:
        assert excinfo.value.data == data
    if errors is None:
        assert not hasattr(excinfo.value, 'errors')
    else:
        assert excinfo.value.errors == errors
