datagovsg.environment
=====================

.. automodule:: datagovsg.environment.client

Example usage:

.. code-block:: python

    # get the latest lightning observations
   from datagovsg import Environment
   from datagovsg.environment.types import WeatherDict
   environment = Environment()
   lightning: WeatherDict = environment.lightning()

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Types
-----

.. toctree::
   :maxdepth: 1

   datagovsg.environment.types_args
   datagovsg.environment.types
