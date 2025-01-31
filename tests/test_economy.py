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

"""Test that the Economy class is working properly."""

from datetime import date

import pytest

from datagovsg import Economy

METHODS = [
    'designs',
    'patents',
    'trademarks',
]

LODGEMENT_DATE = date(2025, 1, 12)

@pytest.fixture(scope='module')
def client():
    return Economy()

@pytest.mark.parametrize(
    ('method'),
    METHODS,
)
def test_economy_method(client, method):
    data = getattr(client, method, None)()

    assert data is not None

@pytest.mark.parametrize(
    ('method'),
    METHODS,
)
def test_economy_method_with_lodgement_date(client, method):
    data = getattr(client, method, None)(lodgement_date=LODGEMENT_DATE)

    assert data is not None
