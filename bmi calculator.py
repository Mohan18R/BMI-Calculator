# Prompt the user to enter their height in meters
height = float(input("Enter your height in meters: "))

# Prompt the user to enter their weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI using the formula weight / (height^2)
bmi = round(weight / (height ** 2))

# Round the calculated BMI to the nearest whole number


# Check the BMI range and display an appropriate message
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
