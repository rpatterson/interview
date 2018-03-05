===============================
Density API Homework Assignment
===============================

You can find the output of ``sqlite3 db.sqlite3 .schema`` in the file,
``schema.sql``, for the SQL needed to generate the schema needed for
the current state of the code.

Provided are Django ORM models for spaces, doorways, DPU's and passes.
The ``interview.models.Space.count_passes(start, end)`` model instance
method returns the entry and exit counts for a given space within the
time period given.  See ``interview/tests/test_models.py`` for more
examples.

I hit the 4 hour limit before I could wire up the endpoint.  Next step
would be to wire up a DRF endpoint that accepts datetime filters and
includes ``entries`` and ``exits`` counts in the JSON payload.

Regarding scaling to production, it would depend on the high traffic
use cases.  Obviously with 100,000 DPUs, the endpoint that records
passes will have to be performant and scalable.  The current schema is
simple enough that pass inserts shouldn't be too expensive, but at
that scale we might expect an RDBMS to run into write limits.  As
such, we'd probably want to research moving the passes table to some
other NoSQL store of some sort with high write throughput but still
able to perform counts on large record sets efficiently.  Most
important, however, would be to abstract this performance sensitive
are of the code such that swapping out implementations will require
minimal refactoring or other code changes.

See ``notes.rst`` for more stream-of-consciousness notes following my
process.


Initial Setup
-------------

Use make to bootstrap and build the initial python environment::

  $ make

If you ever need to rebuild a clean environment, use the clean target::

  $ make clean


Tests
-----

Use the test target to to run static analysis, tests, and a coverage report::

  $ make test
