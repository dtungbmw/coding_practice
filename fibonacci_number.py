
'''

0, 1, 1, 2, 3, 5, 8...

https://en.wikipedia.org/wiki/Fibonacci_number

'''

import time

def fib (n, cache):

  ret = cache.get(n, None)
  if ret != None:
    print("c= "+str(n))
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


def fib_non_recursive(n):
  # TODO
  return


if __name__ == '__main__':
    n = int(input())
    cache ={}

    s = time.time()
    print (fib(n, cache))
    e = time.time()

    print("time= "+str(e-s))





