Changelog
=========

[2.2.0] - 2026-05-04
--------------------

Added
^^^^^

- Check that dates in methods' arguments are within the range of dates for which data is available.

Changed
^^^^^^^

- Change Economy methods' response types to be more generic.
    - This is due to the poor state of the documentation about the response types.
- Update list of allowed date string formats.
- When building parameters, allow whether to remove parameters with ``None`` values.
- Sanitised comma-separated numbers as tuples of those numbers.
- Set default error message and also mention if `data` and/or `errors` attributes are set in the error.

[2.1.0] - 2026-04-05
--------------------

Added
^^^^^

- New Environment methods: ``flood_alerts()``, ``lightning()`` and ``wbgt()``.
- Support use of Data.gov.sg API key with all clients.

Changed
^^^^^^^

- **Breaking:** Remove ``Ckan`` client.
- Specify allowed date and datetime string formats.
- Set datetime correctly in Singapore timezone.
- Require expected parameter type when building query parameters.
- Improve data sanitisation. Allow specifying of keys to ignore when sanitising.
- Refactor some constants.

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

- ``Ckan`` client has been deprecated since Data.gov.sg has removed it.
    - Using any method logs a ``DeprecationWarning`` warning.
    - This client will be removed in the next major release of this package or at the end of 2025, whichever is earlier.

[1.0.3] - 2020-01-21
--------------------

Changed
^^^^^^^

- Update ``pytest`` requirement.

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
