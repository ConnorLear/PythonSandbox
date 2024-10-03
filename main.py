def wrong():
  print("")
  print("You got this answer wrong!")
  print("Now you have to completly restart!")
  exit()
def correct():
  print("")
  print("Correct! Next question.")
def p():
  print("")

#This is the intro
username = input("Hello ")
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
question = #
"""

pa1 = input()

"""
correct_answers = ["C", "c"]

if correct_answers.count(pa1):
  correct()
else:
  wrong()  
"""

if pa1 == "C" or "c":
  correct()
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

pa2 = input()

if pa2 == "D" or "d":
  p()
  print("Okay? Then what is your answer?")
  p()
  ps2 = input()
  
else:
  wrong()

