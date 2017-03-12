#import time
#day=time.localtime(time.time())
import time
import threading
import os

def timer_start():
    t = threading.Timer(1, test_func)
    t.start()

def test_func():
    day=time.localtime(time.time())
    d=day.tm_mday
    h=day.tm_hour
    m=day.tm_min
    s=day.tm_sec
    if d==1 and h==0 and m==0 and s==0:
    	os.system("php xcat sendDiaryMail")
        os.system("php xcat resetTraffic")
    timer_start()

def timer2():
    timer_start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    timer2()

