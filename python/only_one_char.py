



input = [('A', 'D'), ('B', 'E'), ('F', 'G'), ('D', 'P') ,('P', 'O'), ('L', 'A')]

s1 = set()
s2 = set()
m1 = dict()
m2 = dict()

for item in input:
    s1.add(item[0])
    s2.add(item[1])
    m1[item[0]]= item[1]
    m2[item[1]] = item[0]

def cleanData(ch, m, s):
    related = m.get(ch)
    if related in s:
        s.remove(related)

def isValid(string):
    for s in string:
        if s in s1:
            cleanData(s, m1, s1)
        elif s in s2:
            cleanData(s, m2, s2)
        else:
            print("fail")
            return
    print("pass")

isValid("APPLE")