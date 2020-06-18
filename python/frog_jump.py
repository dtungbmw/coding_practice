"""

11 feet

"""

import sys


def jump(accu, goal, counter):

  if accu  == goal:
    counter.append(1)
    return
  elif accu  > goal:
    return
  else:
    jump(accu + 1, goal, counter)
    jump(accu + 2, goal, counter)


if __name__ == '__main__':
  counter =[]
  c=jump(0, 7, counter)
  print("total path1= ", len(counter))


