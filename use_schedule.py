#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 13:43
# @Author  : ChenYao
# @File    : use_schedule.py
import datetime
import sched
import threading
import time

'''
使用sched实现定时执行任务
'''


# ---------------sched的enter方法可以实现周期性的调用方法----------------------------


class SchedulerThread(threading.Thread):
    """可以注册每天定时执行的任务, """

    def __init__(self):
        threading.Thread.__init__(self)
        self.schedule = sched.scheduler(time.time, time.sleep)
        self.shutdown = False

    def run(self):
        print("start schedule thread.")
        try:
            self.schedule.run()
        except Exception as ex:
            print("schedule run error:{}".format(ex))
        finally:
            print("exit schedule thread.")

    def exit(self):
        self.shutdown = True

    def enter(self, *args, **kwargs):
        if not self.shutdown:
            self.schedule.enter(*args, **kwargs)

    @staticmethod
    def next_schedule_wait_seconds(hour, minuter):
        now = datetime.now()
        run_time = datetime(now.year, now.month, now.day, hour, minuter)

        if run_time < now:
            run_time = run_time + datetime.timedelta(hours=24)

        delta = run_time - now
        return delta.seconds


def test(scheduler):
    print("haha")
    scheduler.enter(delay=10, priority=0, action=test, argument=(scheduler,))


scheduler = SchedulerThread()
scheduler.start()

scheduler.enter(delay=1, priority=0, action=test, argument=(scheduler,))
