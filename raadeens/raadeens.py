import random
import math
Ronde = 1
Punten = 19
y = 'y'
while y == 'y' or y == 'Y':
    x = random.randint(1, 1000)
    print("Je hebt maximaal 10 kansen om de getal te raden per ronde! Dit is ronde:", Ronde)

    count = 0

    while count < math.log(1000 - 1 + 1, 2):
        count += 1

        guess = int(input("Begin met raden! Als u wilt stoppen met spelen type dan N of n: "))
        if guess == "n" or guess == "N":
            break
        if x == guess:
            print("Gefeliciteerd! Je hebt het in ",
                  count, " kansen gedaan!")
            Ronde = Ronde + 1
            Punten = Punten + 1
            print("Je hebt", Punten, " Punten!")
            break

        elif x > guess:
            print("Te laag! Probeer het nog een keer! ")
        elif x < guess:
            print("Te hoog! Probeer het nog een keer!")
    if count >= math.log(1000 - 1 + 1, 2):
        print("Het getal was %d" % x)
        Ronde = Ronde + 1
        print("Je hebt", Punten, " Punten!")
    if Punten == 20:
        break
    y = input("Wil je nog een keer spelen? Type dan y of Y. Als u wilt stoppen, type dan N of n: ")

