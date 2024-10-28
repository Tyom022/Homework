# task 1
var_number = int(input("Please enter the number: "))

if var_number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")
    
# task 2
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Slightly overweight")
elif 30 <= bmi < 35:
    print("Obese")
else:
    print("Clinically obese")

# task 3

year = int(input("Input the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The Year is leap")
else:
    print("The year is not leap")

# task 4
choose_pizza = str(input("We have 3 sizes pizza Small Medum Large:choose ex:(S,M,L): "))
bill = 0 
if choose_pizza == "S":
    bill += 15
    var_peperoni = str(input("add peperoni?ex: (Y/N): "))
    if var_peperoni == "Y":
        bill += 1
elif choose_pizza == "M":
    bill += 20
    var_peperoni = str(input("add peperoni?ex: (Y/N): "))
    if var_peperoni == "Y":
        bill += 2
elif choose_pizza == "L":
    bill += 25
    var_peperoni = str(input("add peperoni?ex: (Y/N): "))
    if var_peperoni == "Y":
        bill += 3
else:
    print("We havnt this type ")
    
var_addChesse = str(input("add cheese? ex: (Y/N) "))
if var_addChesse == "Y":
    bill += 3

print(f"Your bill is {bill} ")