import sys
import time

print(sys.version) # to find python version
print("Hello and Welcome to Python")

seconds = time.time() # returns no. of seconds passed since epoch
local_time = time.ctime(seconds) # returns local time
print(local_time)

# adding additional time commands
tm = time.localtime(seconds)
print(tm.tm_year)

# get gmt time
gmt_tm = time.gmtime(seconds)
print(f"{gmt_tm.tm_hour}:{gmt_tm.tm_min}:{gmt_tm.tm_sec}")
