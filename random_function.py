import random

#add 100 random numbers between -10 and 10
total = 0
for _ in range(100):
    total = total + random.randint(-10,10)
print(total)
