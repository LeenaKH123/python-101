# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
import datetime, time

time1 = time.strftime("%H:%M:%S:%MS", time.localtime())
print(time1)
