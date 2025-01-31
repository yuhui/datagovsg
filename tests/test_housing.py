# Copyright 2025 Yuhui
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

"""Test that the Housing class is working properly."""

from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

import pytest

from datagovsg import Housing

TEST_DATE = date.today() - timedelta(1)
TEST_DATETIME = datetime.combine(
    TEST_DATE,
    time(23, 45, 16, tzinfo=ZoneInfo('Asia/Singapore'))
)

@pytest.fixture
def client():
    return Housing()

def test_carpark_availability(client):
    carpark_availability = client.carpark_availability()

    assert carpark_availability is not None

def test_carpark_availability_with_datetime(client):
    carpark_availability = client.carpark_availability(date_time=TEST_DATETIME)

    timestamp = carpark_availability['items'][0]['timestamp']
    timestamp_difference = (TEST_DATETIME - timestamp) \
        if TEST_DATETIME > timestamp \
        else (timestamp - TEST_DATETIME)

    # Allow 5-minute difference
    assert timestamp_difference.seconds <= (60 * 5)
