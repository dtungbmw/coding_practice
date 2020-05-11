"""

11 feet

"""

import sys

class Path:
  path= []


def jump(level, total, inc,  path):
  if level == total:
    #print(str(level)+", "+str(total))
    path.append(level)
    path.append(-10000)
    return path
  elif level > total:
    path.append(-20000)
    return path
  else:
    #print(str(level) + ", " + str(total))
    path.append(level)
    p1=jump(level + inc, total, inc, path)
    p1.append(level)
    p2=jump(level + inc+1, total, inc, p1)

    return p2


    #jump(level+2, total, path)


if __name__ == '__main__':
  path_1 = jump(0, 5, 1, [])
  print("total path1= ", path_1)
  #path_2 = jump(0, 5, 2, [])
  #print("total path2= ", path_2)

  #print ("total path1= ", str(len(path_1)+len(path_2)) )

