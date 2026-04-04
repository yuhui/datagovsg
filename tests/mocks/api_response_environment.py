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

"""Mock response for the Environment module."""

class APIResponseAirTemperature:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S109",
                        "deviceId": "S109",
                        "name": "Ang Mo Kio Avenue 5",
                        "location": {
                            "latitude": 1.3764,
                            "longitude": 103.8492
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T10:15:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 26.4
                            }
                        ]
                    }
                ],
                "readingType": "DBT 1M F",
                "readingUnit": "deg C"
            },
            "errorMsg": ""
        }

class APIResponseAirTemperaturePage1:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S109",
                        "deviceId": "S109",
                        "name": "Ang Mo Kio Avenue 5",
                        "location": {
                            "latitude": 1.3764,
                            "longitude": 103.8492
                        }
                    },
                    {
                        "id": "S106",
                        "deviceId": "S106",
                        "name": "Pulau Ubin",
                        "location": {
                            "latitude": 1.4168,
                            "longitude": 103.9673
                        }
                    },
                    {
                        "id": "S117",
                        "deviceId": "S117",
                        "name": "Banyan Road",
                        "location": {
                            "latitude": 1.256,
                            "longitude": 103.679
                        }
                    },
                    {
                        "id": "S104",
                        "deviceId": "S104",
                        "name": "Woodlands Avenue 9",
                        "location": {
                            "latitude": 1.44387,
                            "longitude": 103.78538
                        }
                    },
                    {
                        "id": "S115",
                        "deviceId": "S115",
                        "name": "Tuas South Avenue 3",
                        "location": {
                            "latitude": 1.29377,
                            "longitude": 103.61843
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T23:59:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 25.2
                            },
                            {
                                "stationId": "S106",
                                "value": 25.1
                            },
                            {
                                "stationId": "S117",
                                "value": 26.2
                            },
                            {
                                "stationId": "S104",
                                "value": 24.9
                            },
                            {
                                "stationId": "S115",
                                "value": 25.9
                            }
                        ]
                    },
                    {
                        "timestamp": "2026-01-12T23:58:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 25.2
                            },
                            {
                                "stationId": "S106",
                                "value": 25.1
                            },
                            {
                                "stationId": "S117",
                                "value": 26.2
                            },
                            {
                                "stationId": "S104",
                                "value": 24.9
                            },
                            {
                                "stationId": "S115",
                                "value": 25.9
                            }
                        ]
                    },
                    {
                        "timestamp": "2026-01-12T23:57:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 25.2
                            },
                            {
                                "stationId": "S106",
                                "value": 25.1
                            },
                            {
                                "stationId": "S117",
                                "value": 26.1
                            },
                            {
                                "stationId": "S104",
                                "value": 24.9
                            },
                            {
                                "stationId": "S115",
                                "value": 25.9
                            }
                        ]
                    }
                ],
                "readingType": "DBT 1M F",
                "readingUnit": "deg C",
                "paginationToken": "b2Zmc2V0PTI1"
            },
            "errorMsg": ""
        }

