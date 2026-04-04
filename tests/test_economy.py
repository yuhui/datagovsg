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

"""Test that the Economy class is working properly."""

from os import getenv

import pytest
from dotenv import load_dotenv
from typeguard import check_type

from datagovsg import Economy
from datagovsg.economy.types import (
    DesignsDict,
    PatentsDict,
    TrademarksDict,
)

TEST_PARAMETERS = [
    ('designs', DesignsDict),
    ('patents', PatentsDict),
    ('trademarks', TrademarksDict),
]

"""
The API endpoint is poorly documented, so skip the tests for specific dates.
Anyway, it seems that the endpoint always returns 0 results, so maybe it's not
working properly in the first place. __shrug shoulders__

from datetime import date
LODGEMENT_DATE = date(2025, 1, 12)
"""

@pytest.fixture(scope='module')
def client():
    load_dotenv()
    api_key = getenv('DATAGOVSG_API_KEY')
    return Economy(api_key)

@pytest.mark.parametrize(
    ('method', 'expected_type'),
    TEST_PARAMETERS,
)
def test_economy_methods(client, method, expected_type):
    data = getattr(client, method, None)()

    assert check_type(data, expected_type) == data
