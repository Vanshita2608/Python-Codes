#integers
print("\nDATA TYPES")
print("\n\nINTEGERS")
a = 100
print("Value of a =" , a)
print("Binary" , 0b101)
print("Octal" , 0o10)
print("Hexadecimal" , 0x25)

#floating point
print("\n\nFLOATING POINT")
f1 = 4.2
f2 = .4
f3 = 5.
print("f1 = " , f1)
print("f2 = " , f2)
print("f3 = " , f3)
f4 = 6e+2
f5 = 6E-2
print("f4 = " , f4)
print("f5 = " , f5)
f6 = 1.79e308
f7 = 1.8e308
print("f6 = " , f6)
print("f7 = " , f7)

#complex numbers
print("\n\nCOMPLEX NUMBERS")
c1 = 2+3j
print("c1 = " , c1)
c2 = complex(5,6)
print("c2 = " , c2)
c3 = complex(8,-4)
print("c3 = " , c3)

#boolen
print("\n\nBOOLEAN")
b1 = True
b2 = False
print("Value of b1 = " , b1)
print("Value of b2 = " , b2)
print("2>4" , 2>4)
print("5<10" , 5<10)

#operators
print("\n\nOPERATORS")
print("\nARITHMETIC OPERATORS")
print("+ - * / are known")
a = 5
b = 2
print("Floor Division = " , a//b)
print("Exponent = " , a**b)

#identity operators
print("\n\nIDENTITY OPERATORS")
x = 5
y = 6
z = y
print("z is y = " , z is y)
print("z is x = " , z is x)
print("y is x = " , y is x)
print("y is not x = " , y is not x)
print("------> CACHING")
a = 7
b = 7
print("id of a = " , id(a))
print("id of b = " , id(b))
b = 8
print("id of b = " , id(b))

#membership opeartors
print("\n\nMEMBERSHIP OPERATORS")
str = "Python Operators"
print("P" in str)
print("Python" in str)
print("python" in str)
print("python" not in str)
dict = {6:"June" , 10:"Dec"}
print(6 in dict)
print("Dec" in dict)

#different style of printing
print("\n\nDIFFERENT SYLE OF PRINT")
print("HI" , "FRIENDS" , sep='-' , end='\n')

#immutability
print("\n\nIMMUTABILITY")
str1 = "Hello"
print(id(str1))
str1 = str1 + "World"
print(id(str1))