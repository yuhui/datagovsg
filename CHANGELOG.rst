Changelog
=========

[2.0.0] - 2025-01-31
--------------------

Added
^^^^^

- Type hints for input parameters and output responses.
    -  Type check performed by typeguard_.

.. _typeguard: https://typeguard.readthedocs.io/en/latest/

Changed
^^^^^^^

- Compatibility with prevailing Data.gov.sg specifications.
- **Breaking:** Clients have been reorganised to align with Data.gov.sg's categorisation.
    - ``Technology`` client is now ``Economy``.
    - ``carpark_availability()`` method that used to be in ``Transport`` client is now in a new ``Housing`` client.
- Updated minimum Python version to v3.13.

Deprecated
^^^^^^^^^^

- ``Ckan`` client has bee deprecated since Data.gov.sg has removed it.
    - Using any method logs a ``DeprecationWarning`` warning.
    - This client will be removed in the next major release of this package or at the end of 2025, whichever is earlier.

[1.0.3] - 2020-01-21
--------------------

Changed
^^^^^^^

- Updated ``pytest`` requirement.

[1.0.2] - 2019-09-03
--------------------

Changed
^^^^^^^

- Use relative imports.
- Specify base constants to import, instead of ``*``.

[1.0.1] - 2019-08-06
--------------------

Changed
^^^^^^^

- Conform version numbering with SemVer.

[1.0] - 2019-07-29
------------------

Added
^^^^^

- Initial version to interact with Data.gov.sg's documented API endpoints as of July 2019.
