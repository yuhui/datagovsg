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

"""Test that the Ckan class is working properly."""

from warnings import catch_warnings, simplefilter

import pytest

from datagovsg import Ckan

@pytest.fixture(scope='module')
def client():
    return Ckan()

def test_datasource_search(client):
    with catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        simplefilter('always')

        resource = client.datastore_search()

        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert 'CKAN has been removed from Data.gov.sg.' in str(w[-1].message)

        assert resource is None

def test_package_list(client):
    with catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        simplefilter('always')

        packages = client.package_list()

        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert 'CKAN has been removed from Data.gov.sg.' in str(w[-1].message)

        assert packages is None

def test_package_show(client):
    with catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        simplefilter('always')

        package = client.package_show()

        assert len(w) == 1

        assert issubclass(w[-1].category, DeprecationWarning)
        assert 'CKAN has been removed from Data.gov.sg.' in str(w[-1].message)

        assert package is None

def test_resource_show(client):
    with catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        simplefilter('always')

        resource = client.resource_show()

        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert 'CKAN has been removed from Data.gov.sg.' in str(w[-1].message)

        assert resource is None
