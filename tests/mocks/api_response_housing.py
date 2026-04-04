# Copyright 2026 Yuhui
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

# pylint: disable=line-too-long,missing-class-docstring,missing-function-docstring

"""Mock response for the Housing module."""

class APIResponseCarparkAvailability:
    status_code = 200

    @staticmethod
    def json():
        return {
            "items": [
                {
                    "timestamp": "2026-01-12T00:15:36+08:00",
                    "carpark_data": [
                        {
                            "carpark_info": [
                                {
                                    "total_lots": "105",
                                    "lot_type": "C",
                                    "lots_available": "31"
                                }
                            ],
                            "carpark_number": "HE12",
                            "update_datetime": "2026-01-12T00:14:30"
                        }
                    ]
                }
            ]
        }

__all__ = [
    'APIResponseCarparkAvailability',
]
