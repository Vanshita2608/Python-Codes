#slicing
#slicing_and_converting_tuples.py

print("\nSlicing")
devices = ('mouse' , 'keyboard' , 'printer' , 'monitor')
print(devices[1:])
print(devices[::-1])
print(devices[2:4])

print("\nConverting lists to tuples")
l1 = [0,1,2]
t1 = tuple(l1)
print(t1)
#string
print("\nConverting string to tuple")
print(tuple('STRING'))