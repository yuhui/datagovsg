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

"""Data.gov.sg custom types for Environment client methods' responses."""

from datetime import date, datetime
from typing import NotRequired
try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

# Common types

class _LabelLocationDict(TypedDict):
    """Type definition for various custom types"""

    latitude: float
    """Latitude coordinate of the region label.

    :example: 1.2799
    """
    longitude: float
    """Longitude coordinate of the region label.

    :example: 103.8703
    """

class _AreaMetadataDict(TypedDict):
    """Type definition for various custom types"""

    name: str
    """Name of the area.

    :example: "Ang Mo Kio"
    """
    label_location: _LabelLocationDict
    """Provides longitude and latitude for placing readings on a map."""

class _RegionMetadataDict(TypedDict):
    """Type definition for various custom types"""

    name: str
    """Region name.

    :example: "West"
    """
    labelLocation: _LabelLocationDict
    """Provides longitude and latitude for placing readings on a map."""

class _RegionReadingsDict(TypedDict):
    """Type definition for various custom types"""

    national: NotRequired[int]
    """Reading for national reporting stations.

    :example: 24
    """
    east: int
    """Reading for east region.

    :example: 18
    """
    west: int
    """Reading for west region.

    :example: 12
    """
    north: int
    """Reading for north region.

    :example: 11
    """
    south: int
    """Reading for south region.

    :example: 8
    """
    central: int
    """Reading for central region.

    :example: 7
    """

class _StationDict(TypedDict):
    """Type definition for various custom types"""

    id: str
    """Station's ID.

    :example: "S108"
    """
    deviceId: str
    """Reading Device's ID (usually same as Station's ID).

    :example: "S108"
    """
    name: str
    """Station's name.

    :example: "Marina Gardens Drive"
    """
    labelLocation: _LabelLocationDict
    """Provides longitude and latitude for placing readings on a map."""

class _StationReadingDataDict(TypedDict):
    """Type definition for various custom types"""

    stationId: str
    """Station ID.

    :example: "S108"
    """
    value: float
    """Value.

    :example: 29.0
    """

