import random

while 


picks = int(input("How many quick picks? "))
quick_picks = [[random.sample(range(45), 6)] for i in range(0, picks)]
print(quick_picks)

for n in quick_picks:
    for i in n:
        for x in i:
            print(x, end=' ')