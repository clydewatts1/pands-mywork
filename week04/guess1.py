import random as rnd

guess_no = rnd.randint(0,100)

i = guess_no + 1
print(f"No = {guess_no}")
while (i != guess_no):
    i = int(input("guess no: "))
    if i != guess_no:
        print("No correct")