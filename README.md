# Automatic-Computer-Shutdown-Timer
This program automatically shuts down your computer after the specified amount of time using the "os.system()" function. It also uses the "win11toast" library to send you warning of how long until the shutdown via notifications.

In order to change the amount of time, go into the code and find "clock_manager.setTimer(0, 1, 10)". You can set the amount of time by setting the hours in the first argument, the minutes in the second argument, and the seconds in the final argument.


Libraries:
 - win11toast (pip install win11toast)
 - os (included with Python installation)
