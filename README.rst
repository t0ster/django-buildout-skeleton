Installation and Setup
======================

::

    python bootstrap.py
    ./bin/buildout
    ./bin/django syncdb
    ./bin/django collectstatic
    ./bin/runserver


Go to http://localhost:8000

Running Tests::

    ./bin/test
