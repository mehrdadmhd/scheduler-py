from threading import Thread

import croniter
import datetime
import time


class Scheduler(object):
    def __init__(self, interval):
        self.jobs = {}
        self.schedule = []
        self.interval = interval
        self.last_check = None
        self.started = False
        self.shutdown = False

        self._refresh_times()

    def start(self):
        if self.started:
            return

        self.started = True

        thread = Thread(target=self._do)
        thread.start()

    def _do(self):

        while not self.shutdown:
            now = datetime.datetime.now()

            for alias in self.schedule:
                self.jobs[alias].run(now)

            self._refresh_times(True)
            time.sleep(self.interval)


    def add(self, alias, expression, func, args=None):
        self.jobs[alias] = Job(alias, expression, func, args)
        # self._refresh_times()

    def _refresh_times(self, force=False):

        if self.last_check is None or force:
            self.last_check = datetime.datetime.now()

        check_for = self.last_check + datetime.timedelta(seconds=self.interval)

        self.schedule = []
        for alias, job in self.jobs.items():
            if job.can_run(check_for):
                self.schedule.append(alias)


class Job(object):


    def __init__(self, alias, cron_expression, func, args):
        self.is_periodic = False
        self.cron_expression = cron_expression
        self.last_run = None
        self.next_run = None
        self.job_func = func
        self.job_func_args = args
        self.alias = alias

        self.cron_expression_obj = CronExpression(cron_expression)
        self.next_run = self.cron_expression_obj.get_next()

    def can_run(self, time_to_run):
        return self.next_run != self.last_run and self.next_run <= time_to_run

    def run(self, now):
        if self.next_run == self.last_run:
            return

        self.next_run = self.cron_expression_obj.get_next(True)
        self.last_run = now

        if self.job_func_args is None:
            self.job_func()
        else:
            self.job_func(*self.job_func_args)



class CronExpression(object):

    def __init__(self, cron_expression):
        self.cron_expression = cron_expression
        self.last_run = None
        self.next_run = None

        self._process_cron_expression()

    def _process_cron_expression(self):

        if self.last_run is None:
            self.last_run = datetime.datetime.now()

        self.cron = croniter.croniter(self.cron_expression, self.last_run)

        self.get_next()

    def get_next(self, force=False):
        if self.next_run is None or force:
            self.next_run = self.cron.get_next(datetime.datetime)

        return self.next_run

