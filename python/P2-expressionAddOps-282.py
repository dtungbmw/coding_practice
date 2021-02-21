#https://www.youtube.com/watch?v=uhZeoivB7_4
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#Given a string that contains only digits 0-9 and a target value, return all possibilities to
# add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

from typing import List
class Solution:
    result = List[str]
    def addOperators(self, num: str, target: int, temp) -> List[str]:
        if len(num)==1 and target != int(num[0]):
            return None
        else:
            self.result.append(temp)
        for i in range(len(num)):
            temp=""
            if self.addOperators(num[i:-1], target - int(num[i]), temp) is not None:
                temp=num[i]+ '+'+ temp
        return self.result

s=Solution()
result=s.addOperators("123", 6,[])
print(result)


