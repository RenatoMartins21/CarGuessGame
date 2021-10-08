import random
import datetime
import csv
now = datetime.datetime.now()
print('\t\tWelcome to Word Guess game!')
print('You have 3 attempts to guess the word that I have choosen, the theme is Cars!')

file = open("cars.txt", "r")
WORDS = file.read().split(',')
word = random.choice(WORDS)
correct = word
tries = 1

print('Length of the word: ', len(word),'\n')
guess = input('Guess the word: ')

while guess.lower() != correct.lower() and guess != "" and tries <= 2:
    print("No!")
    tries += 1
    guess = input("Guess the word: ")
    
if guess.lower() == correct.lower():
    print("\nYes! You guessed the word! The word was: ", correct)
    print("You guessed it in ", tries)
    nick = input("What is your name?")


    with open('people.csv', 'w') as csvfile:
        fieldnames = ['name', 'tries', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'name': nick, 'tries': tries, 'date': now})

        
else:
    print('\nNo! You ran out of tries!')
    
input('\n\nPress the Enter key to exit.')
