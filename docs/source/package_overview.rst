Package Overview
================

Interacting with `Data.gov.sg`_'s API is done through one of four clients, where each client corresponds with a "set" of endpoints. (`Data.gov.sg`_ doesn't categorise its endpoints by set, but it can be assumed from the endpoints' path directories.)

.. _Data.gov.sg: https://data.gov.sg

The four clients are: ``Ckan``, ``Environment``, ``Technology`` and ``Transport``.

Each client contains several public functions, one function per endpoint. A function's name is the same as its corresponding endpoint's ending path.

Most functions accept named arguments, where an argument corresponds with a parameter that the endpoint accepts.

    *Why have separate clients instead of one single client?*

    Without knowing how `Data.gov.sg`_'s API will evolve, and noticing that the endpoints were themselves already partitioned into "sets", it seemed like a good idea to keep each set of endpoints in its own contextual client. This allows for each "set" of endpoints to be customised on their own, e.g. the ``Environment`` endpoints allow for either a date or date-time to be specified, whereas the ``Transport`` endpoints don't.
