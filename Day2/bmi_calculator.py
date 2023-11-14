height = float(input("Enter heigh in meters :\n"))
weight = int(input("Enter weight in kilograms :\n"))

# bmi = round((weight / height ** 2))
# bmi = round((weight / height ** 2), 5)
bmi = "{:.3f}".format(weight / height ** 2)
# bmi = (weight // height ** 2)

print(f"Your BMI is {bmi}")
