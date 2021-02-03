
class Cell:
    x = 0;
    y =0;
    val = -1;
    visited = False

    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def equal(self, other):
        return self.x==other.x && self.y==other.y;

    def print(self):
        print("==")
        print (str(x))
        print (str(y))
        print (str(val))
        print (str(visited))

    def inc_x(self):
        self.x = self.x +1;
        return self

    def inc_y(self):
        self.y = self.y + 1;
        return self

class Matrix :
    def __init__(self, m, n):
        self.m = m
        self.n =n
        map

    def add_cell (cell):



def unique_path(curr, end):

    if curr.equal(end):
        return

    if curr.visited is True:
        print (" visited")

    if curr.visited is False:
        # explore further
        curr.print
        unique_path(curr.inc_x(), end )
        unique_path(curr.inc_y(), end)
        unique_path(curr.inc_x().inc_y(), end)

###   11, 14, 16
##    34, 36, 59
##    53, 54, 55



end_cell = new Cell(2, 2, 55)
