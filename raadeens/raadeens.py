import random
import math
Ronde = 1
Punten = 0
y = 'y'
while y == 'y' or y == 'Y':
    x = random.randint(1, 1000)
    print("U hebt maximum 10 kansen om de nummer te raden! Dit is ronde:", Ronde)

    count = 0

    while count < math.log(1000 - 1 + 1, 2):
        count += 1

        guess = int(input("Begin met raden! Als u wilt stoppen met spelen, type dan N of n."))
        if guess == "n" or guess == "N":
            break
        if x == guess:
            print("Gefeliciteerd! U heeft de nummer in ",
                  count, " kansen geraden!")
            Ronde = Ronde + 1
            Punten = Punten + 1
            print("U heeft", Punten, " Punten!")
            break

        elif x > guess:
            print("Te laag! Probeer wat hoger! ")
        elif x < guess:
            print("Te hoog! Probeer wat lager!")
    if count >= math.log(1000 - 1 + 1, 2):
        print("De nummer was %d" % x)
        Ronde = Ronde + 1
        print("U heeft", Punten, " Punten!")
    if Punten == 20:
        break
    y = input("Wilt u opnieuw spelen! Type dan Y of y. Als u wilt stoppen, type dan N of n. ")
