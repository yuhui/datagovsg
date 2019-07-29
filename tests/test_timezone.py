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

"""Test that the timezone functions are working properly."""

import pytest

from datetime import date, datetime
from pytz import timezone as pytimezone

from datagovsg import timezone

@pytest.mark.parametrize(
    ('date_time', 'expected_hour'),
    [
        (datetime(2019, 7, 1, 8), 8),
        (datetime(2019, 7, 1, 8, tzinfo=pytimezone('Asia/Singapore')), 8),
        (datetime(2019, 7, 1, 8, tzinfo=pytimezone('UTC')), 16),
    ],
)
def test_datetime_as_sgt(date_time, expected_hour):
    sgt_date_time = timezone.datetime_as_sgt(date_time)
    assert sgt_date_time.hour == expected_hour

@pytest.mark.parametrize(
    'date_time',
    ['2019-07-13 08:32:17', '2019-07-13 08:32:17+08:00'],
)
def test_datetime_as_sgt_from_bad_datetime(date_time):
    with pytest.raises(AssertionError):
        _ = timezone.datetime_as_sgt(date_time)

@pytest.mark.parametrize(
    ('date_time_str', 'expected_date_time'),
    [
        ('2019-07-13 08:32:17', datetime(2019, 7, 13, 8, 32, 17)),
        ('2019-07-13', date(2019, 7, 13)),
    ],
)
def test_datetime_from_string(date_time_str, expected_date_time):
    date_time = timezone.datetime_from_string(date_time_str)
    if isinstance(expected_date_time, datetime):
        expected_date_time = timezone.datetime_as_sgt(expected_date_time)
    assert date_time == expected_date_time

@pytest.mark.parametrize(
    'date_time_str',
    ['foobar', '2019-07-13 08:32', '2019-07 08:32:17', '2019-07'],
)
def test_datetime_from_bad_string(date_time_str):
    with pytest.raises(ValueError):
        _ = timezone.datetime_from_string(date_time_str)
