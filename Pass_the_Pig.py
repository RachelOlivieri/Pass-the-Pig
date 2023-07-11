print("Welcome to Pass the Pig!")
print("------------------------")
print('Press "y" to role the') 
print('pigs and "n" to pass')
print("\n")
# Displays the basic rules of the game

import random

score_p1 = 0
score_p2 = 0

round = "y"

# While loop that goes through the game as long as the variable 'round' = "y"
while round == "y":

    # Another while loop that keeps the game running as long as the scores are bellow 100
    while score_p1 < 100 and score_p2 < 100:
        # Calls the random module twice to generate a random number from 0-9
        roll1 = random.randint(0, 9)
        roll2 = random.randint(0, 9)

        # Defines a function for the 1st player that takes roll1 and prints
        # a message describing the the result of the role. It also updates
        # the global variable 'Score_p1' with the appropriate num of pts 
        def player1():

            global score_p1


            if roll1 == 0:
                print("Pig Out - 0 pts!")
                score_p1 = 0;
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif roll1 == 1:
                print("Sider - 1 pt!") 
                score_p1 += 1
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 2:
                print("Trotter - 5 pts!")
                score_p1 += 5
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 3:
                print("Double Trotter - 20 pts!")
                score_p1 += 20
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 4:
                print("Razorback - 5 pts!")
                score_p1 += 5
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 5:
                print("Double Razorback - 20 pts!")
                score_p1 += 20
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 6:
                print("Snouter - 10 pts!")
                score_p1 += 10
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 7:
                print("Double Snouter - 40 pts!")
                score_p1 += 40
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 8:
                print("Leaning Jowler - 15 pts!")
                score_p1 += 15
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role1 == 9:
                print("Double Leaning Jowlers - 60 pts!")
                score_p1 += 60
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
 
        # Defines a function for the 2nd player that takes roll1 and prints
        # a message describing the the result of the role. It also updates
        # the global variable 'Score_p2' with the appropriate num of pts 
        def player2():
        
            global score_p2

            if role2 == 0:
                print("Pig Out - 0 pts!")
                score_p2 = 0;
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 1:
                print("Sider - 1 pt!") 
                score_p2 += 1
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 2:
                print("Trotter - 5 pts!")
                score_p2 += 5
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 3:
                print("Double Trotter - 20 pts!")
                score_p2 += 20
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 4:
                print("Razorback - 5 pts!")
                score_p2 += 5
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 5:
                print("Double Razorback - 20 pts!")
                score_p2 += 20
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 6:
                print("Snouter - 10 pts!")
                score_p2 += 10
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 7:
                print("Double Snouter - 40 pts!")
                score_p2 += 40
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 8:
                print("Leaning Jowler - 15 pts!")
                score_p2 += 15
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
            elif role2 == 9:
                print("Double Leaning Jowlers - 60 pts!")
                score_p2 += 60
                print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
                print("\n")
 

        roller1 = input("Ready to role Player 1? (y/n) ")

        # User input validation for the 1at player
        while roller1 not in ["y", "n"]:
            roller1 = input("Error. Please re-enter: ")

        # Conditional statement that checks the value of the 'roller1' variable.
        # What the user enters determines which part of the code runs 
        if roller1 == "n":
            print("Pass!") 
            print("\n")
        elif roller1 == "y":
            print("-------------------------------")
            player1() 

            if score_p1 >= 100:
                print("Player 1 Wins!")
                print("--------------")
                round = input("Do you want to play again? (y/n)")
                if round == "n":
                    break
                elif round == "y":
                    score_p1 = 0
                    score_p2 = 0
            elif score_p2 >= 100:
                print("Player 2 Wins!")
                print("--------------")
                round = input("Do you want to play again? (y/n)")
                if round == "n":
                    break
                elif round == "y":
                    score_p1 = 0
                    score_p2 = 0

        roller2 = input("Ready to role Player 2? (y/n) ")
 
        # User input validation for the 2nd player
        while roller2 not in ["y", "n"]:
            roller2 = input("Error. Please re-enter: ")

        # Conditional statement that checks the value of the 'roller2' variable.
        # What the user enters determines which part of the code runs 
        if roller2 == "n":
            print("Pass!")
            print("\n")
        elif roller2 == "y":
            print("-------------------------------")
            player2()

            if score_p1 >= 100:
                print("Player 1 Wins!")
                print("--------------")
                round = input("Do you want to play again? (y/n)")
                if round == "n":
                    break
                elif round == "y":
                    score_p1 = 0
                    score_p2 = 0
            elif score_p2 >= 100:
                print("Player 2 Wins!")
                print("--------------")
                round = input("Do you want to play again? (y/n)")
                if round == "n":
                    break
                elif round == "y":
                    score_p1 = 0
                    score_p2 = 0

