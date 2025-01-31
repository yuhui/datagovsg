# Copyright 2025 Yuhui. All rights reserved.
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

"""Data.gov.sg custom types for Transport client methods' responses."""

from datetime import datetime
from typing import NotRequired
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

from ..types import Url

# Common types

class _ApiInfoDict(TypedDict):
    """Type definition for various custom types"""

    status: str
    """Status. One of:

    - "healthy"
    """

# Carpark Availability

class _CarparkAvailabilityItemDataInfoDict(TypedDict):
    """Type definition for _CarparkAvailabilityItemDataDict"""

    total_lots: int
    """Total number of carpark lots.

    :example: 105
    """
    lot_type: str
    """Type of carpark lot.

    :example: "C"
    """
    lots_available: int
    """Total number of available carpark lots.

    :example: 86
    """

class _CarparkAvailabilityItemDataDict(TypedDict):
    """Type definition for _CarparkAvailabilityItemDict"""

    carpark_info: list[_CarparkAvailabilityItemDataInfoDict]
    """Carpark information."""
    carpark_number: str
    """Carpark number.

    :example: "HE12"
    """
    update_datetime: datetime
    """Update date-time.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """

class _CarparkAvailabilityItemDict(TypedDict):
    """Type definition for CarparkAvailabilityDict"""

    timestamp: datetime
    """Time of acquisition of data.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    carpark_data: list[_CarparkAvailabilityItemDataDict]
    """Carpark availability information per carpark."""

class CarparkAvailabilityDict(TypedDict):
    """Type definition for carpark_availability()"""

    items: list[_CarparkAvailabilityItemDict]
    """Items."""

# Taxi Availability

class _TaxiAvailabilityCrsPropertiesDict(TypedDict):
    """Type definition for _TaxiAvailabilityCrsDict"""

    href: Url
    """Href link.

    :example: "http://spatialreference.org/ref/epsg/4326/ogcwkt/"
    """
    type: str
    """Type.

    :example: "ogcwkt"
    """

class _TaxiAvailabilityCrsDict(TypedDict):
    """Type definition for TaxiAvailabilityDict"""

    type: str
    """Type.

    :example: "link"
    """
    properties: _TaxiAvailabilityCrsPropertiesDict
    """Properties."""

class _TaxiAvailabilityFeatureGeometryDict(TypedDict):
    """Type definition for _TaxiAvailabilityFeatureDict"""

    type: str
    """Type. One of:

    - "MultiPoint"
    """
    coordinates: list[list[float]]
    """A position (longitude, latitude).

    :example: [103.62403, 1.28675]
    """

class _TaxiAvailabilityFeaturePropertiesDict(TypedDict):
    """Type definition for _TaxiAvailabilityFeatureDict"""

    timestamp: datetime
    """Time of acquisition of data from LTA's Datamall.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    taxi_count: int
    """Total number of available taxis.

    :example: 207
    """
    api_info: _ApiInfoDict
    """API info."""

class _TaxiAvailabilityFeatureDict(TypedDict):
    """Type definition for TaxiAvailabilityDict"""

    type: str
    """Type.

    :example: "Feature"
    """
    geometry: _TaxiAvailabilityFeatureGeometryDict
    """Geometry."""
    properties: _TaxiAvailabilityFeaturePropertiesDict
    """Additional meta-data from Data.gov.sg."""

class TaxiAvailabilityDict(TypedDict):
    """Type definition for taxi_availability()"""

    type: str
    """A GeoJSON representing the locations of available taxis in Singapore.

    :example: "FeatureCollection"
    """
    crs: _TaxiAvailabilityCrsDict
    """The coordinate reference system used."""
    features: list[_TaxiAvailabilityFeatureDict]
    """Locations of available taxis."""

# Traffic Images

class _TrafficImagesItemCameraMetadataDict(TypedDict):
    """Type definition for _TrafficImagesItemCameraDict"""

    height: int
    """Height of the image (pixels).

    :example: 240
    """
    width: int
    """Width of the image (pixels).

    :example: 320
    """
    md5: str
    """MD5 hash of image file.

    :example: "ce2a62f561c6073f0b63e14a9a094d8a"
    """

class _TrafficImagesItemCameraLocationDict(TypedDict):
    """Type definition for _TrafficImagesItemCameraDict"""

    latitude: float
    """Latitude.

    :example: 1.29531332
    """
    longitude: float
    """Longitude.

    :example: 103.871146
    """

class _TrafficImagesItemCameraDict(TypedDict):
    """Type definition for _TrafficImagesItemDict"""

    timestamp: datetime
    """Time of image.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    camera_id: str
    """Camera ID provided by LTA.

    :example: "1001"
    """
    image_id: NotRequired[str]
    """Image ID provided by LTA."""
    image: Url
    """URL of image.

    :example: \
        "https://images.data.gov.sg/api/traffic-images/2024/12/eca383cf-a380-4c57-8f15-84f9652e3cd3.jpg"
    """
    image_metadata: _TrafficImagesItemCameraMetadataDict
    """Metadata of the image file."""
    location: _TrafficImagesItemCameraLocationDict
    """Location."""

class _TrafficImagesItemDict(TypedDict):
    """Type definition for TrafficImagesDict"""

    timestamp: datetime
    """Time of acquisition of data.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    cameras: list[_TrafficImagesItemCameraDict]
    """Camera information and images."""

class TrafficImagesDict(TypedDict):
    """Type definition for traffic_images()"""

    items: list[_TrafficImagesItemDict]
    """Items."""
    api_info: _ApiInfoDict
    """API info."""


__all__ = [
    'TaxiAvailabilityDict',
    'TrafficImagesDict',
]
