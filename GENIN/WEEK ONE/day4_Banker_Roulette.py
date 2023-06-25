test_seed = int (input("Create a seed number: "))
random.seed(test_seed)

#Split string method
namesAsCSV = input ("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

#Get the total number of names on the list
num_items = len(names)

#I will generate number between 0 and the last index
random_choice = random.randint(0, num_items - 1)
person_who_pays = names[random_choice]
print (person_who_pays) + "is going to buy the meal today!"