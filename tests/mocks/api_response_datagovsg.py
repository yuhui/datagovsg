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

# pylint: disable=missing-class-docstring,missing-function-docstring

"""Mock responses for the DataGovSg module."""

class APIResponseDefault:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 1,
            "message": "..."
        }

class APIResponseBadRequest:
    status_code = 400

    @staticmethod
    def json():
        return {
            "code": 4,
            "name": "ERROR_PARAMS",
            "data": None,
            "errorMsg": "Invalid date format. Date format must be YYYY-MM-DD (2024-06-01) or YYYY-MM-DDTHH:mm:ss (2024-06-01T08:30:00)."
        }

class APIResponseNotFound:
    status_code = 404

    @staticmethod
    def json():
        return {
            "code": 17,
            "name": "REAL_TIME_API_DATA_NOT_FOUND",
            "data": None,
            "errorMsg": "Data not found"
        }

class APIResponseRateLimitExceeded:
    status_code = 429

    @staticmethod
    def json():
        return {
            "code": 24,
            "name": "TOO_MANY_REQUESTS",
            "data": None,
            "errorMsg": "Rate limit exceeded"
        }

class APIResponseTrafficImages:
    status_code = 200

    @staticmethod
    def json():
        return {
            "items": [
                {
                    "timestamp": "2026-01-04T23:26:01+08:00",
                    "cameras": [
                        {
                            "timestamp": "2026-01-04T23:21:21+08:00",
                            "image": "https://images.data.gov.sg/api/traffic-images/2026/01/95c4cfdb-27f8-4f54-812c-cb028311920e.jpg",
                            "location": {
                                "latitude": 1.323604823,
                                "longitude": 103.8587802
                            },
                            "camera_id": "1701",
                            "image_metadata": {
                                "height": 1080,
                                "width": 1920,
                                "md5": "c6d51dcbb72f6fed25ffa6391a594ac8"
                            }
                        }
                    ]
                }
            ],
            "api_info": {
                "status": "healthy"
            }
        }

__all__ = [
    'APIResponseDefault',
    'APIResponseBadRequest',
    'APIResponseNotFound',
    'APIResponseRateLimitExceeded',
    'APIResponseTrafficImages',
]
