# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4, then the computer picks sticks(1-4). Who ever will pick the last stick will lose.
# Look for the TODO blocks as an indication of when you have to add your own code.
import random
sticks = 21

def playGame():
    # you do not need to modify code in this function
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
        

def askUserChoice():
    while True:
        usersChoice=input('Choose a number of sticks between (1-4) to pick up')
        if usersChoice=='1' or usersChoice=='2' or usersChoice=='3' or usersChoice=='4': #making sure 1 2 3 and 4 are the only valid inputs
            break
        print('NO CHEATING')#no cheating message displayed if user chooses a number other than 1 2 3 or 4

    return (int(usersChoice))#returns the valid input



def subtractSticks( number ):
    global sticks
    sticks=sticks-number # 1. subtracts the parameter `number` from the global variable `sticks`
    if sticks<1:
        return True# 2. checks if the number subtracted resulted in the last stick, if so, return True
    if sticks>0:
        return False # 3. if there are still sticks left, return False
    
def determineComputerChoice():
    RandomComputerChoice=random.randint(1,4)#using randomint function to make the computer randomly choose 1 2 3 or 4 sticks.
    return RandomComputerChoice#returning the above function
    # TODO: write code inside this function that returns an integer between 1 and 4, random chosen by the computer
