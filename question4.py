#2520 is the smallest number that can be divided by each of
#the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible
#by all of the numbers from 1 to 20?

def MasterMultiple(n):
    for x in range(1, 21):
        if n % x != 0:
            return False
    return True

number = 2520

while True:
    number += 1
    if MasterMultiple(number):
        print(number)
        break
