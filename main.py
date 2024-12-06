"""
This program simulates the population of predators and prey.
In a given ecosystem, the population of a pair of predators and prey is
dependent on the balance of those two populations, which will change over
time in a series of generations. There should be enough prey to feed the
predators and low enough predators as to not overhunt the prey population.
This can be compared to an unbalanced population, where one of the listed
conditions is not met resulting in both populations dying off. However,
should these conditions be met, the population should survive indefinitely
or at least several times the ending generation count of an unbalanced population.


Joshua Schreyer
Connor Lear
December - 2024
"""

import random


def write_results(results: list[str], file_name: str) -> None:
    """
    Writes the results of the simulation to a file
    Parameters:
        results: list[str] - a list of strings, each element is one result
        file_name: str - the name of the file to write to
    """

    with open(file_name, "w") as file:
        for r in results:
            file.write(r + "\n")
    

def main() -> None:

    INITIAL_PREDATORS = 1
    INITIAL_PREY = 5

    PERCENT_CHANCE_TO_KILL = 25
    MIN_KILLINGS = 0
    MAX_KILLINGS = 3

    PREY_GENERATIONS_REPRODUCE = 1
    PREY_MIN_CHILDREN = 1
    PREY_MAX_CHILDREN = 6

    PREDATOR_GENERATIONS_REPRODUCE = 3
    PREDATOR_MIN_CHILDREN = 1
    PREDATOR_MAX_CHILDREN = 2

    GENERATIONS_TO_SIMULATE = 1000
    CARRYING_CAPACITY = 5000
    CARRYING_CAPACITY_PREDATOR_PENALTY = 200
    CARRYING_CAPACITY_PREY_PENALTY = 500

    predators = INITIAL_PREDATORS
    prey = INITIAL_PREY

    prey_reproduce_generation = PREY_GENERATIONS_REPRODUCE - 1
    predators_reproduce_generation = PREDATOR_GENERATIONS_REPRODUCE - 1

    results: list[str] = ["Generation Num,Predators,Prey"]
    for i in range(GENERATIONS_TO_SIMULATE):
        for j in range(predators):
            killings = random.randint(MIN_KILLINGS, MAX_KILLINGS)
            for k in range(killings):
                chance = random.randint(1, 100)
                if chance <= PERCENT_CHANCE_TO_KILL:
                    prey -= 1

        if prey//2 <= predators:
            predators = prey//2
        if prey_reproduce_generation == 0:
            prey_reproduce_generation = PREY_GENERATIONS_REPRODUCE - 1
            for j in range(prey//2):
                newborns = random.randint(PREDATOR_MIN_CHILDREN, PREDATOR_MAX_CHILDREN)
                prey += newborns
        else:
            prey_reproduce_generation -= 1

        if predators_reproduce_generation == 0:
            predators_reproduce_generation = PREDATOR_GENERATIONS_REPRODUCE - 1
            for j in range(0, prey, 2):
                newborns = random.randint(PREY_MIN_CHILDREN, PREY_MAX_CHILDREN)
                predators += newborns
        else:
            predators_reproduce_generation -= 1

        if predators + prey > CARRYING_CAPACITY:
            predators -= CARRYING_CAPACITY_PREDATOR_PENALTY
            prey -= CARRYING_CAPACITY_PREY_PENALTY

        if predators <= 0 and prey <= 0:
            results.append(f"{i}, 0, 0")
            break

        results.append(f"{i}, {predators}, {prey}")

    write_results(results, "results.csv")

if __name__ == "__main__":
    main()