class APIResponseAirTemperaturePage2:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S117",
                        "deviceId": "S117",
                        "name": "Banyan Road",
                        "location": {
                            "latitude": 1.256,
                            "longitude": 103.679
                        }
                    },
                    {
                        "id": "S102",
                        "deviceId": "S102",
                        "name": "Semakau Landfill",
                        "location": {
                            "latitude": 1.189,
                            "longitude": 103.768
                        }
                    },
                    {
                        "id": "S60",
                        "deviceId": "S60",
                        "name": "Sentosa",
                        "location": {
                            "latitude": 1.25,
                            "longitude": 103.8279
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T23:34:00+08:00",
                        "data": [
                            {
                                "stationId": "S117",
                                "value": 26.2
                            },
                            {
                                "stationId": "S102",
                                "value": 26.3
                            },
                            {
                                "stationId": "S60",
                                "value": 26.1
                            }
                        ]
                    },
                    {
                        "timestamp": "2026-01-12T23:33:00+08:00",
                        "data": [
                            {
                                "stationId": "S117",
                                "value": 26.2
                            },
                            {
                                "stationId": "S102",
                                "value": 26.3
                            },
                            {
                                "stationId": "S60",
                                "value": 26.1
                            }
                        ]
                    },
                    {
                        "timestamp": "2026-01-12T23:32:00+08:00",
                        "data": [
                            {
                                "stationId": "S117",
                                "value": 26.2
                            },
                            {
                                "stationId": "S102",
                                "value": 26.3
                            },
                            {
                                "stationId": "S60",
                                "value": 26.1
                            }
                        ]
                    },
                    {
                        "timestamp": "2026-01-12T23:31:00+08:00",
                        "data": [
                            {
                                "stationId": "S117",
                                "value": 26.2
                            },
                            {
                                "stationId": "S102",
                                "value": 26.4
                            },
                            {
                                "stationId": "S60",
                                "value": 26.2
                            }
                        ]
                    }
                ],
                "readingType": "DBT 1M F",
                "readingUnit": "deg C",
                "paginationToken": "b2Zmc2V0PTUw"
            },
            "errorMsg": ""
        }

class APIResponseAirTemperaturePage3:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S109",
                        "deviceId": "S109",
                        "name": "Ang Mo Kio Avenue 5",
                        "location": {
                            "latitude": 1.3764,
                            "longitude": 103.8492
                        }
                    },
                    {
                        "id": "S102",
                        "deviceId": "S102",
                        "name": "Semakau Landfill",
                        "location": {
                            "latitude": 1.189,
                            "longitude": 103.768
                        }
                    },
                    {
                        "id": "S50",
                        "deviceId": "S50",
                        "name": "Clementi Road",
                        "location": {
                            "latitude": 1.3337,
                            "longitude": 103.7768
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T23:09:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 25.3
                            },
                            {
                                "stationId": "S102",
                                "value": 26.4
                            },
                            {
                                "stationId": "S50",
                                "value": 25.3
                            }
                        ]
                    },
                    {
                        "timestamp": "2026-01-12T23:08:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 25.3
                            },
                            {
                                "stationId": "S102",
                                "value": 26.5
                            },
                            {
                                "stationId": "S50",
                                "value": 25.3
                            }
                        ]
                    }
                ],
                "readingType": "DBT 1M F",
                "readingUnit": "deg C"
            },
            "errorMsg": ""
        }

class APIResponseFloodAlerts:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "datetime": "2026-01-12T10:14:21+08:00",
                        "item": {
                            "type": "observation",
                            "identifier": "2.49.0.0.702.2-BCM-17586121561884-DYOONG",
                            "isStationData": False,
                            "msgType": "Alert",
                            "references": "pub_joint_ops_ctr@pub.gov.sg, 2.49.0.0.702.2-BCM-17586117885024-DYOONG, 2025-09-23T15:16:28+08:00",
                            "sender": "pub_joint_ops_ctr@pub.gov.sg",
                            "scope": "Public",
                            "status": "Actual",
                            "readings": [
                                {
                                    "area": {
                                        "areaDesc": "at <street name1> from <street name2> to <street name3>",
                                        "circle": [
                                            1.33201,
                                            103.87015,
                                            1
                                        ]
                                    },
                                    "category": "Met",
                                    "certainty": "Observed",
                                    "description": "Flash flood at Bt Timah Rd from Wilby Rd to Blackmore Dr. Please avoid the area. Issued 1705 hrs.",
                                    "event": "Flood",
                                    "eventCode": {
                                        "value": "OET-081",
                                        "valueName": "OET:v1.2"
                                    },
                                    "headline": "Flash Flood Alert",
                                    "instruction": "Please avoid this area for the next one (1) hour.",
                                    "responseType": "Avoid",
                                    "senderName": "PUB",
                                    "severity": "Minor",
                                    "urgency": "Immediate"
                                }
                            ]
                        },
                        "updatedTimestamp": "2026-01-12T10:16:42+08:00"
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseLightning:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "datetime": "2026-01-12T10:14:00+08:00",
                        "item": {
                            "type": "observation",
                            "isStationData": False,
                            "readings": [
                                {
                                    "location": {
                                        "latitude": "1.1700",
                                        "longitude": "103.8718"
                                    },
                                    "datetime": "2026-01-12T10:15:44.004+08:00",
                                    "text": "Cloud to Cloud",
                                    "type": "C"
                                }
                            ]
                        },
                        "updatedTimestamp": "2026-01-12T10:16:02+08:00"
                    }
                ]
            },
            "errorMsg": None
        }

