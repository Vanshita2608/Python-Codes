#multithreading
#multithreading.py

'''
print("\n1.")
import threading
from threading import *
print(current_thread().getName())
def mt():
	print("Executing thread name = " ,current_thread().getName())
child = Thread(target = mt)
child.start()
print("Executing thread name = " ,current_thread().getName())
'''

'''
print("\n2.")
import threading
from threading import *
print(current_thread().getName())
def mt():
	print("Executing thread name = " ,current_thread().getName())
child = Thread(target = mt)
child.setName("Child")
child.start()
print("Executing thread name = " ,current_thread().getName())
'''

'''
print("\n3.")
import threading
from threading import *
print(current_thread().getName())
def div7():
	print("Executing thread name = " ,current_thread().getName())
	for i in range(0,20):
		if(i%7==0):
			print(i)
child = Thread(target = div7)
child.setName("Child")
child.start()
print("Executing thread name = " ,current_thread().getName())
'''

'''
print("\nWithout creating a class.")
import threading
from threading import *
print(current_thread().getName())
def div7():
	print("Executing thread name = " ,current_thread().getName())
	for i in range(0,20):
		if(i%7==0):
			print(i)

def div5():
	print("Executing thread name = " ,current_thread().getName())
	for i in range(0,20):
		if(i%5==0):
			print(i)


child1 = Thread(target = div7)
child2 = Thread(target = div5)

child1.setName("Child_1")
child2.setName("Child_2")

child1.start()
child2.start()

child1.join()
child2.join()
print("Exiting Main")
'''

'''
print("\nBy extending thread class")
import threading
from threading import *
class MyThread(threading.Thread):
	def run(self):
		for x in range(7):
			print("Child")
a = MyThread()
a.start()
a.join()
print("End of " ,current_thread().getName())
'''

'''
print("\nWithout extending thread class")
import threading
from threading import *
class ex:
	def myfunc(self):
		for x in range(7):
			print("Child")
myobj = ex()
t1 = Thread(target = myobj.myfunc)
t1.start()
t1.join()
print("Done")
'''

'''
print("\nWithout synchronization")
import threading
from threading import *
import time
def wish(name,age):
	for i in range(3):
		print("Hi" , name)
		time.sleep(2)
		print("Age" , age)
t1 = Thread(target = wish , args = ("ABC" , 19))
t2 = Thread(target = wish , args = ("XYZ" , 29))
t1.start()
t2.start()
'''

'''
print("\nWith synchronization (race condition)")
import threading
from threading import *
import time
l = Lock()
def wish(name,age):
	for i in range(3):
		l.acquire()
		print("Hi" , name)
		time.sleep(2)
		print("Age" , age)
		l.release()
t1 = Thread(target = wish , args = ("ABC" , 19))
t2 = Thread(target = wish , args = ("XYZ" , 29))
t1.start()
t2.start()
t1.join()
t2.join()
print("Main Exiting")
'''


print("\nQ. Write a python script to count numbers divisible by 7 from 1-100.")
print("Create 2 threads to count the numbers, divide the work/task between them equally")
print("Display individual as well as total count")
import threading
from threading import *
import time

count = 0
def DivBy7(start,end):
	global count
	for i in range(start,end+1):
		if(i%7==0):
			print(i)
			count += 1
			time.sleep(1)

t1 = Thread(target = DivBy7 , args = (1,50))
t2 = Thread(target = DivBy7 , args = (51,100))
t1.start()
t2.start()
t1.join()
t2.join()
print("Count = " , count)
print("Exiting Main")