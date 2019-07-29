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

"""Test that the Client class is working properly."""

import pytest
from datetime import date, datetime

from datagovsg.client import __Client

# random values to populate in kwargs
SOME_STRING = 'lorem ipsum'
SOME_NUMBER = 42

BASE_KWARGS = {
    'some_string': SOME_STRING,
    'some_number': SOME_NUMBER,
}

# constants for testing datetime and date as datetime and date objects
GOOD_DATE_TIME = datetime(2019, 7, 13, 8, 32, 17)
GOOD_DATE = date(2019, 7, 13)

# constants for testing datetime and date as string objects
BAD_DATE_TIME = '2019-07-13 08:32:17'
BAD_DATE = '2019-07-13'

def key_in_dict(key, d):
    return key in d

def key_not_in_dict(key, d):
    return key not in d

@pytest.fixture(scope='module')
def client():
    return __Client()

def test_repr(client):
    assert repr(client) == str(client.__class__)

@pytest.mark.parametrize(
    ('date_time', 'dt', 'test_date_time_func', 'test_dt_func'),
    [
        (None, None, key_not_in_dict, key_not_in_dict),
        (GOOD_DATE_TIME, None, key_in_dict, key_not_in_dict),
        (None, GOOD_DATE, key_not_in_dict, key_in_dict),
        (GOOD_DATE_TIME, GOOD_DATE, key_in_dict, key_not_in_dict),
    ],
)
def test_prepare_kwargs_with_good_datetime_date(
    client,
    date_time, dt,
    test_date_time_func, test_dt_func,
):
    kwargs = __build_kwargs({'date_time': date_time, 'date': dt})
    new_kwargs = client.prepare_kwargs(kwargs)

    assert 'some_string' in new_kwargs
    assert new_kwargs['some_string'] is SOME_STRING
    assert 'some_number' in new_kwargs
    assert new_kwargs['some_number'] is SOME_NUMBER

    assert test_date_time_func('date_time', new_kwargs)
    assert test_dt_func('date', new_kwargs)

@pytest.mark.parametrize(
    ('date_time', 'dt'),
    [
        (BAD_DATE_TIME, None),
        (None, BAD_DATE),
        (BAD_DATE_TIME, BAD_DATE),
    ],
)
def test_prepare_kwargs_with_bad_datetime_date(client, date_time, dt):
    kwargs = __build_kwargs({'date_time': date_time, 'date': dt})
    with pytest.raises(AssertionError):
        _ = client.prepare_kwargs(kwargs)

# private

def __build_kwargs(test_kwargs):
    return dict(BASE_KWARGS, **test_kwargs)
