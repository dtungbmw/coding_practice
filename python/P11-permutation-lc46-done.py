# LC 46
# https://www.youtube.com/watch?v=KukNnoN-SoY

answer=[]
class Solution:
    def permute(self, numList, result):
        if len(numList)==0:
            answer.append(result.copy())
            return
        for i in range(len(numList)):
            result.append(numList[i])
            new_numList = numList.copy()
            new_numList.remove(numList[i])
            self.permute(new_numList, result)
            result.pop()
        return

s = Solution()
numList=["a","4","b","m"]
result=[]
s.permute(numList, result)
print(answer)