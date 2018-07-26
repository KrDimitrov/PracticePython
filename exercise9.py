import random

g = 0
ri = random.randint(1, 9)
while True:
    _input = input("Enter Number or Exit: ")
    if _input == "exit" or '':
        break
    _input = int(_input)
    if _input < ri:
        print("Too low!\n")
        g+=1
    if _input > ri:
        print("Too high!\n")
        g+=1
    if _input == ri:
        print("You guessed Right!!!\n")
        ri = random.randint(1, 9)
        print("New number generated!\n")

print("You tried " + str(g) + " times to guess!")

