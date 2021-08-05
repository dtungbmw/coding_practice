#Input: x = 123
#Output: 321

import sys


class Solution:
    def reverse(self, x: int) -> int:

        max = 2 ** 31 -1
        print(str(max))
        if abs(x) > max:
            return 0
        i = x
        if x < 0:
            i = -1 * x
        rev = 0
        while i != 0:
            j = i % 10

            i = int(i / 10)
            rev = rev * 10 + j
            # print ( str(i)+"; "+str(j)+"; "+str(rev))

        if x < 0:
            rev = -1 * rev
        return rev


s=Solution()
rev=s.reverse(1534236469)
print(str(rev))