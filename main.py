def p():
  print("")
def wrong():
  p()
  print("Wrong! Now you have to restart the entire game.")
  p()
  exit()

#This is the intro to the program
username = input("Hello, (Username here) >")
print("""You have been welcomed to this game!
Maybe the one you can't finish. Maybe your hell.""")
p()
print("There are ten questions")
p()

#Question 1
print("""First Question:
What is 1+1=!""")
p()

#Answers Question 1
print("""A. 2
B. 11
C. Window
D. None of the above""")
p()

#Conformation so the player writes the right answer
print("(btw write the letter not the answer)")
p()

"""
player = p
answer = a
second answer = s
question = #
"""

#Answer
pa1 = input().lower()
if pa1 == "c":
  p()
  print("Correct! Next question.")
else:
  wrong()  
p()

#Question 2
print("""Second Question:
If 1+1= Window then when does 2+2=!""")
p()

#Answer Question 2
print("""A. 2 Windows
B. 4
C. 4 o'clock
D. Other""")
p()

#Answer
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
  print("""How. I didn't even put that answer on the
screen. Ok if your so confident then what
was the answer for e.""")





