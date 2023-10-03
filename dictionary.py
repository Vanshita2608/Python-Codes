#dictionary

#empty
print("\nEmpty dictionary")
d1 = {}
print(d1)
print(type(d1))

#elements
print("\nDictionary with elements")
d2 = {1:'C' , 2:'C++'}
print(d2)

#rules
print("\n\n___RULES___")
print("1. Key")
print("Keys have constraint to be of any immutable data types such as a string, numer or a tuple. These can't be repeated")
d3 = {'hi':1 , 1:'bye' , (1,2,3):5}
print(d3)
# invalid --> d3 = {[1,2,3]:1}

print("\n2. Value")
print("Value in a dictionary can be of aqny valid python data type Values can be repeated")
d4 = {1:'C' , 2:'C++' , 3:[1,2,3]}

#creating a dict with each item as a pair
print("\nCreating a dict with each item as a pair")
d5 = dict([(1,'ABC') , (2,'DEF')])
print(d5)

#creating a nested dictionary
print("\nCreating a nested dictionary")
d6 = {1:'Dog' , 2:'Cat' , 3:{'A':'a' , 'B':'b' , 'C':'c'}}
print(d6)

#Accessing dictionary elements
print("\n\nAccessing dictionary elements")
d7 = {'Name':'ABC' , 'RollNo':123 , 'Sub':'Python'}
print("Name = " , d7['Name'])
print("Roll No = " , d7['RollNo'])
print("Subject = " , d7['Sub'])

#Adding elements to a dictionary
print("\nAdding elements to a dictionary")
d8 = {}
print("Dictionary before adding = " , d8)
d8[0] = 'ABC'
d8[1] = 'DEF'
d8[2] = 123
print("Dictionary after adding = " , d8)
d8['Value_set'] = 2,3,4
print(d8)
d8[2] = 'Welcome'
print(d8)

#Accessing elements of nested dictionary
print("\nAccessing elements of nested dictionary")
d9 = {'d1':{1:'ABC'}, 'd2':{'lang':'Python'}}
print(d9)
print(d9['d1'])
print(d9['d1'][1])
print(d9['d2']['lang'])