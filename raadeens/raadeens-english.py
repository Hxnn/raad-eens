import random
import math
Round = 1  # You start at round 1 obv
Points = 0  # Max points is 20 but you start at 0
y = 'y'
while y == 'y' or y == 'Y':  # If you say either of those at the end, you get back here.
    x = random.randint(1, 1000)  # X is a random number between 1 and 1000.
    print("You have a maximum of 10 tries to guess the number! This is round:", Round)  # I had to show which round
    # you're on, so this shows that.

    count = 0  # How many times you've guessed.

    while count < math.log(1000 - 1 + 1, 2):  # While count is smaller than 10, add 1 and guess again.
        count += 1

        guess = int(input("Starts guessing! If you'd wish to stop playing, type either N or n."))
        if guess == "n" or guess == "N":  # So you can instantly stop playing or go on.
            break
# If you've guessed the random number, since x is the random number, you win. Also showcased how many tries it took
        # you, which round you're on and how many points you got since I also had to make a point system.
        if x == guess:
            print("Congratulations! You've guessed the number in ",
                  count, " tries!")
            Round = Round + 1
            Points = Points + 1
            print("You have", Points, " Points!")
            break
# If you either guessed too high or too low, it'll tell you but you can keep on playing. The ammount of guesses goes
        # up though. Since you got a max of 10 guesses. [which is "count" I think]
        elif x > guess:
            print("Too low! Try a bit higher! ")
        elif x < guess:
            print("Too high! Try a bit lower!")
    if count >= math.log(1000 - 1 + 1, 2):
        print("The number was %d" % x)
        Round = Round + 1
        print("You have", Points, " Points!")
    if Points == 20:
        break
    y = input("Would you like to play again? If so, write either Y or y. If you wish to stop playing, type either N "
              "or n. ")

# Here I had to ask if the player would like to play again or stop playing. Also had to display the points you have
# in total.