class _StationReadingDict(TypedDict):
    """Type definition for various custom types"""

    timestamp: datetime
    """Timestamp.

    :example: datetime(2025, 1, 12, 15, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    data: list[_StationReadingDataDict]
    """Data"""

class _WeatherForecastLowHighDict(TypedDict):
    """Type definition for various custom types"""

    low: int | float
    """Low value.

    :example: 15
    """
    high: int | float
    """High value.

    :example: 30
    """

class _WeatherForecastLowHighUnitDict(TypedDict):
    """Type definition for various custom types"""

    low: int | float
    """Low value.

    :example: 26
    """
    high: int | float
    """High value.

    :example: 36
    """
    unit: str
    """Unit of measure."""

class _WeatherForecastValidPeriodDict(TypedDict):
    """Type definition for various custom types"""

    start: datetime
    """Valid period start time.

    :example: datetime(2025, 1, 12, 16, 30, 0)
    """
    end: datetime
    """Valid period end time.

    :example: datetime(2025, 1, 12, 18, 30, 0)
    """
    text: str
    """Valid period in text.

    :example: "12.30 am to 2.30 am"
    """

class _WeatherForecastWindSpeedDirectionDict(TypedDict):
    """Type definition for various custom types"""
    speed: _WeatherForecastLowHighDict
    """Speed."""
    direction: str
    """Direction.

    :example: "SSE"
    """

# Air Temperature, Rainfall, Relative Humidity, Wind Direction, Wind Speed

class _WindSpeedStationDict(TypedDict):
    """Type definition for EnvironmentReadingDict"""

    id: str
    """Station's ID.

    :example: "S108"
    """
    deviceId: str
    """Reading Device's ID (usually same as Station's ID).

    :example: "S108"
    """
    name: str
    """Station's name.

    :example: "Marina Gardens Drive"
    """
    location: _LabelLocationDict
    """Label location."""

class EnvironmentReadingDict(TypedDict):
    """Type definition for air_temperature(), rainfall(), \
        relative_humidity(), wind_direction() and wind_speed()"""

    stations: list[_StationDict | _WindSpeedStationDict]
    """Stations."""
    readings: list[_StationReadingDict]
    """Readings."""
    readingType: str
    """Information about the reading.

    :example: Air Temperature: "DBT 1M F"
    :example: Rainfall: "DTB1 Rainfall 5 Minute Total F"
    :example: Relative Humidity: "RH 1M F"
    :example: Wind Direction: "Wind Dir AVG (S) 10M M1M"
    :example: Wind Speed: "Wind Speed AVG(S)10M M1M"
    """
    readingUnit: str
    """Measurement unit for reading.

    :example: Air Temperature: "deg code"
    :example: Rainfall: "mm"
    :example: Relative Humidity: "percentage"
    :example: Wind Direction: "degrees"
    :example: Wind Speed: "knots"
    """

# PM2.5

class _PM25ItemReadingsDict(TypedDict):
    """Type definition for _PM25ItemDict"""

    pm25_one_hourly: _RegionReadingsDict
    """PM2.5 one-hourly readings."""

class _PM25ItemDict(TypedDict):
    """Type definition for PM25Dict"""

    date: date
    """SGT date of the reading.

    :example: date(2024, 7, 17)
    """
    updatedTimestamp: datetime
    """SGT timestamp of last updated.

    :example: datetime(2024, 7, 17, 14, 15, 43, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    timestamp: datetime
    """SGT timestamp of the reading.

    :example: datetime(2024, 7, 17, 6, 0, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    readings: _PM25ItemReadingsDict
    """Overall and regional PSI data including pollutant concentrations and \
        sub-indices.
    """

class PM25Dict(TypedDict):
    """Type definition for pm25()"""

    regionMetadata: list[_RegionMetadataDict]
    """Region metadata."""
    items: list[_PM25ItemDict]
    """Items."""

# PSI

class _PSIItemReadingsDict(TypedDict):
    """Type definition for _PSIItemDict"""

    co_eight_hour_max: _RegionReadingsDict
    """Carbon monoxide 8-hourly maximum. Concentration is measured in \
        micrograms per cubic metre.
    """
    co_sub_index: _RegionReadingsDict
    """Carbon monoxide sub-index. Concentration is measured in micrograms per \
        cubic metre.
    """
    no2_one_hour_max: _RegionReadingsDict
    """Nitrogen dioxide 1-hourly maximum. Concentration is measured in \
        micrograms per cubic metre.
    """
    o3_eight_hour_max: _RegionReadingsDict
    """Ozone 8-hourly maximum. Concentration is measured in micrograms per \
        cubic metre.
    """
    o3_sub_index: _RegionReadingsDict
    """Ozone sub-index. Concentration is measured in micrograms per cubic \
        metre.
    """
    so2_twenty_four_hourly: _RegionReadingsDict
    """Sulpher dioxide 24-hourly readings. Concentration is measured in \
        micrograms per cubic metre.
    """
    so2_sub_index: _RegionReadingsDict
    """Sulpher dioxide sub-index. Concentration is measured in micrograms per \
        cubic metre.
    """
    pm10_twenty_four_hourly: _RegionReadingsDict
    """PM1.0 24-hourly readings. Concentration is measured in micrograms per \
        cubic metre.
    """
    pm10_sub_index: _RegionReadingsDict
    """PM1.0 sub-index. Concentration is measured in micrograms per cubic \
        metre.
    """
    pm25_twenty_four_hourly: _RegionReadingsDict
    """PM2.5 24-hourly readings. Concentration is measured in micrograms per \
        cubic metre.
    """
    pm25_sub_index: _RegionReadingsDict
    """PM2.5 sub-index. Concentration is measured in micrograms per cubic \
        metre.
    """
    psi_three_hourly: NotRequired[_RegionReadingsDict]
    """PSI 3-hourly readings. Concentration is measured in micrograms per \
        cubic metre.
    """
    psi_twenty_four_hourly: _RegionReadingsDict
    """PSI 24-hourly readings. Concentration is measured in micrograms per \
        cubic metre.
    """

class _PSIItemDict(TypedDict):
    """Type definition for PSIDict"""

    date: date
    """SGT date of the reading.

    :example: date(2024, 7, 17)
    """
    updatedTimestamp: datetime
    """SGT timestamp of last updated.

    :example: datetime(2024, 7, 17, 14, 15, 43, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    timestamp: datetime
    """SGT timestamp of the reading.

    :example: datetime(2024, 7, 17, 6, 0, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    readings: _PSIItemReadingsDict
    """Overall and regional PSI data including pollutant concentrations and \
        sub-indices.
    """

class PSIDict(TypedDict):
    """Type definition for psi()"""

    regionMetadata: list[_RegionMetadataDict]
    """Region metadata."""
    items: list[_PSIItemDict]
    """Itms."""

# UV Index

class _UVIndexRecordHourlyIndexDict(TypedDict):
    """Type definition for _UVIndexRecordDict"""

    hour: datetime
    """"Hour indicating the start of the hour for which the index is for.

    :example: datetime(2024, 7, 17, 11, 0, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    value: float
    """"UV index for the hour.

    :example: 1
    """

class _UVIndexRecordDict(TypedDict):
    """Type definition for UVIndexDict"""

    date: date
    """SGT date of the reading.

    :example: date(2024, 7, 17)
    """
    updatedTimestamp: datetime
    """SGT timestamp of last updated.

    :example: datetime(2024, 7, 17, 14, 15, 43, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    timestamp: datetime
    """SGT timestamp of the reading.

    :example: datetime(2024, 7, 17, 6, 0, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    index: list[_UVIndexRecordHourlyIndexDict]
    """Reverse-chronologically ordered indexes."""

class UVIndexDict(TypedDict):
    """Type definition for uvIndex()"""

    records: list[_UVIndexRecordDict]
    """Records."""

# Weather Forecast: 2-Hour

class _WeatherForecastTwoHourItemForecastDict(TypedDict):
    """Type definition for WeatherForecastTwoHourDict"""

    area: str
    """Area.

    :example: "Ang Mo Kio"
    """
    forecast: str
    """Forecast. One of:

    - "Fair"
    - "Fair (Day)"
    - "Fair (Night)"
    - "Fair and Warm"
    - "Partly Cloudy"
    - "Partly Cloudy (Day)"
    - "Partly Cloudy (Night)"
    - "Cloudy"
    - "Hazy"
    - "Slightly Hazy"
    - "Windy"
    - "Mist"
    - "Fog"
    - "Light Rain"
    - "Moderate Rain"
    - "Heavy Rain"
    - "Passing Showers"
    - "Light Showers"
    - "Showers"
    - "Heavy Showers"
    - "Thundery Showers"
    - "Heavy Thundery Showers"
    - "Heavy Thundery Showers with Gusty Winds"
    """

class _WeatherForecastTwoHourItemDict(TypedDict):
    """Type definition for WeatherForecastTwoHourDict"""

    update_timestamp: datetime
    """Time of acquisition of data from NEA.

    :example: datetime(2024, 7, 17, 5, 5, 54, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    timestamp: datetime
    """Time that forecast was issued by NEA.

    :example: datetime(2024, 7, 17, 4, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    valid_period: _WeatherForecastValidPeriodDict
    """Period of time the forecast is valid for."""
    forecasts: list[_WeatherForecastTwoHourItemForecastDict]
    """Forecasts for various areas in Singapore."""

class WeatherForecastTwoHourDict(TypedDict):
    """Type definition for two_hour_weather_forecast()"""

    area_metadata: list[_AreaMetadataDict]
    """Area metadata."""
    items: list[_WeatherForecastTwoHourItemDict]
    """Items."""

# Weather Forecast: 24-Hour

class _WeatherForecastTwentyFourHourRecordForecastDict(TypedDict):
    """Type definition for _WeatherForecastTwentyFourHourRecordGeneralDict \
        and _WeatherForecastTwentyFourHourRecordPeriodRegionDict
    """

    code: str
    """Forecast code.

    :example: "FA"
    """
    text: str
    """Forecast text. One of:

    - "Fair"
    - "Fair (Day)"
    - "Fair (Night)"
    - "Fair and Warm"
    - "Partly Cloudy"
    - "Partly Cloudy (Day)"
    - "Partly Cloudy (Night)"
    - "Cloudy"
    - "Hazy"
    - "Slightly Hazy"
    - "Windy"
    - "Mist"
    - "Fog"
    - "Light Rain"
    - "Moderate Rain"
    - "Heavy Rain"
    - "Passing Showers"
    - "Light Showers"
    - "Showers"
    - "Heavy Showers"
    - "Thundery Showers"
    - "Heavy Thundery Showers"
    - "Heavy Thundery Showers with Gusty Winds"
    """

class _WeatherForecastTwentyFourHourRecordGeneralDict(TypedDict):
    """Type definition for _WeatherForecastTwentyFourHourRecordDict"""

    validPeriod: _WeatherForecastValidPeriodDict
    """Period of time the forecast is valid for."""
    temperature: _WeatherForecastLowHighUnitDict
    """Unit of measure - Degrees Celsius."""
    relativeHumidity: _WeatherForecastLowHighUnitDict
    """Unit of measure - Percentage"""
    forecast: _WeatherForecastTwentyFourHourRecordForecastDict
    """Forecast."""
    wind: _WeatherForecastWindSpeedDirectionDict
    """Wind."""

class _WeatherForecastTwentyFourHourRecordPeriodRegionsDict(TypedDict):
    """Type definition for _WeatherForecastTwentyFourHourRecordPeriodDict"""

    east: _WeatherForecastTwentyFourHourRecordForecastDict
    """Forecast for east region."""
    west: _WeatherForecastTwentyFourHourRecordForecastDict
    """Forecast for west region."""
    north: _WeatherForecastTwentyFourHourRecordForecastDict
    """Forecast for north region."""
    south: _WeatherForecastTwentyFourHourRecordForecastDict
    """Forecast for south region."""
    central: _WeatherForecastTwentyFourHourRecordForecastDict
    """Forecast for central region."""

class _WeatherForecastTwentyFourHourRecordPeriodDict(TypedDict):
    """Type definition for _WeatherForecastTwentyFourHourRecordDict"""

    timePeriod: _WeatherForecastValidPeriodDict
    """Period of time the forecast is valid for."""
    regions: _WeatherForecastTwentyFourHourRecordPeriodRegionsDict
    """Regional forecast."""

class _WeatherForecastTwentyFourHourRecordDict(TypedDict):
    """Type definition for WeatherForecastTwentyFourHourDict"""

    date: date
    """Date of the forecast from NEA.

    :example: date(2024, 7, 17)
    """
    updatedTimestamp: datetime
    """Time of acquisition of data from NEA.

    :example: datetime(2024, 7, 17, 5, 5, 54, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    timestamp: datetime
    """Time that forecast was issued by NEA.

    :example: datetime(2024, 7, 17, 4, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    general: _WeatherForecastTwentyFourHourRecordGeneralDict
    """A general weather forecast for the 24-hour period."""
    periods: list[_WeatherForecastTwentyFourHourRecordPeriodDict]
    """Forecasts for various areas in Singapore."""

class WeatherForecastTwentyFourHourDict(TypedDict):
    """Type definition for twenty_four_hour_weather_forecast()"""

    area_metadata: NotRequired[list[_AreaMetadataDict]]
    """Area metadata."""
    records: list[_WeatherForecastTwentyFourHourRecordDict]
    """Records."""

# Weather Forecast: 4-Day

class _WeatherForecastFourDayRecordForecastForecastDict(TypedDict):
    """Type definition for _WeatherForecastFourDayRecordForecastDict"""

    summary: str
    """Summary.

    :example: "Fair and occasionally windy"
    """
    code: str
    """Forecast code.

    :example: "FA"
    """
    text: str
    """Forecast. One of:

    - "Fair"
    - "Fair (Day)"
    - "Fair (Night)"
    - "Fair and Warm"
    - "Partly Cloudy"
    - "Partly Cloudy (Day)"
    - "Partly Cloudy (Night)"
    - "Cloudy"
    - "Hazy"
    - "Slightly Hazy"
    - "Windy"
    - "Mist"
    - "Fog"
    - "Light Rain"
    - "Moderate Rain"
    - "Heavy Rain"
    - "Passing Showers"
    - "Light Showers"
    - "Showers"
    - "Heavy Showers"
    - "Thundery Showers"
    - "Heavy Thundery Showers"
    - "Heavy Thundery Showers with Gusty Winds"
    """

class _WeatherForecastFourDayRecordForecastDict(TypedDict):
    """Type definition for _WeatherForecastFourDayRecordDict"""

    timestamp: datetime
    """Time that forecast was issued by NEA.

    :example: datetime(2024, 7, 17, 16, 0, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    day: str
    """Day of week. One of:

    - "Monday"
    - "Tuesday"
    - "Wednesday"
    - "Thursday"
    - "Friday"
    - "Saturday"
    - "Sunday"
    """
    temperature: _WeatherForecastLowHighUnitDict
    """Unit of measure - Degrees Celsius."""
    relativeHumidity: _WeatherForecastLowHighUnitDict
    """Unit of measure - Percentage."""
    forecast: _WeatherForecastFourDayRecordForecastForecastDict
    """Forecast."""
    wind: _WeatherForecastWindSpeedDirectionDict
    """Wind."""

class _WeatherForecastFourDayRecordDict(TypedDict):
    """Type definition for WeatherForecastFourDayDict"""

    date: date
    """Date of the forecast from NEA.

    :example: date(2024, 7, 17)
    """
    updatedTimestamp: datetime
    """Time of acquisition of data from NEA.

    :example: datetime(2024, 7, 17, 5, 5, 54, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    timestamp: datetime
    """Time that forecast was issued by NEA.

    :example: datetime(2024, 7, 17, 4, 59, 0, \
        tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
    """
    forecasts: list[_WeatherForecastFourDayRecordForecastDict]
    """Forecast summary for the days."""

class WeatherForecastFourDayDict(TypedDict):
    """Type definition for four_day_weather_forecast()"""

    records: list[_WeatherForecastFourDayRecordDict]
    """Records."""

__all__ = [
    'EnvironmentReadingDict',
    'PM25Dict',
    'PSIDict',
    'UVIndexDict',
    'WeatherForecastTwoHourDict',
    'WeatherForecastTwentyFourHourDict',
    'WeatherForecastFourDayDict',
]
