weight=float(input("Enter your weight in kilograms"))
height=float(input("Enter your height in meters"))
a = (height*height)
BMI= (weight/a)
if(BMI<=18.5):
    print("your BMI is",BMI)
    print("Your are in the category of underweight")
elif(18.5 <= BMI < 25):
    print("your BMI is",BMI)
    print("Your are in the category of normalweight")
elif(25 <= BMI < 30):
    print("your BMI is",BMI)
    print("Your are in the category of overweight")
else:
    print("your BMI is",BMI)
    print("Your are in the category of obese")
