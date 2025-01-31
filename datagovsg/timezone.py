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

from datetime import date, datetime
from zoneinfo import ZoneInfo

from typeguard import typechecked

DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'

@typechecked
def datetime_as_sgt(dt: datetime) -> datetime:
    """Set a datetime with the SGT timezone and return the datetime.

    :param dt: Datetime to convert to SGT timezone.
    :type dt: datetime

    :return: The datetime in SGT timezone.
    :rtype: datetime
    """
    dt_sg: datetime = dt.astimezone(ZoneInfo('Asia/Singapore'))
    return dt_sg

@typechecked
def datetime_from_string(val: str) -> datetime | date:
    """Convert a YYYY-MM-DDTHH:MM:SS string into a datetime and return the \
    datetime.

    :param val: String to convert to a datetime.
    :type val: str

    :raises ValueError: "val" is not a recognised datetime string.

    :return: The value as a datetime or date, if there is no time.
    :rtype: datetime | date
    """
    dt: datetime | date

    # try parsing without time
    try:
        dt_format = DATE_FORMAT
        dt = datetime.strptime(val, dt_format)
    except ValueError:
        # try parsing without timezone
        try:
            dt_format = f'{DATE_FORMAT} {TIME_FORMAT}'
            dt = datetime.strptime(val, dt_format)
        except ValueError:
            # try parsing without timezone with "T"
            try:
                dt_format = f'{DATE_FORMAT}T{TIME_FORMAT}'
                dt = datetime.strptime(val, dt_format)
            except ValueError:
                # try parsing with timezone
                try:
                    dt_format = f'{DATE_FORMAT} {TIME_FORMAT}%z'
                    dt = datetime.strptime(val, dt_format)
                except ValueError:
                    # try parsing with timezone with "T"
                    try:
                        dt_format = f'{DATE_FORMAT}T{TIME_FORMAT}%z'
                        dt = datetime.strptime(val, dt_format)
                    except ValueError:
                        # try parsing without timezone with microseconds
                        try:
                            dt_format = f'{DATE_FORMAT} {TIME_FORMAT}.%f'
                            dt = datetime.strptime(val, dt_format)
                        except ValueError:
                            # try parsing without timezone with microseconds and "T"
                            try:
                                dt_format = f'{DATE_FORMAT}T{TIME_FORMAT}.%f'
                                dt = datetime.strptime(val, dt_format)
                            except ValueError:
                                # try parsing with timezone and microseconds
                                try:
                                    dt_format = f'{DATE_FORMAT} {TIME_FORMAT}.%f%z'
                                    dt = datetime.strptime(val, dt_format)
                                except ValueError:
                                    # try parsing with timezone and microseconds and "T"
                                    try:
                                        dt_format = f'{DATE_FORMAT}T{TIME_FORMAT}.%f%z'
                                        dt = datetime.strptime(val, dt_format)
                                    except ValueError as e:
                                        # still getting an error, this isn't a datetime string
                                        raise ValueError('val is not a datetime string') from e

    dt = datetime_as_sgt(dt)

    if dt_format == DATE_FORMAT:
        # the original string was just the date, so return a date object only
        dt = dt.date()

    return dt

__all__ = [
    'datetime_from_string',
]
