#importing the time module
import time

#input name
name = input("What is your name? ")

print("Your name is "+ name, "Good Luck !")

#wait for 1 second
time.sleep(1)

print("Start guessing ...")
time.sleep(0.5)

word = ['sasuke', 'sakura', 'naruto', 'gojo',
         'geto', 'kurama', 'nanami', 'yuta',
         'panda', 'hime', 'nobara', 'makizen']


#creates an variables with an empty variables
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero

while turns > 0:
    #make a couter in secret_words
    failed = 0

    # for every character in secret_word
    for char in word:

    # see if the character is in the players guess
        if char in guesses:
            #print then out of the character
            print(char, end=""),
        else:
            #if not found, print a dash
            print ("_", end=""),

            failed += 1
    #if failed is equal to zero
    
    #print you won 
            if failed == 0:
                print("You won")
    #exit the script
                break
    #ask the user go guess a character
            guess = input("guess a character :")

    #set the players guess to guesses
            guesses += guess
#if the guess is not found in the secret word
            if guess not in word:
# turn counter decreases with 1 (now 9)
                turns -= 1
            #print wrong
                print("Wrong")
            #how many turns are left
                print("You have", + turns, 'more guesses')
#if the turns are equal to zero 
                if turns == 0:
            #print "You lose"  
                    print("You lose")  
