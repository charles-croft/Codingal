a = (float(input("Height (cm): ")))
b = (float(input("Weight (kg): ")))
BMI = b/(a/100)**2
print ("Your BMI is: ", BMI)
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print ("You are healthy")
elif BMI <= 29.9:
    print ("You are overweight")
elif BMI <= 34.4:
    print ("You are severly overweight")
elif BMI <= 39.9:
    print ("You are obese")
else:
    print ("You are severly obese")