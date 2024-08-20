import clockManager, os
from win11toast import toast

clock_manager = clockManager.ClockSystem()

clock_manager.setTimer(0, 1, 10)

lastNotification = 0

while len(clock_manager.timers) > 0:

    if clock_manager.timers["0"] == 600 and lastNotification != 600:
        toast("10 Minutes Remain.")
    
    if clock_manager.timers["0"] == 300 and lastNotification != 300:
        toast("5 Minutes Remain.")
    
    if clock_manager.timers["0"] == 60 and lastNotification != 60:
        toast("1 Minute Remains.")
    
    if clock_manager.timers["0"] == 5 and lastNotification != 5:
        toast("5.")

    if clock_manager.timers["0"] == 4 and lastNotification != 4:
        toast("4.")
    
    if clock_manager.timers["0"] == 3 and lastNotification != 3:
        toast("3.")
    
    if clock_manager.timers["0"] == 2 and lastNotification != 2:
        toast("2.")
    
    if clock_manager.timers["0"] == 1 and lastNotification != 1:
        toast("1.")
    
    clock_manager.tick()

toast("Shut down imminent")



clock_manager.setTimer(0, 0, 15)

while clock_manager.timers != {}:
    clock_manager.tick()

os.system("shutdown -s")