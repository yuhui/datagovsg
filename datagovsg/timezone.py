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

"""Standardise all datetime-related timezones to SGT (Singapore Time)."""

from datetime import date, datetime, time
from re import fullmatch, match
from zoneinfo import ZoneInfo

from typeguard import typechecked

ALLOWED_DATE_FORMATS = (
    '%Y-%m-%dT%H:%M:%S.%f%z',
    '%Y-%m-%dT%H:%M:%S%z',
    '%Y-%m-%dT%H:%M:%S.%f',
    '%Y-%m-%dT%H:%M:%S',
    '%Y%m%dT%H:%M:%S.%f%z',
    '%Y%m%dT%H:%M:%S%z',
    '%Y%m%dT%H:%M:%S.%f',
    '%Y%m%dT%H:%M:%S',
    '%Y-%m-%d %H:%M:%S.%f%z',
    '%Y-%m-%d %H:%M:%S%z',
    '%Y-%m-%d %H:%M:%S.%f',
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d',
    '%Y%m%d',
    '%d/%m/%Y',
    '%H:%M:%S.%f%z',
    '%H:%M:%S%z',
    '%H:%M:%S.%f',
    '%H:%M%z',
    '%H:%M',
    '%H%M',
)

@typechecked
def datetime_as_sgt(dt: datetime) -> datetime:
    """Update a datetime to use the SGT timezone and return the datetime.

    :param dt: Datetime to update to use SGT timezone.
    :type dt: datetime

    :return: The datetime in SGT timezone.
    :rtype: datetime
    """
    dt_sg: datetime = dt.replace(tzinfo=ZoneInfo('Asia/Singapore'))
    return dt_sg

@typechecked
def datetime_from_string(val: str) -> datetime | date | time:
    """Convert a string into a datetime in SGT timezone.

    Strings are parsed according to the following formats, in order:
    1. %Y-%m-%dT%H:%M:%S.%f%z
    2. %Y-%m-%dT%H:%M:%S%z
    3. %Y-%m-%dT%H:%M:%S.%f
    4. %Y-%m-%dT%H:%M:%S
    5. %Y%m%dT%H:%M:%S.%f%z
    6. %Y%m%dT%H:%M:%S%z
    7. %Y%m%dT%H:%M:%S.%f
    8. %Y%m%dT%H:%M:%S
    9. %Y-%m-%d %H:%M:%S.%f%z
    10. %Y-%m-%d %H:%M:%S%z
    11. %Y-%m-%d %H:%M:%S.%f
    12. %Y-%m-%d %H:%M:%S
    13. %Y-%m-%d
    14. %Y%m%d
    15. %d/%m/%Y
    16. %H:%M:%S.%f%z
    17. %H:%M:%S%z
    18. %H:%M:%S.%f
    19. %H:%M%z
    20. %H:%M
    21. %H%M

    :param val: String to convert to a datetime.
    :type val: str

    :raises ValueError: `val` is not a recognised datetime string.

    :return: The value as a datetime or date, if there is no time, or time, if \
        there is no date.
    :rtype: datetime | date | time
    """
    dt: datetime | date | time

    dt_datetime = None
    dt_format = ''
    for date_format in ALLOWED_DATE_FORMATS:
        try:
            if date_format == '%H%M' and len(val) != 4:
                raise ValueError('val is not a 4-digit time')
            if date_format == '%H:%M' and len(val) != 5:
                raise ValueError('val is not a 5-digit time')

            dt_datetime = datetime.strptime(val, date_format)
            dt_format = date_format
        except ValueError:
            continue

    if dt_datetime is None:
        raise ValueError('val is not a recognised datetime string')

    dt_datetime_sgt = datetime_as_sgt(dt_datetime)
    dt_date_sgt = dt_datetime_sgt.date()
    dt_time_sgt = dt_datetime_sgt.time()

    if match('%H:?%M', dt_format) is not None:
        dt = dt_time_sgt
    elif fullmatch('%Y-?%m-?%d', dt_format) is not None:
        dt = dt_date_sgt
    elif fullmatch('%d/%m/%Y', dt_format) is not None:
        dt = dt_date_sgt
    else:
        dt = dt_datetime_sgt

    return dt

@typechecked
def datetime_to_string(dt: datetime | date) -> str:
    """Convert a datetime to string.

    :param dt: Datetime to convert to string.
    :type dt: datetime or date

    :return: The datetime as a string in ISO format.
    :rtype: str
    """
    # IMPORTANT! Test for `datetime` before `date`!
    val: str = dt.strftime('%Y-%m-%dT%H:%M:%S') if isinstance(dt, datetime) \
        else dt.strftime('%Y-%m-%d')
    return val

@typechecked
def is_datetime_between_range(
    dt: datetime,
    min_dt: datetime,
    max_dt: datetime | None=None,
) -> bool:
    """Check if a datetime is between the first and last datetimes (inclusive).

    :param dt: Datetime to check.
    :type dt: datetime

    :param min_dt: Earliest possible datetime.
    :type dt: datetime

    :param max_dt: Latest possible datetime. If None, then defaults to now.
    :type dt: datetime or None

    :raises ValueError: ``min_dt`` is after ``max_dt``.

    :return: ``True`` if the datetime is between the first and last datetimes.
    :rtype: bool
    """
    result: bool

    if max_dt is None:
        max_dt = datetime.now()

    if datetime_as_sgt(min_dt) > datetime_as_sgt(max_dt):
        raise ValueError('min_dt is after max_dt')

    result = datetime_as_sgt(min_dt) <= datetime_as_sgt(dt) <= \
        datetime_as_sgt(max_dt)

    return result

__all__ = [
    'datetime_as_sgt',
    'datetime_from_string',
    'datetime_to_string',
    'is_datetime_between_range',
]
