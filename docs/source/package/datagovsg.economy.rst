datagovsg.economy
=================

.. automodule:: datagovsg.economy.client

Example usage:

.. code-block:: python

    # get the patents lodged on 1 August 2018
    from datetime import date
    from datagovsg import Economy
    from datagovsg.economy.types import EconomyDict
    economy = Economy()
    patents: EconomyDict = economy.patents(lodgement_date=date(2018, 8, 1))

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Types
-----

.. toctree::
   :maxdepth: 1

   datagovsg.economy.types_args
   datagovsg.economy.types
