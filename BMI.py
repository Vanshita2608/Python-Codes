'''   write a python script to calculate body mass  index (BMI) of a person 

      BMI = weight(kg)
	      ------------
	       height_sq(m)

      BMI ranges
        1. less than 18.5 "underweight"
        2. between 18.5 & 24.9  "healthy"
        3. between 25 & 29.9  "overweight"
        4. 30 and 30+  "obese"                       '''


w = int(input("Enter the weight :"))
h = int(input("Enter the height :"))

h = h/100
BMI = (w)/(h**2)

if BMI < 18.5:
	print("\nUnderWeight")
elif BMI>18.5 and BMI<24.9:
	print("\nHealthy")
elif BMI>25 and BMI<29.9:
	print("\nOverWeight")
else:
	print("\nObese")