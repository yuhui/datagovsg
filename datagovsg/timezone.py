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

"""Standardise all datetime-related timezones to SGT (Singapore Time)."""

from datetime import datetime, timedelta, tzinfo
from pytz import timezone as pytimezone

def datetime_as_sgt(dt):
    """Set a datetime with the SGT timezone and return the datetime.

    Raises:
        AssertionError:
            Raised if `dt` is not of datetime class.
    """
    assert isinstance(dt, datetime)
    return dt.astimezone(pytimezone('Asia/Singapore'))

def datetime_from_string(val):
    """Convert a YYYY-MM-DDTHH:MM:SS string into a datetime
    and return the datetime.

    Raises:
        ValueError:
            Raised if `val` is not in a valid datetime format.
    """
    # first, try parsing without time
    dt_format = '%Y-%m-%d'
    try:
        dt = datetime.strptime(val, dt_format)
    except:
        # next, try parsing without timezone
        dt_format = '{} %H:%M:%S'.format(dt_format)
        try:
            dt = datetime.strptime(val, dt_format)
        except:
            # last, try parsing with timezone
            dt_format = '{}%z'.format(dt_format)
            dt = datetime.strptime(val, dt_format)
    # if still getting an error, then this isn't a datetime string

    dt = datetime_as_sgt(dt)

    if dt_format is '%Y-%m-%d':
        # the original string was just the date, so return a date object only
        dt = dt.date()

    return dt
