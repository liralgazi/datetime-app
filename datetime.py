import time
import os,sys
import datetime
#import flask 
from datetime import datetime 

f = open('date.txt', 'w+')

while (5>3):
    time.sleep(5)
    now = datetime.datetime.now()
    f.write(f.read() + '\n' + str(now.strftime("%Y-%m-%d %H:%M:%S")))
    print(str(now.strftime("%Y-%m-%d %H:%M:%S")))

f.close()
