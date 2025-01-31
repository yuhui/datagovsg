datagovsg.environment.types Response Types
==========================================

.. automodule:: datagovsg.environment.types

Common Types
------------

.. autoclass:: _AreaMetadataDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _LabelLocationDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _RegionMetadataDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _RegionReadingsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _StationDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _StationReadingDataDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _StationReadingDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastLowHighDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastLowHighUnitDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastValidPeriodDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastWindSpeedDirectionDict
   :members:
   :member-order: bysource
   :show-inheritance:

air_temperature(), rainfall(), relative_humidity(), wind_direction(), wind_speed()
----------------------------------------------------------------------------------

.. autoclass:: EnvironmentReadingDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WindSpeedStationDict
   :members:
   :member-order: bysource
   :show-inheritance:

pm25()
------

.. autoclass:: PM25Dict
   :members:
   :member-order: bysource
   :show-inheritance:

   .. py:attribute:: items
      :type: list[_PM25ItemDict]

      Items.

.. autoclass:: _PM25ItemDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _PM25ItemReadingsDict
   :members:
   :member-order: bysource
   :show-inheritance:

psi()
-----

.. autoclass:: PSIDict
   :members:
   :member-order: bysource
   :show-inheritance:

   .. py:attribute:: items
      :type: list[_PSIItemDict]

      Items.

.. autoclass:: _PSIItemDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _PSIItemReadingsDict
   :members:
   :member-order: bysource
   :show-inheritance:

uv_index()
----------

.. autoclass:: UVIndexDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _UVIndexRecordDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _UVIndexRecordHourlyIndexDict
   :members:
   :member-order: bysource
   :show-inheritance:

two_hour_weather_forecast()
---------------------------

.. autoclass:: WeatherForecastTwoHourDict
   :members:
   :member-order: bysource
   :show-inheritance:

   .. py:attribute:: items
      :type: list[_WeatherForecastTwoHourItemDict]

      Items.

.. autoclass:: _WeatherForecastTwoHourItemDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastTwoHourItemForecastDict
   :members:
   :member-order: bysource
   :show-inheritance:

twenty_four_hour_weather_forecast()
-----------------------------------

.. autoclass:: WeatherForecastTwentyFourHourDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastTwentyFourHourRecordDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastTwentyFourHourRecordPeriodDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastTwentyFourHourRecordPeriodRegionsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastTwentyFourHourRecordGeneralDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastTwentyFourHourRecordForecastDict
   :members:
   :member-order: bysource
   :show-inheritance:

four_day_weather_forecast()
---------------------------

.. autoclass:: WeatherForecastFourDayDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastFourDayRecordDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastFourDayRecordForecastDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: _WeatherForecastFourDayRecordForecastForecastDict
   :members:
   :member-order: bysource
   :show-inheritance:
