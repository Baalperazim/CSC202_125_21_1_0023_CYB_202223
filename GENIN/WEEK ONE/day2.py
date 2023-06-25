#if the bill is $150.00, split between 5 people, with 12% tip,
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#I will round the result to 2 decimal places = 33.60
print ("Welcome to the tip Calculator!")
#changing the integer value to a float to aid division of floating point numbers
bill = float (input("What is the Total Bill? $"))
tip =int( input ("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round (bill_per_person, 2)
print (f"Each person should pay {final_amount} dollar")
