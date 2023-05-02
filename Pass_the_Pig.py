print("Welcome to Pass the Pig!")
print("------------------------")
print("\n")

import random

score_p1 = 0
score_p2 = 0

while score_p1 < 100 and score_p2 < 100:
    role1 = random.randint(0, 9)
    role2 = random.randint(0, 9)

    def player1():

        global score_p1


        if role1 == 0:
            print("Pig Out - 0 pts!")
            score_p1 = 0;
            print(f"Player 1:  {score_p1} | Player 2: {score_p2}")
            print("\n")
        elif role1 == 1:
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
 

    roller1 = input("Ready to role Player 1? (y) ")

    while roller1 != "y":
        roller1 = input("Error. Please re-enter: ")


    if roller1 == "y":
        print("-------------------------------")
        player1() 

        if score_p1 >= 100:
            print("Player 1 Wins!")
            print("--------------")
            break
        elif score_p2 >= 100:
            print("Player 2 Wins!")
            print("--------------")
            break



    roller2 = input("Ready to role Player 2? (y) ")

    while roller2 != "y":
        roller2 = input("Error. Please re-enter: ")

    if roller2 == "y":
        print("-------------------------------")
        player2()

        if score_p1 >= 100:
            print("Player 1 Wins!")
            print("--------------")
            break
        elif score_p2 >= 100:
            print("Player 2 Wins!")
            print("--------------")
            break



