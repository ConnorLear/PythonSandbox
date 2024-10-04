def p():
  print("")
def wrong():
  p()
  print("Wrong! Now you have to restart the entire game.")
  p()
  exit()

#This is the intro
username = input("Hello, (Username here) >")
print("You have been welcomed to this game! ")
print("Maybe the one you can't finish. Maybe your hell.")

p()

print("There are ten questions")

p()

#This is question 1
print("First Question:")
print("What is 1+1=!")

p()
#Answers
print("A. 2")
print("B. 11")
print("C. Window")
print("D. None of the above")

p()
#A conformation so the player writes the right answer
print("(btw write the letter not the answer)")

p()
"""
Player answer -
player = p
answer = a
second answer = s
question = #
"""

pa1 = input().lower()

if pa1 == "c":
  p()
  print("Correct! Next question.")
else:
  wrong()  

p()

print("Second Question:")
print("If 1+1= Window then when does 2+2=!")

p()

print("A. 2 Windows")
print("B. 4")
print("C. 4 o'clock")
print("D. Other")

p()

pa2 = input().lower()

if pa2 == "d":
  p()
  print("Okay? Then what is your answer?")
  p()
  ps2 = input()
  if ps2 == "2 windows o'clock" or "2 Windows o'clock":
    p()
    print("Okay? I don't know how you got that but lets continue.")
  else:
    wrong()
else:
  wrong()

p()

print("Third Question:")
print("This is an easy one. If 1+1= window, and")
print("1+1 equals 2, then what does 5+6=!")

p()

pa3 = int(input("Answer here: "))

if pa3 == 11:
  p()
  ps3 = input("Are you sure?: ").lower()
  if ps3 == "no":
    p()
    print("Okay maybe your smart, or you've done this a millon")
    print("times but we know the first possibility isn't true.")
    print("Next question I guess.")
  else:
    wrong()
else:
  wrong()

p()

print("Fourth Question:")
print("What is the rarrest species on earth.")

p()

pa4 = input().lower()

if pa4 == "this question is to hard":
  p()
  print("I know write...  WAIT! HOW DID YOU")
  print("GUESS THAT ANSWER. Are you cheating?")
else:
  wrong()

p()

print("Question 5:")
print("What do dogs eat.")

p()

print("A. Chinese People")
print("B. Cats")
print("C. Dogs")
print("D. Feces")

p()

pa5 = input().lower()

p()

if pa5 == "e":
  p()
  print("How. I didn't even put that answer on the")
  print("screen. Ok if your so confident then what")
  print("was the answer for e.")





