#display 3rd largest number
#3rd_largest_tuple.py

t = (3,4,5,6,7,8,9,10)
t1 = sorted(t,reverse=True)
print(t1)
print("3rd largest number : " , t1[2])