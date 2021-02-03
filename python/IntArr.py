


def intArr( currVal, nextVal, currResult, preOp, nextOp):

    result = currResult
    if nextOp == '+':
        result = currResult + nextVal
    elif nextOp == '-':
        result = currResult - nextVal
    elif nextOp == '*':
        print ("todo")

    return result


arr = [ 1,2, 3]


for a in arr:
    result = intArr(1, 2, 3, '+', None, +)