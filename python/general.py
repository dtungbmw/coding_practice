
def printout(msg, doit=False):
    if doit is True:
        print(msg)

class Node():
    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value
#   8
#  5   10
# 3  7
class BinaryTree:
    node3 = Node(3, None, None)
    node7 = Node(7, None, None)
    node10 = Node(10, None, None)
    node5 = Node(5, node3, node7)
    node8 = Node(8, node5, node10 )
def search_binay_tree(node, val):
    if node is None:
        return None
    elif node.value == val:
        #print("val= "+str(val))
        return val
    else:
        x=search_binay_tree(node.left, val)
        if x is None:
            #print("search right..")
            x=search_binay_tree(node.right, val)
        #print("current val= " + str(node.value))
    return x
tree=BinaryTree()
res=search_binay_tree(tree.node8, 7)
#print("============= resut= "+str(res))
# Check it deviation between numbers
# What is the advantage of recursion?What is the advantage of recursion?
#array combination question.

def combin_lower_upper(lst, str_len):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            rest = combin_lower_upper(lst[0:i] + lst[i + 1:], str_len)
            for r in rest:
                for k in [lst[i].upper(), lst[i].lower()]:
                    l.append( [k]+r)
        return l

test =list('ab')
res=combin_lower_upper(test, len(test))
for i in res:
    printout(i, False)


class Mountain:
    start = -1
    end = -1
    def length(self):
        return self.end - self.start + 1
    def reset(self):
        self.start = -1
        self.end = -1
    def detected(self):
        return self.end != -1 and self.start != -1


# Python3 code for longest mountain subarray
# Function to find the
# longest mountain subarray
def LongestMountain(a):
        i = 0
        longest = 0
        m = Mountain()
        if (len(a) < 3):
            return 0
        for i in range(len(a) - 1):
            if (a[i + 1] > a[i]):
                if m.detected() is True: m.reset()
                if (m.start == -1): m.start = i
            elif (a[i + 1] < a[i]):
                    if (m.start != -1):
                        m.end = i + 1
                    if (m.end != -1 and m.start != -1):
                        if (longest < m.length()):
                            longest =  m.length()
            else:
                m.reset()
        if m.detected() is True:
            if (longest < m.length()):
                longest = m.length()

        return longest

        # Driver code

d = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]

printout(LongestMountain(d), True)

