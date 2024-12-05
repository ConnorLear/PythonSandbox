"""
Connor Lear - December 2024
"""

import random

def p(MAAAAAAPS):
    print(MAAAAAAPS)

def roll_n_times(n: int) -> int:
    print()

prey_amount: int = 10
preditor_amount: int = 1
#You have to make prey and preditor names plurul
prey_name: str = "Pigs"
preditor_name: str = "People"
most_childs = 5
least_childs = 1
max_preditor_kills = 2
generations_one_turn = 1000

p(f"""There are {prey_amount} {prey_name}!
There are {preditor_amount} {preditor_name}!
This is the first {generations_one_turn} generations!""")

p("")

for i in range(generations_one_turn):
	prey_births: int = random.randint(least_childs, most_childs)
	prey_amount += prey_births
	for i in range(preditor_amount):
		preditor_kills: int = random.randint(1, max_preditor_kills)
		if preditor_kills == 2:
			preditor_amount += max_preditor_kills - 1

p(f"""There are now {prey_amount} {prey_name}!
There are now {preditor_amount} {preditor_name}!
This is the second {generations_one_turn} generations!""")