

#https://github.com/tresloukadu/hackerRank-workschedule-avaliation

class Context :
    workHours=0
    dayHours=0
    pattern=""
    remainder=0
    table = []
    def prinTimeTbl(self):
        for item in self.table:
            print(item, end="")
        print("", end="\n")


def calRemainder(context):
    total  =0
    pattern = context.pattern
    for p in pattern:
        if p != '?':
            total = total + int(p)
    context.remainder = context.workHours - total


def timeTable(context, idx, variation):

    if idx == len(context.pattern)-1:
        if variation==0 :
            context.prinTimeTbl()
        return
    if context.table[idx] == '?':
        for p in range(context.dayHours+1):
            tmp=context.table[idx]
            context.table[idx]=p
            timeTable(context, idx+1, variation - p)
            context.table[idx]=tmp
    else:
        timeTable(context, idx + 1, variation)



def findSchedule(context):
    variation = context.remainder
    timeTable( context, 0, variation)

c=Context()
c.pattern="08??840"
c.dayHours = 8
c.workHours = 24
for p in c.pattern:
    c.table.append(p)

calRemainder(c)
findSchedule(c)




