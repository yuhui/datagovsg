datagovsg.transport
===================

.. automodule:: datagovsg.transport.client

Example usage:

.. code-block:: python

    # get the list of available taxis
    from datagovsg import Transport
    from datagovsg.transport.types import TaxiAvailabilityDict
    transport = Transport()
    taxi_availability: TaxiAvailabilityDict = transport.taxi_availability()

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Types
-----

.. toctree::
   :maxdepth: 1

   datagovsg.transport.types_args
   datagovsg.transport.types
