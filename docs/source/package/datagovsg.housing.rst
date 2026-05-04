datagovsg.housing
===================

.. automodule:: datagovsg.housing.client

Example usage:

.. code-block:: python

    # get the list of available car park spaces
    from datagovsg import Housing
    from datagovsg.housing.types import CarparkAvailabilityItemDict
    housing = Housing()
    carpark_availability: list[CarparkAvailabilityItemDict] = housing.carpark_availability()

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Types
-----

.. toctree::
   :maxdepth: 1

   datagovsg.housing.types_args
   datagovsg.housing.types