class APIResponsePM25:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "regionMetadata": [
                    {
                        "name": "west",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.7
                        }
                    },
                    {
                        "name": "east",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.94
                        }
                    },
                    {
                        "name": "central",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "south",
                        "labelLocation": {
                            "latitude": 1.29587,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "north",
                        "labelLocation": {
                            "latitude": 1.41803,
                            "longitude": 103.82
                        }
                    }
                ],
                "items": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T10:46:06+08:00",
                        "timestamp": "2026-01-12T10:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 13,
                                "east": 15,
                                "central": 19,
                                "south": 8,
                                "north": 12
                            }
                        }
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponsePM25Page1:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "regionMetadata": [
                    {
                        "name": "west",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.7
                        }
                    },
                    {
                        "name": "east",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.94
                        }
                    },
                    {
                        "name": "central",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "south",
                        "labelLocation": {
                            "latitude": 1.29587,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "north",
                        "labelLocation": {
                            "latitude": 1.41803,
                            "longitude": 103.82
                        }
                    }
                ],
                "items": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T23:45:31+08:00",
                        "timestamp": "2026-01-12T23:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 14,
                                "east": 14,
                                "central": 12,
                                "south": 8,
                                "north": 3
                            }
                        }
                    },
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T22:45:38+08:00",
                        "timestamp": "2026-01-12T22:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 14,
                                "east": 13,
                                "central": 11,
                                "south": 8,
                                "north": 11
                            }
                        }
                    }
                ],
                "paginationToken": "b2Zmc2V0PTI1"
            },
            "errorMsg": ""
        }

class APIResponsePM25Page2:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "regionMetadata": [
                    {
                        "name": "west",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.7
                        }
                    },
                    {
                        "name": "east",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.94
                        }
                    },
                    {
                        "name": "central",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "south",
                        "labelLocation": {
                            "latitude": 1.29587,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "north",
                        "labelLocation": {
                            "latitude": 1.41803,
                            "longitude": 103.82
                        }
                    }
                ],
                "items": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T22:00:51+08:00",
                        "timestamp": "2026-01-12T21:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 15,
                                "east": 12,
                                "central": 10,
                                "south": 9,
                                "north": 9
                            }
                        }
                    }
                ],
                "paginationToken": "b2Zmc2V0PTUw"
            },
            "errorMsg": ""
        }

