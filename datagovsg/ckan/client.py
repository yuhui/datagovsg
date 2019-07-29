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

"""Client for interacting with the CKAN APIs."""

from cachetools import cached, TTLCache

from datagovsg import net
from datagovsg.ckan.constants import *
from datagovsg.client import __Client

class Client(__Client):
    """Interact with CKAN software to access its catalogue of datasets."""

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def datastore_search(
        self,
        resource_id,
        limit=100,
        offset=0,
        fields=None,
        filters=None,
        q=None,
        sort=None,
        records_format='objects',
    ):
        """Search data in a resource.

        Arguments:
            resource_id (str):
                ID or alias of the resource to be searched against.
            limit (int):
                (optional) Maximum number of rows to return.
                Default: 100.
            offset (int):
                (optional) Offset this number of rows.
                Default: 0.
            fields (str):
                (optional) Fields to return.
            filters (dict):
                (optional) Dictionary of matching conditions,
                e.g {"key1": "a", "key2": "b"}.
            q (str or dict):
                (optional) Full text query.
                If it's a string, it'll search on all fields on each row.
                If it's a dictionary as {"key1": "a", "key2": "b"},
                it’ll search on each specific field.
            sort (str):
                (optional) Comma-separated field names with ordering,
                e.g. "fieldname1, fieldname2 desc".
            records_format (str):
                (optional) The format for the records return value.
                "objects": list of {fieldname1: value1, ...} dicts
                "lists": list of [value1, value2, ...] lists
                "csv": comma-separated values with no header
                "tsv": tab-separated values with no header
                Default: "objects".

        Returns:
            (dict) Resources that match the search criteria.
            All of the records are concatenated together, so there is no need
            for further pagination.

        References:
            https://data.gov.sg/dataset/ckan-datastore-search
        """
        data = self.__paginate_search_datastore(
            DATASOURCE_SEARCH_CKAN_ENDPOINT,
            resource_id=resource_id,
            limit=limit,
            offset=offset,
            fields=fields,
            filters=filters,
            q=q,
            sort=sort,
        )

        # `records_format` is borked in the API
        # so create it as per the specification

        # create a list of record values since that is the base format
        # for "lists", "csv" and "tsv".
        # (for "objects", just return the records as-is.)
        records_list = [
            list(record.values()) for record in data['result']['records']
        ]
        if records_format is 'lists':
            data['result']['records'] = records_list
        elif records_format is 'csv':
            data['result']['records'] = [
                ','.join(str(v) for v in record) for record in records_list
            ]
        elif records_format is 'tsv':
            data['result']['records'] = [
                '\t'.join(str(v) for v in record) for record in records_list
            ]

        return data

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def package_list(self, limit=None, offset=None):
        """Return a list of datasets on data.gov.sg.

        Arguments:
            limit (int):
                (optional) Maximum number of packages to return per page.
                Default: None, i.e. return all packages.
            offset (int):
                (optional) Offset this number of packages.

        Returns:
            (dict) Metadata and list of packages.

        References:
            https://data.gov.sg/dataset/ckan-package-list
        """
        package_list = net.send_request(
            PACKAGE_LIST_CKAN_ENDPOINT,
            limit=limit,
            offset=offset,
        )

        return package_list

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def package_show(self, package_id):
        """Return the metadata of a dataset (package) and its resources.

        Arguments:
            package_id (str):
                ID or name of the dataset.

        Returns:
            (dict) Metadata and resources of the requested package.

        References:
            https://data.gov.sg/dataset/ckan-package-show
        """
        package = net.send_request(
            PACKAGE_SHOW_CKAN_ENDPOINT,
            id=package_id,
        )

        return package

    @cached(cache=TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_ONE_DAY))
    def resource_show(self, resource_id):
        """Return the metadata of a resource.

        Arguments:
            resource_id (str):
                ID of the resource.

        Returns:
            (dict) Metadata of the requested resource.

        References:
            https://data.gov.sg/dataset/ckan-resource-show
        """
        resource = net.send_request(
            RESOURCE_SHOW_CKAN_ENDPOINT,
            id=resource_id,
        )

        return resource

    # private

    def __paginate_search_datastore(self, url, **kwargs):
        """Search one page of data in a resource.
        This function calls itself recursively to get all records.
        In the recursion, only `url` is specified since it contains all of the
        necessary parameters.

        Arguments:
            url (str):
                Datastore Search URL.
            kwargs (dict):
                Arguments that are set in the calling function.
                See search_datastore().

        Returns:
            (dict) One page of resources that match the search criteria.
            The records are concatenated with the previous called page's,
            then returned altogether.
        """
        page_data = net.send_request(url, **kwargs)

        # it is possible to paginate "forever" by following result._links.next
        # so check if there are any records in the current page first
        if len(page_data['result']['records']) > 0:
            # get the next page of results
            next_link = page_data['result']['_links']['next']
            next_url = BASE_CKAN_DOMAIN + next_link
            next_page_data = self.__paginate_search_datastore(next_url)
            page_data['result']['records'] += \
                next_page_data['result']['records']

        return page_data
