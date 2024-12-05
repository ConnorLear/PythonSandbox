

data = input()

rock = data.count("R")

paper = data.count("P")

scissors = data.count("S")

winners = []

if rock >= scissors and not(scissors >= rock):
    winners.append("ROCK")

if scissors >= paper and not(rock >= scissors):
    winners.append("SCISSORS")

if paper >= rock and not(scissors >= paper):
    winners.append("PAPER")

if len(winners) == 1:
    print(winners[0])
else:
    print("NO WINNER")