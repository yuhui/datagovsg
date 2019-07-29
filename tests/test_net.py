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

"""Test that the net functions are working properly."""

import pytest
from datetime import date, datetime

from datagovsg import net

@pytest.mark.parametrize(
    ('url', 'accept_type', 'kwargs'),
    [
        (
            'https://api.data.gov.sg/v1/environment/psi',
            'json',
            {},
        ),
        (
            'https://api.data.gov.sg/v1/environment/psi?date_time=2019-07-13T08%3A13%3A27',
            'json',
            {},
        ),
        (
            'https://api.data.gov.sg/v1/environment/psi',
            'json',
            {'date': date(2019, 7, 13)},
        ),
        (
            'https://api.data.gov.sg/v1/transport/taxi-availability',
            'vnd.geo+json',
            {},
        ),
        (
            'https://api.data.gov.sg/v1/transport/taxi-availability',
            'vnd.geo+json',
            {'date_time': datetime(2019, 7, 13, 8, 32, 17)},
        ),
    ],
)
def test_send_request(url, accept_type, kwargs):
    response_content = net.send_request(url, accept_type, **kwargs)
    assert isinstance(response_content, dict)

def test_send_request_with_bad_accept_type():
    with pytest.raises(ValueError):
        _ = net.send_request(
        'https://api.data.gov.sg/v1/transport/taxi-availability',
        'csv',
    )
