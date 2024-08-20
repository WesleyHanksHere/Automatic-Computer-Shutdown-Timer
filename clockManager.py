from win11toast import toast
import os, time, sys


class ClockSystem:

    def __init__(self):
        self.alarms = {}
        self.timers = {}
        self.lastRecordedTime = int(time.time())
    
    def tick(self):
        if self.lastRecordedTime < int(time.time()):

            if self.alarms != {}:
                for key in self.alarms.keys():
                    if self.alarms[key] == time.localtime(int(time.time())):
                        del(self.alarms[key])

            if self.timers != {}:
                for key in self.timers.keys():
                    self.timers[key] -= int(time.time()) - self.lastRecordedTime
                    if self.timers[key] <= 0:
                        del(self.timers[key])
                        toast("Timer Elapsed")
                        break
            self.lastRecordedTime = int(time.time())
    
    def setTimer(self, hours, minutes, seconds):
        self.timers[str(len(self.timers))] = seconds
        self.timers[str(len(self.timers) - 1)] += minutes*60
        self.timers[str(len(self.timers) - 1)] += hours*60*60



if __name__ == "__main__":
    clock_manager = ClockSystem()
    clock_manager.setTimer(0, 0, 20)
    while clock_manager.timers:
        clock_manager.tick()