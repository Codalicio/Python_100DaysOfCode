print(f"Welcome to the tip calculator :")

total_bill = float(input("What is the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))
tip_calculated = ((tip / 100) * total_bill)

total_bill_after_tip = total_bill + tip_calculated

splitting_with = int(input("How many people to split the bill with?\n"))

each_person_bill = total_bill_after_tip / splitting_with

print(f"Each person should pay : ${'{:.2f}'.format(each_person_bill)}")
