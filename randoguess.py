#Simple terminal player for the Bulls and Cows Game

import random

real = random.randrange(1000,10000)

real_hash = []

def calculator():
    guess = int(input("Enter a 4 digit number between 1000 and 9999 (inclusive)"))

    guess_hash = []
    cows = 0
    bulls = 0

    for i in range(4):
        real_hash.append(int((real%(10**(i+1)))/10**i))

    for i in range(4):
        guess_hash.append(int((guess%(10**(i+1)))/10**i))

    for j in range(4):
        if real_hash[j] == guess_hash[j]:
            bulls = bulls + 1
        for k in range(4):
            count = 0
            for l in range(k-1, -1, -1):
                if guess_hash[k] == guess_hash[l]:
                    count = count + 1
            if(count):
                continue
            if real_hash[j] == guess_hash[k] and j != k and real_hash[j] != guess_hash[j]:
                cows = cows + 1



    print("cows:",cows)
    print("bulls:",bulls)
    return bulls

guesses = 0
for guesses in range(1000):
    guesses = guesses + 1
    if calculator() == 4:
        break

print("Number of guesses: ", guesses)
print("Congratulations")