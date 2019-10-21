#What is the total bill? How many people? How much do you owe?

import math
def split_bill (total_bill, number_of_people):
	return math.ceil(total_bill / number_of_people)

total_bill = float(input("What is the total bill?   "))
number_of_people = int(input("How many people?   "))

result = split_bill (total_bill, number_of_people)
print("You owe ${}".format(result))
