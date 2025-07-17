
import random

listw: list = ["pair", "abolish", "throat", "infection", "cunning",
"radiation", "unfortunate", "pastel", "visit", "sunrise",
"population", "ridge", "guest", "extract", "absolute",
"confidence", "storage", "royalty", "cord", "desk",
"ruin", "chalk", "fee", "printer", "bless",
"acquisition", "sound", "curve", "censorship", "glance",
"archive", "press", "decade", "total", "name",
"rotten", "truth", "legislature", "herb", "review",
"alse", "opposition", "ladder", "chemistry", "reflection",
"serve", "school", "gun", "straw", "cancer"]
listn: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

w = ""
n = ""

for _ in range(random.randint(1, 3)):
    w += listw[random.randint(0, len(listw)-1)]

for _ in range(random.randint(1, 5)):
    n += listn[random.randint(0, len(listn)-1)]

print(w + n)