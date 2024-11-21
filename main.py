"""
This is high enough game
Connor Lear - Novermber 2024
"""

import random

def main():
    d1: int = random.randint(1,6)
    d2: int = random.randint(1,6)
    d3: int = random.randint(1,6)

    d4 = d1+d2+d3

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    if d4 > 13:
        print("You win")
    else:
        print("You lose")


if __name__ == "__main__":
    main()