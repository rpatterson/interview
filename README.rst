==================================
Verkada - Server Coding Assignment
==================================

Below are instructions on how to build and run my submission for the
assignment.  Discussion of my approach, thoughts, and other notes can
be found further below that.


Setting Up and Running
----------------------

To just run the solution containerized via Docker, use
``docker-compose`` in this directory::

  $ docker-compose up

You can see the camera simulation and API activity and interactions in
the logging output on the console.  Then visit the `/logs/ API
endpoint <http://127.0.0.1:5000/logs/>`_ to try it out.

This solution also includes support for running and testing locally
using ``make`` for easier debugging, editor/IDE integration, etc..  I
wouldn't stick with ``make`` in the long term on a real production
project, of course, but in the spirit of avoiding "premature
optimization" it works just fine until real build requirements are
encountered that would help in choosing something better.  All make
targets will bootstrap and build the local environment and docker
environment as needed.

Use the ``test`` target to run the tests, including, static analysis,
test coverage, linting, and running the tests in the docker
containers::

  $ make test

Similarly, use the ``run`` target to run the solution locally::

  $ make run

If you ever need to rebuild a clean environment, including
``docker-compose`` as much as it supports it, use the ``clean``
target::

  $ make clean


Notes
-----

The heart of the assignment is, of course, asynchronous programming.  I
got caught up and spent too much time researching The Right Way (tm)
to use asynchronous programming to fit each of the bits in this
assignment.  For example, regarding the long polling from the camera,
I wanted to ensure that the solution was based on the ``select()``
system call on the network socket since that would likely be most
efficient.  In the end I had to reign myself in and just went with
Python's default OOTB multi-threading based ``async/await``.

I have written tests for asynchronous code in the past.  It's
interesting, very possible, and improves my code, but it is also
significantly more difficult and time consuming than writing tests for
synchronous code.  Forgive me, but I opted to skip writing tests for
the asynchronous bits.  I did write some tests for the camera event
log implementation in ``camera/camera/tests/test_camera.py`` to show
that I can write tests.

Regarding containerizing the Flask REST API server, any proper
production environment should, of course, use a proper WSGI server,
such as uWSGI, and should be served via a proper web server, such as
nginx.  Since the exercise specifies just 2 containers, I'm assuming
the intention is to skip such production deployment considerations for
the purposes of this exercise.  On a related note, while looking for
base docker images to build off of, I found some of the more popular
images to be doing things "The Wrong Way"(tm) IMNSHO, for example
running uWSGI *and* nginx in the same container, using supervisord
inside a container for process management, etc..  As such I opted for
building on the latest minimal Python image built by Docker.

While writing up this documentation, I had a browser request to the
logs API endpoint hang, so there's probably a bug, I'm guessing a race
condition of some sort.  I haven't looked into it yet and I can't
reproduce it now.
