scheduler
=========

A simple job scheduler with cron expression

Inspired by "`schedule <https://github.com/dbader/schedule>`_".

Usage
-----

.. code-block:: bash

    $ pip3 install scheduler-cron

.. code-block:: python

    import scheduler

    def test_1():
        print('test1')

    def test_2(name):
        print('test2: ' + name)

    def test_3(name, lname):
        print('test3: ' + name + ' ' + lname)

    app = scheduler.Scheduler(60)
    app.add('foo', '* * * * *', test_1)
    app.add('bar', '0/2 * * * *', test_2, ('mehrdad',))
    app.add('bas', '0/3 * * * *', test_3, ('behzad', 'mahmoudi'))
    app.add('zoo', '0/4 * * * *', test_3, ('reza', 'mahmoudi'))
    app.start()


ToDo
-----

  - Run jobs in async mode
  - sleep for more than interval seconds if there is no jobs for next run

Meta
----

Mehrdad Mahmoudi - `@mehrdadmhd <https://twitter.com/mehrdadmhd>`_ - mehrdadmhd@gmail.com

https://github.com/mehrdadmhd/scheduler-py
