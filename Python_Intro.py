import sys
import time

print(sys.version) # to find python version
print("Hello and Welcome to Python")

seconds = time.time() # returns no. of seconds passed since epoch
local_time = time.ctime(seconds) # returns local time
print(local_time)

