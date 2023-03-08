score=0
"""For practice with python"""
def function1 ():
    """prints the initial prompt for function"""
    print("Welcome, would you like to play a game? ")
function1()
if input()=="yes":
    print("What is yonur name? ")
else: exit()
name=input()
print("What is 1+1? ")
if input()=="2":
    print("correct!")
    score=score+1
else: print("incorrect")
print("What is Tristans first name?(answer in all lowercase) ")
TRISTAN="tristan"
if input()==TRISTAN:
    print("correct!!")
    score=score+1
else:
    print("incorrect")
print("CONGRATULATIONS YOU WIN!!!")
print ("Your score is " + str(score))
