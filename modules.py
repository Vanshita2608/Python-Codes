#modules
print("\n_____MODULES_____")
'''
print("\n1. OS Modules")
import os
os.mkdir("E:\\MyDir_1")
print(os.getcwd())
os.chdir("E:\\MyDir_2")
print(os.getcwd())
os.makedirs("C:\\MyDir_1\\MyDir_2")
os.mdir("E:\\MyDir_1.0")
'''

'''
print("\n\n2. random Module")
import random
print("random floating value 0 to 1")
print(random.random())
print("\nrandom integers")
print(random.randint(1,100))
print("\nrandom elements from range")
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.randrange(0,101,10))
print("\nselecting random elements")
print(random.choice("calculator"))
print(random.choice([1,2,3,4,5,6,7,8,9,10]))
print("\nshuffle")
numL = [21,5,32,65,7,4,2,9,1,6]
print(random.shuffle(numL))
'''

print("\n\n3. datetime Module")
import datetime
dtob = datetime.datetime.now()
print(dtob)
tdate = datetime.date.today()
print(tdate)

from datetime import date
today = date.today()
print("current year = " , today.year)
print("current month = " , today.month)
print("current day = " , today.day)

print("\n\nWORKING WITH time()")
from datetime import time
a = time()
print("a = " , a)
b = time(11,34,56)
print("b = " , b)
c = time(hour=11 , minute=34 , second=56)
print("c = " , c)
d = time(11,34,56,234566)
print("d = " , d)

print("\n\n\n")
from datetime import datetime
a1 = datetime(2017,11,28,23,59,342380)
print("year = " , a1.year)
print("month = " , a1.month)
print("date = " , a1.date)
print("hour = " , a1.hour)
print("minute = " , a1.minute)
print("second = " , a1.second)
print("timestamp = " , a1.timestamp)

print("\n\n__Format date using strftime()")
from datetime import datetime
now = datetime.now()
t = now.strftime("%H : %M : %S")
print("Time = " , t)
s1 = now.strftime("%d / %m / %Y , %H : %M : %S")
print("s1 = " , s1)

print("\n\n__Format date using strptime()")
date_string = "26 August, 2005"
print("date_string = " , date_string)
date_obj = datetime.strptime(date_string, "%d %B, %Y")
print("date_obj = " , date_obj)







'''
%A = week day full name
%B = full month
%b = mon
%m = month number (1-12)
%y = 2 digit year
%Y = 4 digit year
'''




'''
print("\n\n4. calendar Module")
import calendar
yy = 2022
mm = 8
print(calendar.month(yy,mm))

print("__________YEAR 2023__________")
print(calendar.calendar(2023,2,1,6))


print("\n\n5. sys Module")
import sys
print("You entered = " , sys.argv[0] , sys.argv[1] , sys.argv[2])
'''
'''
print(sys.maxsize)
print(sys.path)
print(sys.version)
print(sys.platform)
'''
'''
print("\n\n6. USD Module")
import myMath
print(myMath.add(5,5))
print(myMath.sub(10,5))
'''