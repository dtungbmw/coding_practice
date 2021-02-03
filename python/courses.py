

##
## num_course , courses=[ [1,0], [2,1]]
##


def canComplete(num, courses):
    visited = [False] * num
    deplist = [None] * num

    for i in range(num):
        deplist[i] = []

    for course in courses:
        deplist[course[0]].append(course[1])
    print("depel= " + str(deplist))
    print("visited= " + str(visited))
    for i in range(num):
        if not visited[i]:
            if isCycle(i, visited, deplist):
                print (str(i)+", "+str(visited))
                return False
    return True


def isCycle(i, visited, deplist):

    if len(deplist[i]) == 0:
        return False
    visited[i] = True
    for j in deplist[i]:
        if visited[j] is True or isCycle(j, visited, deplist) is True:
            return True
    visited[i] = False
    return False



test = canComplete(4, [[1,0],[0,3],[1,2],[2,3]])

print (str(test))



