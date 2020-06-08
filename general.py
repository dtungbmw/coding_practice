
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
    print(i)