class APIResponsePM25Page3:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "regionMetadata": [
                    {
                        "name": "west",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.7
                        }
                    },
                    {
                        "name": "east",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.94
                        }
                    },
                    {
                        "name": "central",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "south",
                        "labelLocation": {
                            "latitude": 1.29587,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "north",
                        "labelLocation": {
                            "latitude": 1.41803,
                            "longitude": 103.82
                        }
                    }
                ],
                "items": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T21:00:50+08:00",
                        "timestamp": "2026-01-12T20:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 10,
                                "east": 12,
                                "central": 15,
                                "south": 9,
                                "north": 10
                            }
                        }
                    },
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T19:46:06+08:00",
                        "timestamp": "2026-01-12T19:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 10,
                                "east": 12,
                                "central": 20,
                                "south": 7,
                                "north": 11
                            }
                        }
                    },
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T19:00:48+08:00",
                        "timestamp": "2026-01-12T18:00:00+08:00",
                        "readings": {
                            "pm25_one_hourly": {
                                "west": 14,
                                "east": 12,
                                "central": 22,
                                "south": 9,
                                "north": 12
                            }
                        }
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponsePSI:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "regionMetadata": [
                    {
                        "name": "west",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.7
                        }
                    },
                    {
                        "name": "east",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.94
                        }
                    },
                    {
                        "name": "central",
                        "labelLocation": {
                            "latitude": 1.35735,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "south",
                        "labelLocation": {
                            "latitude": 1.29587,
                            "longitude": 103.82
                        }
                    },
                    {
                        "name": "north",
                        "labelLocation": {
                            "latitude": 1.41803,
                            "longitude": 103.82
                        }
                    }
                ],
                "items": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T10:46:07+08:00",
                        "timestamp": "2026-01-12T10:00:00+08:00",
                        "readings": {
                            "o3_sub_index": {
                                "west": 12,
                                "east": 16,
                                "central": 19,
                                "south": 10,
                                "north": 14
                            },
                            "no2_one_hour_max": {
                                "west": 44,
                                "east": 24,
                                "central": 19,
                                "south": 32,
                                "north": 21
                            },
                            "o3_eight_hour_max": {
                                "west": 29,
                                "east": 38,
                                "central": 45,
                                "south": 25,
                                "north": 33
                            },
                            "psi_twenty_four_hourly": {
                                "west": 52,
                                "east": 48,
                                "central": 55,
                                "south": 51,
                                "north": 51
                            },
                            "pm10_twenty_four_hourly": {
                                "west": 26,
                                "east": 34,
                                "central": 32,
                                "south": 27,
                                "north": 22
                            },
                            "pm10_sub_index": {
                                "west": 26,
                                "east": 34,
                                "central": 32,
                                "south": 27,
                                "north": 22
                            },
                            "pm25_twenty_four_hourly": {
                                "west": 13,
                                "east": 11,
                                "central": 16,
                                "south": 12,
                                "north": 12
                            },
                            "so2_sub_index": {
                                "west": 3,
                                "east": 2,
                                "central": 3,
                                "south": 1,
                                "north": 3
                            },
                            "pm25_sub_index": {
                                "west": 52,
                                "east": 48,
                                "central": 55,
                                "south": 51,
                                "north": 51
                            },
                            "so2_twenty_four_hourly": {
                                "west": 5,
                                "east": 3,
                                "central": 5,
                                "south": 2,
                                "north": 5
                            },
                            "co_eight_hour_max": {
                                "west": 1,
                                "east": 0,
                                "central": 1,
                                "south": 0,
                                "north": 1
                            },
                            "co_sub_index": {
                                "west": 5,
                                "east": 4,
                                "central": 6,
                                "south": 4,
                                "north": 5
                            }
                        }
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseRainfall:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S218",
                        "deviceId": "S218",
                        "name": "Bukit Batok Street 34",
                        "location": {
                            "latitude": 1.36491,
                            "longitude": 103.75065
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T10:15:00+08:00",
                        "data": [
                            {
                                "stationId": "S218",
                                "value": 0
                            }
                        ]
                    }
                ],
                "readingType": "TB1 Rainfall 5 Minute Total F",
                "readingUnit": "mm"
            },
            "errorMsg": ""
        }

class APIResponseRelativeHumidity:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S109",
                        "deviceId": "S109",
                        "name": "Ang Mo Kio Avenue 5",
                        "location": {
                            "latitude": 1.3764,
                            "longitude": 103.8492
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T10:15:00+08:00",
                        "data": [
                            {
                                "stationId": "S109",
                                "value": 74.2
                            }
                        ]
                    }
                ],
                "readingType": "RH 1M F",
                "readingUnit": "percentage"
            },
            "errorMsg": ""
        }

