import random

def birthday_simulation_standard():
    print("Note that this simulation is not representative of real-life scenarios and utilizes the naive definition of probability, where each day has an equal chances of selection.")
    print("This version omits February 29th as a day in the year.")
    n = int(input("How many people are going to be in a room? ")) # number of people in a room.
    people = [random.randint(1,365) for _ in range(n)] # generates a random list of n people's birthday, with replacement. each number from 1 to 365 represent a day of the year, without considering leap years.
    match = False

    for i in range(0,n):
        for j in range (i+1, n):
            if (people[i] == people[j]):
                match = True
                break
    
    if match == True:
        print("There is a match of at least one birthday match out of " + str(n) + " people!")

    else:
        print("There is unfortunately not a match out of " + str(n) + " people.")

def birthday_simulation_leap_year():
    print("Note that this simulation is not representative of real-life scenarios and utilizes the naive definition of probability, where each day has an equal chances of selection.")
    print("This version considers leap year scenarios with February 29th as an equally likely day.")
    n = int(input("How many people are going to be in a room? ")) # number of people in a room.
    people = [random.randint(1,366) for _ in range(n)] # generates a random list of n people's birthday, with replacement. each number from 1 to 366 represent a day of the year, considering leap years.
    match = False

    for i in range(0,n):
        for j in range (i+1, n):
            if (people[i] == people[j]):
                match = True
                break
    
    if match == True:
        print("There is a match of at least one birthday match out of " + str(n) + " people!")

    else:
        print("There is unfortunately not a match out of " + str(n) + " people.")

def match_probability_leapYr():
    num_of_people = int(input("How many people do you want in the room to see the probability of a pair? "))
    probability_no_match_numerator = 1 # to be calculated
    for i in range(366-num_of_people+1, 367):
        probability_no_match_numerator *= i
    
    probability_match = 1 - (probability_no_match_numerator / 366 ** num_of_people)

    print("For " + str(num_of_people) + ", the naive probability of at least one match is " + str(probability_match * 100) + "%!")

def match_probability_standard():
    num_of_people = int(input("How many people do you want in the room to see the probability of a pair? "))
    probability_no_match_numerator = 1 # to be calculated
    for i in range(365-num_of_people+1, 366):
        probability_no_match_numerator *= i
    
    probability_match = 1 - (probability_no_match_numerator / 365 ** num_of_people)

    print("For " + str(num_of_people) + ", the naive probability of at least one match is " + str(probability_match * 100) + "%!")