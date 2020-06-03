
'''

0, 1, 1, 2, 3, 5, 8...

https://en.wikipedia.org/wiki/Fibonacci_number

'''

import time
import sys

def fib (n, cache):

  ret = cache.get(n, None)
  if ret != None:
    #print("c= "+str(n))
    return ret
  if n ==0 :
    ret = 0
  elif n <= 1 :
    ret = 1
  else:
    ret = fib(n-1, cache) + fib (n-2, cache)
  cache[n] = ret
  #print(cache)
  return ret


def fib_non_recursive(nterms):
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:

            nth = n1 + n2
            #print(nth)
            # update values
            n1 = n2
            n2 = nth
            count += 1
    return nth


if __name__ == '__main__':
    n = int(input())
    cache ={}
    #print("limit= " + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(sys.getrecursionlimit() * 5000)
    s = time.time()
    #print (fib(n, cache))
    e = time.time()
    #print("time= " + str((e - s)) + " s")
    s = time.time()
    print(fib_non_recursive(n-1))

    e = time.time()

    print("time= "+str((e-s))+" s")




'''
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       
       nth = n1 + n2
       print(nth)
       # update values
       n1 = n2
       n2 = nth
       count += 1
'''