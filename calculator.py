#simple score calculator for target v guess. Can be used to simplify games on paper and pen.

def calculator(real, guess):

    real_hash = []
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

real = int(input("Enter your secret number: "))
for i in range(100):
    guess = int(input("Enter opponent's guess: "))
    if calculator(real, guess) == 4:
        break