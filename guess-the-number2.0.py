import random 
x= random.randint(1,6) 
guess = int(raw_input ( " guess the number : "))
while guess != x: 
    if guess>x: 
        print"guess lower"
    if guess<x: 
        print "guess higher" 
    print "better luck next time : "
    guess= int(raw_input ( " guess the number : "))