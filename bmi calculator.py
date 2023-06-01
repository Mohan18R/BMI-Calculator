# Prompt the user to enter their height in meters
height = float(input("Enter your height in meters: "))

# Prompt the user to enter their weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI using the formula weight / (height^2)
bmi = weight / (height ** 2)

# Round the calculated BMI to the nearest whole number
BMI = round(bmi)

# Check the BMI range and display an appropriate message
if bmi < 18.5:
    print("Your BMI is " + str(BMI) + ", you are underweight.")
elif bmi < 25:
    print("Your BMI is " + str(BMI) + ", you have a normal weight.")
elif bmi < 30:
    print("Your BMI is " + str(BMI) + ", you are slightly overweight.")
elif bmi < 35:
    print("Your BMI is " + str(BMI) + ", you are obese.")
else:
    print("Your BMI is " + str(BMI) + ", you are clinically obese.")
