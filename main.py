"""
Connor Lear - December 2024
"""


import random


def roll_n_times(n: int) -> int:
   print()


prey_amount: int = 10
preditor_amount: int = 1
#You have to make prey and preditor names plurul
prey_name: str = "Pigs"
preditor_name: str = "People"
most_childs = 2
least_childs = 1
max_preditor_kills = 2
generations_one_turn = 100
print(f"""There are {prey_amount} {prey_name}!
There are {preditor_amount} {preditor_name}!
This is the first {generations_one_turn} generations!""")


print()


for _ in range(generations_one_turn):
	for _ in range(prey_amount):
		prey_births: int = random.randint(least_childs, most_childs)
		prey_amount += prey_births
	for _ in range(preditor_amount):
		preditor_kills: int = random.randint(1, max_preditor_kills)
		prey_amount -= preditor_kills
		if preditor_kills >= 2:
			preditor_amount += max_preditor_kills - 1


print(f"""There are now {prey_amount} {prey_name}!
There are now {preditor_amount} {preditor_name}!
This is the second {generations_one_turn} generations!""")