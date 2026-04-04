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

"""Mock response for the Transport module."""

class APIResponseTaxiAvailability:
    status_code = 200

    @staticmethod
    def json():
        return {
            "type": "FeatureCollection",
            "crs": {
                "type": "link",
                "properties": {
                    "href": "http://spatialreference.org/ref/epsg/4326/ogcwkt/",
                    "type": "ogcwkt"
                }
            },
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "MultiPoint",
                        "coordinates": [
                            [
                                103.63601,
                                1.27377
                            ]
                        ]
                    },
                    "properties": {
                        "timestamp": "2026-01-12T00:14:56+08:00",
                        "taxi_count": 1661,
                        "api_info": {
                            "status": "healthy"
                        }
                    }
                }
            ]
        }


class APIResponseTrafficImages:
    status_code = 200

    @staticmethod
    def json():
        return {
            "items": [
                {
                    "timestamp": "2026-01-12T00:14:51+08:00",
                    "cameras": [
                        {
                            "timestamp": "2026-01-12T00:11:11+08:00",
                            "image": "https://images.data.gov.sg/api/traffic-images/2026/01/4a9f79dd-5a29-4138-a470-50f1bd6460f6.jpg",
                            "location": {
                                "latitude": 1.345996,
                                "longitude": 103.69016
                            },
                            "camera_id": "6708",
                            "image_metadata": {
                                "height": 1080,
                                "width": 1920,
                                "md5": "e60a53248ed48106d3d1fe834c5bee2d"
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
    'APIResponseTaxiAvailability',
    'APIResponseTrafficImages',
]
