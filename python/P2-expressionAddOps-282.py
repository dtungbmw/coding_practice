#https://www.youtube.com/watch?v=uhZeoivB7_4
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#Given a string that contains only digits 0-9 and a target value, return all possibilities to
# add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

from typing import List
class Solution:

    def helper(self, num, target, pos, eq, lastVal , currResult,  finalResult):
        print(eq)
        if len(num) == pos:
            if target != currResult:  # not matched
                return False
            else:
                finalResult.append(eq)

        else:
            for i in range(pos, len(num)):
                currVal=num[i]
                curr = int(num[i])
                canDo=True
                if len(eq) >0:
                    print('help2')
                    cnaDo=self.helper(num, target, pos + 1,
                                eq= eq+'+'+currVal, lastVal=currVal ,
                                currResult=currResult+curr, finalResult=finalResult)
                    canDo=self.helper(num, target, pos + 1,
                                eq=eq + '-' + currVal, lastVal=currVal,
                                currResult=currResult - curr, finalResult=finalResult)

                else:
                    print('help1')
                    canDo=self.helper(num, target,  pos +1, eq= currVal, lastVal=currVal , currResult=curr , finalResult=finalResult)

                if canDo is False:
                    return False

    def addOperators(self, num: str, target: int) -> List[str]:

        pos=0
        eq=""
        currResult=0
        finalResult : List[str] =[]
        lastVal=None
        self.helper(num, target,pos, eq, lastVal, currResult, finalResult)
        return finalResult


s=Solution()
result:List[str]=s.addOperators("124", 3)

print(result)




