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

"""Test that the Ckan class is working properly."""

import pytest
from requests.exceptions import HTTPError

from datagovsg import Ckan

# constants for testing datastore_search() and resource_show()
BAD_RESOURCE_ID = 'abc-123'
GOOD_RESOURCE_ID = 'f9dbfc75-a2dc-42af-9f50-425e4107ae84'

# constants for testing package_show()
BAD_PACKAGE_ID = 'abc-123'
GOOD_PACKAGE_ID = 'd1778088-f56a-4353-891f-21f803b2dad5'

@pytest.fixture(scope='module')
def client():
    return Ckan()

@pytest.mark.parametrize(
    ('records_format', 'expected_record_class'),
    [
        (None, dict),
        ('objects', dict),
        ('lists', list),
        ('csv', str),
        ('tsv', str),
    ],
)
def test_datasource_search(client, records_format, expected_record_class):
    resource = client.datastore_search(
        resource_id=GOOD_RESOURCE_ID,
        records_format=records_format,
    )

    assert isinstance(resource, dict)

    assert 'result' in resource
    result = resource['result']

    assert 'resource_id' in result
    assert result['resource_id'] == GOOD_RESOURCE_ID

    assert 'fields' in result
    assert isinstance(result['fields'], list)

    assert 'records' in result
    assert isinstance(result['records'], list)

    fields = result['fields']
    records = result['records']
    for record in records:
        assert isinstance(record, expected_record_class)
        if records_format in (None, 'objects', 'lists'):
            assert len(record) == len(fields)
        elif records_format in ('csv', 'tsv'):
            splitter = ',' if records_format is 'csv' else '\t'
            split_record = record.split(splitter)
            assert len(split_record) == len(fields)

    # the final result should have *all* records in the resource
    # instead of paginated records.
    # so verify that the total number of records matches the total
    # reported in the API response.

    assert 'total' in result
    total = result['total']
    assert total == len(result['records'])

def test_datasource_search_with_bad_resource_id(client):
    with pytest.raises(HTTPError):
        _ = client.datastore_search(resource_id=BAD_RESOURCE_ID)

def test_package_list(client):
    packages = client.package_list()

    assert isinstance(packages, dict)

    assert 'result' in packages
    assert isinstance(packages['result'], list)

def test_package_show(client):
    package = client.package_show(package_id=GOOD_PACKAGE_ID)

    assert isinstance(package, dict)

    assert 'result' in package
    result = package['result']

    assert 'id' in result
    assert result['id'] == GOOD_PACKAGE_ID

    assert 'resources' in result
    resources = result['resources']

    assert 'num_resources' in result
    num_resources = result['num_resources']
    assert num_resources == len(resources)

    for resource in resources:
        assert 'package_id' in resource
        assert resource['package_id'] == GOOD_PACKAGE_ID

        assert 'fields' in resource
        assert isinstance(resource['fields'], list)

def test_package_show_with_bad_package_id(client):
    with pytest.raises(HTTPError):
        _ = client.package_show(package_id=BAD_PACKAGE_ID)

def test_resource_show(client):
    resource = client.resource_show(resource_id=GOOD_RESOURCE_ID)

    assert isinstance(resource, dict)

    assert 'result' in resource
    assert isinstance(resource['result'], dict)
    result = resource['result']

    assert 'id' in result
    assert result['id'] == GOOD_RESOURCE_ID

    assert 'fields' in result
    assert isinstance(result['fields'], list)

def test_resource_show_with_bad_resource_id(client):
    with pytest.raises(HTTPError):
        _ = client.resource_show(resource_id=BAD_RESOURCE_ID)
