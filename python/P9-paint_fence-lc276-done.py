# https://algorithmexplorer.medium.com/leetcode-problem-276-paint-fence-12e95234d6c

#https://algorithmexplorer.medium.com/leetcode-problem-276-paint-fence-12e95234d6c

#The problem states that there are ’n’ fences which can be coloured with
#  one of the ‘k’ colours in such a way that not more than two adjacent fences have the same colour.

def wayToColor(numFences, numColors):
    if numFences ==0:
        return 0
    if numFences ==1:
        return numColors
    same = numColors
    diff = numColors * (numColors -1)
    if numFences ==2:
        return same+diff
    prev_same, prev_diff = same, diff
    for i in range (3, numColors):
        same = prev_diff
        diff = (prev_same+prev_diff) * (numColors -1)
        prev_same, prev_diff = same, diff
    return same+diff

n = wayToColor(2, 3)
print(str(n))



