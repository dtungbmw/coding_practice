# class Node():
#     def __init__(self, value, left, right):
#         self.left = left
#         self.right = right
#         self.value = value
#


# input  = [[1, 6], [8, 10], [15, 18]]
#
# def sort_algo( item):
#     return item[0]
#
# def merge ( timelist):
#
#     sorted=timelist.sort(key = sort_algo)
#     result = []
#     meged = False
#     counter
#     for i in sorted:
#         if counter == len(sorted)-1:
#             return
#         if sorted[i][1] > sorted[i+1][0]:
#             if sorted[i][1] > sorted[i+1][1]:
#                 result.append([sorted[i][0], sorted[i][1]])
#             else:
#                 result.append([sorted[i][0], sorted[i+1][1]])
#             merged == True
#         else:
#             result.apped(i)
#         counter +=1
#     return merged, result
#
# m = input
# is_merged=True
# while is_merged==True:
#     is_merged, m = merged(m)


class Node:
    right = None
    left = None
    value = None

## https://www.youtube.com/watch?v=0Zsabo7ires

def dfs(node, target):
    stack = []
    count = 0
    stack.append(node)
    while len(stack) > 0:
        n = stack.pop()
        print(n.value)
        if target == n.value:
            count += 1
        if n.right is not None:
            stack.append(n.right)
        if n.left is not None:
            stack.append(n.left)
    return count

##   a
##  b d
#  c
a=Node()
c=Node()
d=Node()
b=Node()
a.left = b
a.value =1
b.value =2
c.value = 4
d.value = 4

a.right = d
b.left = c

searchFor = 4
count=dfs(a, searchFor)

print("count of "+str(searchFor)+" = " + str(count))

#######

graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

visited = []