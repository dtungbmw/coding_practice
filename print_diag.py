
# 3, 4, 5
# 5, 3, 2
#
#


class DiagLinkedBlock:
  next_row = 0
  next_column = 0
  row = 0
  column = 0
  value = -1
  def __init__(self, dim, row, column, value):
    self.row = row
    self.column = column
    self.value = value

    if self.row  == 0:
      if column == 0:
        self.next_row = 1
        self.next_column = 0
      else:
        self.next_row = column + 1
        self.next_column = row
        if self.next_row == dim:
          self.next_row = dim -1
          self.next_column = row +1

    elif column == (dim - 1) :
      self.next_row = column
      self.next_column = row + 1

    else:
      self.next_row = row - 1
      self.next_column = column + 1

  def next(self):
    return self.next_row, self.next_column

  def printit(self):
    print("[" + str(self.row) + ", " + str(self.column) + "]= "+ str(self.value))
    #print ("["+str(self.next_row)+", "+str(self.next_column)+"]")


if __name__ == '__main__':
    #n = int(input())

    m = [ [ 1,4 ,5, 19], [2,6,3,18], [9,0,7,15] , [11,8,12,13]]

    #DiagLinkedBlock(3, 1, 0).print()
    #print ("[0, 0]")
    dim = len(m)
    c = 0
    row =0
    column =0
    while c < dim * dim:
        block=DiagLinkedBlock(4, row, column, m[row][column])
        block.printit()
        row, column = block.next()
        c +=1

