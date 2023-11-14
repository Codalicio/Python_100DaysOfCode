print(f"Welcome to the tip calculator :")

bill = float(input("What is the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))
tip_calculated = ((tip / 100) * bill)

total_bill_after_tip = bill + tip_calculated

splitting_with = int(input("How many people to split the bill with?\n"))

bill_per_person = total_bill_after_tip / splitting_with

print(f"Each person should pay : ${'{:.2f}'.format(bill_per_person)}")
