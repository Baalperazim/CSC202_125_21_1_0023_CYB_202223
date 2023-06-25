#This odd or even number determiner will use the modulo operator to know which number is odd or even. 
#Using if and else satements

number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print ("This is an even number.")
else:
    print ("This is an odd number.")