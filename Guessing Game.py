import random

ch = True
co = True
chance = 3
while ch:
    rn = random.randint(0,10)
    
    print("\nGUESSING GAME")
    print("Guess a number in between 0 to 10\n")
    print("You got 3 chances ")
    
    while co:
        if chance == 0 :
            ch = False
            break
        
        n = int(input("Enter the guessed number "))

        if n == rn:
            print("Congo!!!.... You are very Lucky!!.. you have guessed the correct number")
            print("Want to continue playing? (y/n)")
            ch = input()
            if ch == 'n' or ch == 'N' :
                ch = False
                break
            else :
                break
        elif abs(rn-n) < 3 :
            print("Well guess....but it is wrong....you are very close to the correct answer")
            print("Want to continue guessing? (y/n)")
            co = input()
        elif abs(rn-n) < 5 :
            print("You are getting closer....Wanna continue guessing? (y/n)")
            co = input()
        else :
            print("Oopsy!!!... Wrong answer, Wanna guess again? (y/n)")
            co = input()

        if co == 'y' or co == 'Y' :
            chance -= 1
            print("\nYou got "+str(chance)+" chances left ")
            continue
        elif co == 'n' or co == 'N' :
            ch = False
            break

print("Thank you for playing...")
