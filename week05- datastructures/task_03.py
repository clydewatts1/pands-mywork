#Create a program that puts 10 random numbers into a queue(list), the
#program should then output all the values in the queue, then take the
#numbers from the queue one at a time, print it and the current numbers still
#in the queue. (the command pop(0) takes the first element out of a list)

import random as rnd

queue = []
for i in range(10):
    queue.append(rnd.randint(0, 100))

while len(queue) > 0:
    for i in queue:
        print(i, end=" ")
    print()
    # pop the first element from the list
    queue.pop(0)
