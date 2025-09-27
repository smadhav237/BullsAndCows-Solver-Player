#General Purpose Solver. Provides optimal guesses and range of answers based on information received from previous guesses/results.
#needs lookup.txt to run

import math #importing math for log functions, random for generating random numbers
import random

print(random.randint(1000,10000))

lookup = []
with open('lookup.txt', 'r') as file:
    
    for line in file:
        row = line.strip().split()  
        lookup.append(row)

rangi = []
for i in range(1000,10000):              #generating the initial guess range
    rangi.append(i)

def lookitup(real, guess):
    return lookup[real - 1000][guess - 1000]

def distributor(pros, ranges):
    
    distribution = {"00": 0, "10": 0, "20": 0, "30": 0, "40": 0,
                "01": 0, "11": 0, "21": 0, "31": 0,
                "02": 0, "12": 0, "22": 0,
                "03": 0, "13": 0,
                "04": 0}
    tags = {0: "00", 1: "10", 2: "20", 3: "30", 4: "40",
            5: "01", 6: "11", 7: "21", 8: "31",
            9: "02", 10: "12", 11: "22",
            12: "03", 13: "13",
            14: "04"}
    
    for i in ranges:
        distribution[lookitup(pros, i)] = distribution[lookitup(pros, i)] + 1

    entropy = 0
    for j in range(15):
        if distribution[tags[j]]:
            entropy = entropy + (distribution[tags[j]]/len(ranges))*math.log(len(ranges)/distribution[tags[j]], 2)

    return entropy
        
def best_guess(rangi):
    max_entropy = 0  
    guess = 0   
    for j in rangi:
        ent = distributor(j, rangi)
        if ent > max_entropy:
            max_entropy = ent
            guess = j

    return guess

def ranger(guess, result, rangi):
    new_rangi = []
    for i in rangi:
        if lookitup(i, guess) == result:
            new_rangi.append(i)
    
    return new_rangi

def player(rangi):
    print("Suggested First Guess: 1223")
    guess = int(input("Enter your First Guess: "))
    for tries in range(100):
        result = input("Enter the Result: ")
        if result == "04":
            print("Finished with ", tries + 1)
            break
        else:
            print("Guess: ",guess, "Result: ", result[0], "Cows", result[1], "Bulls")
            rangi = ranger(guess, result, rangi)
            if len(rangi) == 1:
                guess = rangi[0]
            else:
                guess = best_guess(rangi)
            print(rangi)
            print("Suggested next guess: ", guess)
            guess = int(input("Enter your Guess: "))
            print("Tries: ", tries + 1, "Next Guess: ", guess)
            

    return tries + 1

player(rangi)











        


    
