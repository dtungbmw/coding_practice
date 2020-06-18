# 3, 4, 5
# 5, 3, 2
#
#

if __name__ == '__main__':
    #n = int(input())
    m = [[1, 4, 5, 19],
         [2, 6, 3, -18],
         [9, 0, -7, 15] ,
         [11,-8, 12,13]]
    backup = []
    dim = len(m)
    for row in range (dim):
        for column in range(dim):
            if row-column < 0:
                backup.append([dim+(row-column), column])
                continue
            print (m[row-column][column])
    #print("*"*20)
    for elm in backup:
        print(m[elm[0]][elm[1]])

