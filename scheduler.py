# -*- coding: utf-8 -*-

from apscheduler.scheduler import Scheduler
import spider_library as sl

# Start the scheduler
sched = Scheduler()
sched.start()

def my_listener(event):
    if event.exception:
        print ('The job crashed :(')
    else:
        print ('The job worked :)')

sched.add_cron_job(sl.getLinks(Url), day_of_week='sun', hour=1, minute=00)
# sched.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