class APIResponseUVIndex:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T10:00:00+08:00",
                                "value": 2
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T10:11:05+08:00",
                        "timestamp": "2026-01-12T10:00:00+08:00"
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseUVIndexPage1:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T19:00:00+08:00",
                                "value": 0
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T19:10:54+08:00",
                        "timestamp": "2026-01-12T19:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T18:00:00+08:00",
                                "value": 1
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T18:10:58+08:00",
                        "timestamp": "2026-01-12T18:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T17:00:00+08:00",
                                "value": 2
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T17:11:02+08:00",
                        "timestamp": "2026-01-12T17:00:00+08:00"
                    }
                ],
                "paginationToken": "b2Zmc2V0PTI1"
            },
            "errorMsg": ""
        }

class APIResponseUVIndexPage2:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T16:00:00+08:00",
                                "value": 5
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T16:10:45+08:00",
                        "timestamp": "2026-01-12T16:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T15:00:00+08:00",
                                "value": 7
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T15:10:48+08:00",
                        "timestamp": "2026-01-12T15:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T14:00:00+08:00",
                                "value": 8
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T14:10:49+08:00",
                        "timestamp": "2026-01-12T14:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T13:00:00+08:00",
                                "value": 7
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T13:10:52+08:00",
                        "timestamp": "2026-01-12T13:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T12:00:00+08:00",
                                "value": 6
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T12:10:55+08:00",
                        "timestamp": "2026-01-12T12:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T11:00:00+08:00",
                                "value": 4
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T11:10:40+08:00",
                        "timestamp": "2026-01-12T11:00:00+08:00"
                    }
                ],
                "paginationToken": "b2Zmc2V0PTUw"
            },
            "errorMsg": ""
        }

class APIResponseUVIndexPage3:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T14:00:00+08:00",
                                "value": 8
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T14:10:49+08:00",
                        "timestamp": "2026-01-12T14:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T13:00:00+08:00",
                                "value": 7
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T13:10:52+08:00",
                        "timestamp": "2026-01-12T13:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T12:00:00+08:00",
                                "value": 6
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T12:10:55+08:00",
                        "timestamp": "2026-01-12T12:00:00+08:00"
                    },
                    {
                        "index": [
                            {
                                "hour": "2026-01-12T11:00:00+08:00",
                                "value": 4
                            }
                        ],
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T11:10:40+08:00",
                        "timestamp": "2026-01-12T11:00:00+08:00"
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseWBGT:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "datetime": "2026-01-12T10:15:00+08:00",
                        "item": {
                            "isStationData": True,
                            "readings": [
                                {
                                    "station": {
                                        "id": "S124",
                                        "name": "Upper Changi Road North",
                                        "townCenter": "Changi"
                                    },
                                    "location": {
                                        "latitude": "1.36777",
                                        "longitude": "103.982262"
                                    },
                                    "wbgt": "26.3",
                                    "heatStress": "Low"
                                }
                            ],
                            "type": "observation"
                        },
                        "updatedTimestamp": "2026-01-12T10:25:03+08:00"
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseTwoHourWeatherForecast:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "area_metadata": [
                    {
                        "name": "Ang Mo Kio",
                        "label_location": {
                            "latitude": 1.375,
                            "longitude": 103.839
                        }
                    }
                ],
                "items": [
                    {
                        "update_timestamp": "2026-01-12T10:05:34+08:00",
                        "timestamp": "2026-01-12T10:00:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T10:00:00+08:00",
                            "end": "2026-01-12T12:00:00+08:00",
                            "text": "10.00 am to Midday"
                        },
                        "forecasts": [
                            {
                                "area": "Ang Mo Kio",
                                "forecast": "Partly Cloudy (Day)"
                            }
                        ]
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseTwoHourWeatherForecastPage1:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "area_metadata": [
                    {
                        "name": "Ang Mo Kio",
                        "label_location": {
                            "latitude": 1.375,
                            "longitude": 103.839
                        }
                    },
                    {
                        "name": "Bedok",
                        "label_location": {
                            "latitude": 1.321,
                            "longitude": 103.924
                        }
                    },
                    {
                        "name": "Bishan",
                        "label_location": {
                            "latitude": 1.350772,
                            "longitude": 103.839
                        }
                    }
                ],
                "items": [
                    {
                        "update_timestamp": "2026-01-12T23:35:41+08:00",
                        "timestamp": "2026-01-12T23:30:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T23:30:00+08:00",
                            "end": "2026-01-13T01:30:00+08:00",
                            "text": "11.30 pm to 1.30 am"
                        },
                        "forecasts": [
                            {
                                "area": "Ang Mo Kio",
                                "forecast": "Partly Cloudy (Night)"
                            },
                            {
                                "area": "Bedok",
                                "forecast": "Partly Cloudy (Night)"
                            },
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Night)"
                            }
                        ]
                    },
                    {
                        "update_timestamp": "2026-01-12T23:05:38+08:00",
                        "timestamp": "2026-01-12T23:00:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T23:00:00+08:00",
                            "end": "2026-01-13T01:00:00+08:00",
                            "text": "11.00 pm to 1.00 am"
                        },
                        "forecasts": [
                            {
                                "area": "Ang Mo Kio",
                                "forecast": "Partly Cloudy (Night)"
                            },
                            {
                                "area": "Bedok",
                                "forecast": "Partly Cloudy (Night)"
                            },
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Night)"
                            }
                        ]
                    },
                    {
                        "update_timestamp": "2026-01-12T22:35:34+08:00",
                        "timestamp": "2026-01-12T22:30:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T22:30:00+08:00",
                            "end": "2026-01-13T00:30:00+08:00",
                            "text": "10.30 pm to 12.30 am"
                        },
                        "forecasts": [
                            {
                                "area": "Ang Mo Kio",
                                "forecast": "Partly Cloudy (Night)"
                            },
                            {
                                "area": "Bedok",
                                "forecast": "Partly Cloudy (Night)"
                            },
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Night)"
                            }
                        ]
                    }
                ],
                "paginationToken": "b2Zmc2V0PTI1"
            },
            "errorMsg": ""
        }

