Package Overview
================

Interacting with `Data.gov.sg`_'s API is done through one of four clients,
where each client corresponds with a "set" of endpoints. (`Data.gov.sg`_ doesn't
categorise its endpoints by set, but it can be assumed from the endpoints' path
directories.)

.. _Data.gov.sg: https://data.gov.sg

The four clients are: ``Economy``, ``Environment``, ``Housing`` and
``Transport``.

    *Breaking changes from v1.x*

    The ``Economy`` client used to be called ``Technology``.

    The old ``Transport`` client has been separated into ``Housing`` and
    ``Transport``.

    `Data.gov.sg`_ no longer provides endpoints for CKAN, so the ``Ckan``
    client has been deprecated.

Each client contains several public functions, one function per endpoint. A
function's name is the same as its corresponding endpoint's ending path.

Most functions accept named arguments, where an argument corresponds with a
parameter that the endpoint accepts.

    *Why have separate clients instead of one single client?*

    Without knowing how `Data.gov.sg`_'s API will evolve, and noticing that
    Data.gov.sg uses "Categories" to group its endpoints, it seemed like a
    good idea to keep each set of endpoints in its own contextual client. This
    allows for each "set" of endpoints to be customised on their own, e.g. the
    ``Environment`` endpoints allow for either a date or date-time to be
    specified, whereas the ``Transport`` endpoints don't.
