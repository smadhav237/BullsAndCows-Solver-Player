#Creates the table of all possible outcomes for a given target and guess in the game.
#The created Lookup table is used in the solver codes for optimization purposes
#creates lookup.txt

def calculator(real_hash, guess):        #calculator function returns the result of comparison between a guess and a certain 

    guess_hash = []
    cows = 0
    bulls = 0

    for i in range(4):
        guess_hash.append(int((guess%(10**(i+1)))/10**i))

    guess_hash.reverse()
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

    return str(cows) + str(bulls)

lookup = [["" for _ in range(9000)] for _ in range(3000)]

for i in range(3000):
    rel = i + 7000
    rel_hash = []
    for k in range(4):
        rel_hash.append(int((rel%(10**(k+1)))/10**k))
    rel_hash.reverse()
    for j in range(0,9000):
        fel = j + 1000
        lookup[i][j] = calculator(rel_hash, fel)
        print("Lookup[",i+7000,"][",j+1000,"] =",lookup[i][j])

with open("lookup.txt", "a") as f:
    for row in lookup:
        f.write(" ".join(row) + "\n")



