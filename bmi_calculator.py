# BMI Calculator
# Developed by: Reena Kushwaha
# Internship Project - Oasis Infobyte

height_cm = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

height_m = height_cm / 100

bmi = weight / (height_m * height_m)

print("Your BMI is:", round(bmi,2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")