class APIResponseTwoHourWeatherForecastPage2:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "area_metadata": [
                    {
                        "name": "Bishan",
                        "label_location": {
                            "latitude": 1.350772,
                            "longitude": 103.839
                        }
                    },
                    {
                        "name": "Boon Lay",
                        "label_location": {
                            "latitude": 1.304,
                            "longitude": 103.701
                        }
                    }
                ],
                "items": [
                    {
                        "update_timestamp": "2026-01-12T11:05:36+08:00",
                        "timestamp": "2026-01-12T11:00:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T11:00:00+08:00",
                            "end": "2026-01-12T13:00:00+08:00",
                            "text": "11.00 am to 1.00 pm"
                        },
                        "forecasts": [
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Day)"
                            },
                            {
                                "area": "Boon Lay",
                                "forecast": "Partly Cloudy (Day)"
                            }
                        ]
                    },
                    {
                        "update_timestamp": "2026-01-12T10:35:34+08:00",
                        "timestamp": "2026-01-12T10:30:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T10:30:00+08:00",
                            "end": "2026-01-12T12:30:00+08:00",
                            "text": "10.30 am to 12.30 pm"
                        },
                        "forecasts": [
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Day)"
                            },
                            {
                                "area": "Boon Lay",
                                "forecast": "Partly Cloudy (Day)"
                            }
                        ]
                    },
                    {
                        "update_timestamp": "2026-01-12T10:05:34+08:00",
                        "timestamp": "2026-01-12T10:00:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T10:00:00+08:00",
                            "end": "2026-01-12T12:00:00+08:00",
                            "text": "10.00 am to Midday"
                        },
                        "forecasts": [
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Day)"
                            },
                            {
                                "area": "Boon Lay",
                                "forecast": "Partly Cloudy (Day)"
                            }
                        ]
                    },
                    {
                        "update_timestamp": "2026-01-12T09:35:49+08:00",
                        "timestamp": "2026-01-12T09:30:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T09:30:00+08:00",
                            "end": "2026-01-12T11:30:00+08:00",
                            "text": "9.30 am to 11.30 am"
                        },
                        "forecasts": [
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Day)"
                            },
                            {
                                "area": "Boon Lay",
                                "forecast": "Partly Cloudy (Day)"
                            }
                        ]
                    },
                    {
                        "update_timestamp": "2026-01-12T09:05:34+08:00",
                        "timestamp": "2026-01-12T09:00:00+08:00",
                        "valid_period": {
                            "start": "2026-01-12T09:00:00+08:00",
                            "end": "2026-01-12T11:00:00+08:00",
                            "text": "9.00 am to 11.00 am"
                        },
                        "forecasts": [
                            {
                                "area": "Bishan",
                                "forecast": "Partly Cloudy (Day)"
                            },
                            {
                                "area": "Boon Lay",
                                "forecast": "Partly Cloudy (Day)"
                            }
                        ]
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseTwentyFourHourWeatherForecast:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T05:40:52+08:00",
                        "general": {
                            "temperature": {
                                "low": 23,
                                "high": 32,
                                "unit": "Degrees Celsius"
                            },
                            "relativeHumidity": {
                                "low": 55,
                                "high": 85,
                                "unit": "Percentage"
                            },
                            "forecast": {
                                "code": "WD",
                                "text": "Windy"
                            },
                            "validPeriod": {
                                "start": "2026-01-12T06:00:00+08:00",
                                "end": "2026-01-13T06:00:00+08:00",
                                "text": "6 AM 12 Jan to 6 AM 13 Jan"
                            },
                            "wind": {
                                "speed": {
                                    "low": 15,
                                    "high": 25
                                },
                                "direction": "N"
                            }
                        },
                        "periods": [
                            {
                                "timePeriod": {
                                    "start": "2026-01-12T06:00:00+08:00",
                                    "end": "2026-01-12T12:00:00+08:00",
                                    "text": "6 am to Midday 12 Jan"
                                },
                                "regions": {
                                    "west": {
                                        "code": "PC",
                                        "text": "Partly Cloudy (Day)"
                                    },
                                    "east": {
                                        "code": "PC",
                                        "text": "Partly Cloudy (Day)"
                                    },
                                    "central": {
                                        "code": "PC",
                                        "text": "Partly Cloudy (Day)"
                                    },
                                    "south": {
                                        "code": "PC",
                                        "text": "Partly Cloudy (Day)"
                                    },
                                    "north": {
                                        "code": "PC",
                                        "text": "Partly Cloudy (Day)"
                                    }
                                }
                            },
                            {
                                "timePeriod": {
                                    "start": "2026-01-12T12:00:00+08:00",
                                    "end": "2026-01-12T18:00:00+08:00",
                                    "text": "Midday to 6 pm 12 Jan"
                                },
                                "regions": {
                                    "west": {
                                        "code": "WD",
                                        "text": "Windy"
                                    },
                                    "east": {
                                        "code": "WD",
                                        "text": "Windy"
                                    },
                                    "central": {
                                        "code": "WD",
                                        "text": "Windy"
                                    },
                                    "south": {
                                        "code": "WD",
                                        "text": "Windy"
                                    },
                                    "north": {
                                        "code": "WD",
                                        "text": "Windy"
                                    }
                                }
                            },
                            {
                                "timePeriod": {
                                    "start": "2026-01-12T18:00:00+08:00",
                                    "end": "2026-01-13T06:00:00+08:00",
                                    "text": "6 pm 12 Jan to 6 am 13 Jan"
                                },
                                "regions": {
                                    "west": {
                                        "code": "PN",
                                        "text": "Partly Cloudy (Night)"
                                    },
                                    "east": {
                                        "code": "PN",
                                        "text": "Partly Cloudy (Night)"
                                    },
                                    "central": {
                                        "code": "PN",
                                        "text": "Partly Cloudy (Night)"
                                    },
                                    "south": {
                                        "code": "PN",
                                        "text": "Partly Cloudy (Night)"
                                    },
                                    "north": {
                                        "code": "PN",
                                        "text": "Partly Cloudy (Night)"
                                    }
                                }
                            }
                        ],
                        "timestamp": "2026-01-12T05:30:00+08:00"
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseFourDayWeatherForecast:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "records": [
                    {
                        "date": "2026-01-12",
                        "updatedTimestamp": "2026-01-12T05:20:43+08:00",
                        "forecasts": [
                            {
                                "temperature": {
                                    "low": 24,
                                    "high": 33,
                                    "unit": "Degrees Celsius"
                                },
                                "relativeHumidity": {
                                    "low": 60,
                                    "high": 95,
                                    "unit": "Percentage"
                                },
                                "forecast": {
                                    "summary": "Late afternoon and evening passing showers\n",
                                    "code": "PS",
                                    "text": "Passing Showers"
                                },
                                "day": "Tuesday",
                                "timestamp": "2026-01-13T00:00:00+08:00",
                                "wind": {
                                    "speed": {
                                        "low": 15,
                                        "high": 25
                                    },
                                    "direction": "N"
                                }
                            }
                        ],
                        "timestamp": "2026-01-12T05:09:00+08:00"
                    }
                ]
            },
            "errorMsg": ""
        }

