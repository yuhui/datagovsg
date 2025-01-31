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

from warnings import warn

class Client:
    """REMOVED BY DATA.GOV.SG.

    This API has been removed from Data.gov.sg. As a result, all of the \
        methods in this class return ``None``.

    This class will be removed from this package's next major release or \
        31 December 2025, whichever comes earlier.

    :warns DeprecationWarning: Inform the developer that this method has
        been deprecated.

    Formerly: Interact with CKAN software to access its catalogue of datasets.
    """

    def __init__(self) -> None:
        """Constructor method"""
        warn('CKAN has been removed from Data.gov.sg.', DeprecationWarning)

    def datastore_search(self) -> None:
        """Search data in a resource.

        :warns DeprecationWarning: Inform the developer that this method has \
            been deprecated.

        :return: ``None``.
        :rtype: None
        """
        warn('CKAN has been removed from Data.gov.sg.', DeprecationWarning)

        data = None

        return data

    def package_list(self) -> None:
        """Return a list of datasets on data.gov.sg.

        :warns DeprecationWarning: Inform the developer that this method has \
            been deprecated.

        :return: ``None``.
        :rtype: None
        """
        warn('CKAN has been removed from Data.gov.sg.', DeprecationWarning)

        package_list = None

        return package_list

    def package_show(self) -> None:
        """Return the metadata of a dataset (package) and its resources.

        :warns DeprecationWarning: Inform the developer that this method has \
            been deprecated.

        :return: ``None``.
        :rtype: None
        """
        warn('CKAN has been removed from Data.gov.sg.', DeprecationWarning)

        package = None

        return package

    def resource_show(self) -> None:
        """Return the metadata of a resource.

        :warns DeprecationWarning: Inform the developer that this method has \
            been deprecated.

        :return: ``None``.
        :rtype: None
        """
        warn('CKAN has been removed from Data.gov.sg.', DeprecationWarning)

        resource = None

        return resource

