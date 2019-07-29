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

"""Mixin for Clients that interact with Data.gov.sg's APIs."""

from datetime import date, datetime

class __Client(object):
    """Client mixin for other API Clients."""

    def __repr__(self):
        return '{}'.format(self.__class__)

    def prepare_kwargs(self, kwargs):
        """Remove unnecessary arguments from kwargs and return that kwargs.

        Raises:
            AssertionError:
                Raised if date_time is specified but isn't a datetime object.
                Raised if date is specified but isn't a date object.
        """
        # remove keys with None values
        new_kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if 'date_time' in new_kwargs and 'date' in new_kwargs:
            # reject `date` in favour of `date_time`
            del new_kwargs['date']

        if 'date_time' in new_kwargs:
            assert isinstance(new_kwargs['date_time'], datetime)

        if 'date' in new_kwargs:
            assert isinstance(new_kwargs['date'], date)

        return new_kwargs