class APIResponseWindDirection:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S108",
                        "deviceId": "S108",
                        "name": "Marina Gardens Drive",
                        "location": {
                            "latitude": 1.2799,
                            "longitude": 103.8703
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T10:15:00+08:00",
                        "data": [
                            {
                                "stationId": "S108",
                                "value": 2
                            }
                        ]
                    }
                ],
                "readingType": "Wind Dir AVG (S) 10M M1M",
                "readingUnit": "degrees"
            },
    "errorMsg": ""
}

class APIResponseWindSpeed:
    status_code = 200

    @staticmethod
    def json():
        return {
            "code": 0,
            "data": {
                "stations": [
                    {
                        "id": "S108",
                        "deviceId": "S108",
                        "name": "Marina Gardens Drive",
                        "location": {
                            "latitude": 1.2799,
                            "longitude": 103.8703
                        }
                    }
                ],
                "readings": [
                    {
                        "timestamp": "2026-01-12T10:15:00+08:00",
                        "data": [
                            {
                                "stationId": "S108",
                                "value": 11.5
                            }
                        ]
                    }
                ],
                "readingType": "Wind Speed AVG(S)10M M1M",
                "readingUnit": "knots"
            },
            "errorMsg": ""
        }

__all__ = [
    'APIResponseAirTemperature',
    'APIResponseAirTemperaturePage1',
    'APIResponseAirTemperaturePage2',
    'APIResponseAirTemperaturePage3',
    'APIResponseFloodAlerts',
    'APIResponseLightning',
    'APIResponsePM25',
    'APIResponsePM25Page1',
    'APIResponsePM25Page2',
    'APIResponsePM25Page3',
    'APIResponsePSI',
    'APIResponseRainfall',
    'APIResponseRelativeHumidity',
    'APIResponseUVIndex',
    'APIResponseUVIndexPage1',
    'APIResponseUVIndexPage2',
    'APIResponseUVIndexPage3',
    'APIResponseWBGT',
    'APIResponseTwoHourWeatherForecast',
    'APIResponseTwoHourWeatherForecastPage1',
    'APIResponseTwoHourWeatherForecastPage2',
    'APIResponseTwentyFourHourWeatherForecast',
    'APIResponseFourDayWeatherForecast',
    'APIResponseWindDirection',
    'APIResponseWindSpeed',
]
