print("Welcome to Python Pizza Deliveries!")
size = input ("What size of pizza do you want? S, M, or L ").lower()
add_pepperoni = input ("Do you want to pepperoni? Y or N ").lower()
extra_cheese = input ("Do you want extra cheese? Y or N ").lower()
#I am going to set the initial bill to zero to make addition less complex
bill = 0

if size == "s":
    #Small size of pizza is 15 dollars
    bill += 15
    #+= 15 means plus 15, vice versa -= 15 meaning minus 15
elif size == "m":
    #medium size of pizza is 20 dollars
    bill += 20
else:
    #Big size of pizza is 25 dollars
    bill += 25

if add_pepperoni == "y":
    if size == "s": 
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")