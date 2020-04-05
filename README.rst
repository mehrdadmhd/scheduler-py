scheduler
========

A simple job scheduler with cron expression

Inspired by `"schedule" <https://github.com/dbader/schedule>`_ .

Usage
-----

.. code-block:: bash

    $ pip3 install git+https://git.asiatech.ir/dev/scheduler-py.git --upgrade

.. code-block:: python

    import scheduler

    def test_1():
        print('test1')

    def test_2(name):
        print('test2: ' + name)

    def test_3(name, lname):
        print('test3: ' + name + ' ' + lname)

    scheduler = Scheduler(60)
    scheduler.add('foo', '* * * * *', test_1)
    scheduler.add('bar', '0/2 * * * *', test_2, ('mehrdad',))
    scheduler.add('bas', '0/3 * * * *', test_3, ('behzad', 'mahmoudi'))
    scheduler.add('zoo', '0/4 * * * *', test_3, ('reza', 'mahmoudi'))
    scheduler.start()


ToDo
-----

  - Run jobs in async mode
  - sleep for more than interval seconds if there is no jobs for next run

Meta
----

Mehrdad Mahmoudi - `@mehrdadmhd <https://twitter.com/mehrdadmhd>`_ - mehrdadmhd@gmail.com

https://github.com/mehrdadmhd/scheduler-py