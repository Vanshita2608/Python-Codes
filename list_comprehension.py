#list comprehension

print("\nnew_list = [expression for member in iterable]")
sent = 'Unity Has Strength'
char = [i for i in sent]
print("All characters = " , char)

print("\nnew_list = [expression for member in iterable(if condition)]")
sent = 'Unity Has Strength'
vowels = [i for i in sent if i in 'aeiou']
print("Vowels = " , vowels)

print("\nnew_list = [expression (if logic else logic) for member in iterable]")
org_prices = [1.25 , -9.45 , 10.22 , 3.78 , -5.92 , 1.16]
prices = [i if i>0 else 0 for i in org_prices]
print("Prices = " , prices)