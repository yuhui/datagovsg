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

"""Test that the Transport class is working properly."""

import pytest
from requests.exceptions import HTTPError

from datagovsg import Transport

@pytest.fixture
def client():
    return Transport()

def test_carpark_availability(client):
    carpark_availability = client.carpark_availability()

    assert isinstance(carpark_availability, dict)

def test_taxi_availability(client):
    taxi_availability = client.taxi_availability()

    assert isinstance(taxi_availability, dict)

def test_traffic_images(client):
    traffic_images = client.traffic_images()

    assert isinstance(traffic_images, dict)
