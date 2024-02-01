import time
import datetime
f=0
while(1):
    time.sleep(1)
    r=time.time()
    f=f+1
    print(f)
    d=datetime.datetime.now()
    print(d)
