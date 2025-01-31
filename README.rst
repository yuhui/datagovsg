datagovsg
=========

|pyversions| |pypi| |status| |codecov| |downloads| |license| |readthedocs|

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/datagovsg
   :alt: Python 3
.. |pypi| image:: https://img.shields.io/pypi/v/datagovsg
   :alt: PyPi
   :target: https://pypi.org/project/datagovsg
.. |status| image:: https://img.shields.io/pypi/status/datagovsg
   :alt: PyPi status
.. |codecov| image:: https://codecov.io/gh/yuhui/datagovsg/graph/badge.svg?token=ahhqotTFVt
   :target: https://codecov.io/gh/yuhui/datagovsg
   :alt: CodeCov coverage
.. |downloads| image:: https://img.shields.io/pypi/dm/datagovsg
.. |license| image:: https://img.shields.io/github/license/yuhui/datagovsg
   :alt: GNU General Public License v3.0
   :target: https://www.gnu.org/licenses/gpl-3.0.html
.. |readthedocs| image:: https://readthedocs.org/projects/datagovsg/badge/?version=latest
   :alt: Documentation Status
   :target: https://datagovsg.readthedocs.io/en/latest/?badge=latest

This is an unofficial Python package for interacting with APIs available at
`Data.gov.sg`_.

.. _Data.gov.sg: https://data.gov.sg

Installing the package
----------------------

Install the package using ``pip``::

    pip install datagovsg

Using the package
-----------------

The main steps are:

1. Import a class.
2. Instantiate an object from the class.
3. Call a function on that object.

For more information, `refer to the documentation`_.

.. _refer to the documentation: http://datagovsg.readthedocs.io/

Usage overview
^^^^^^^^^^^^^^

Interacting with `Data.gov.sg`_'s API is done through one of four clients, where
each client corresponds with a "set" of endpoints. (`Data.gov.sg`_ doesn't
categorise its endpoints by set, but it can be assumed from the endpoints' path
directories.)

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

Reference
---------

`Data.gov.sg's Developer Guide`_

.. _Data.gov.sg's Developer Guide : https://guide.data.gov.sg/developer-guide/api-overview
