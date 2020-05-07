from primesieve import *
from collections import Counter
import time

start = time.time()


primes = primes(2**20)

primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]

def pdr(s):
    """take a number and return a list with families
    for example if the input number is 566003 then
    the result will be
    [[566003,566113,566223,566333,566443,566553,566663,566773,566883,566993],
    [500003,511003,522003,533003,544003,555003,566003,577003,588003,599003]]"""
    s = str(s)
    sol = []
    for duplicate in (Counter(s) - Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        sol.append(temp)
    return sol

# list to store all the checked numbers, so not to repeat
checked = []


def check(l):
    """take a list and remove all the values which are
    not prime numbers, finally return a list with only
    prime numbers"""
    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l

# condition for while loop
flag = True

# while loop iterator
i = 0

# while loop
while flag:
    # check if we have not check the number before
    if primes[i] not in checked:
        # find the family of the given number
        replacements = pdr(primes[i])
        for j in replacements:
            if len(check(j)) == 8:
                print(j[0])
                flag = False
                break
    i += 1

# time at the end of program execution
end = time.time()

# total time taken for execution
print(end - start)