import random

randNum = int(random.randrange(0, 100))
checkCor = False
while checkCor == False:
    numberGuess = int(input("Guess the Numero!"))
    if numberGuess == randNum :
        print("Heheh, you got it!")
        checkCor = True
    elif numberGuess > randNum :
        print("Lower, pal buddy chum")
    elif numberGuess < randNum:
        print("Higher xd")