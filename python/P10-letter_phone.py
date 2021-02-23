# Letter Combinations of a Phone Number  
# https://www.youtube.com/watch?v=h6FmiyYDjmk&t=1227s
# https://www.youtube.com/watch?v=TeF2nHDnObI (python)
# 地界：你的熱情與世界的需要相遇的地方


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        L = len(digits)
        mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def dfs(word, idx):
            if idx == L:
                output.append(word)
            else:
                for c in mp[digits[idx]]:
                    dfs(word + c, idx + 1)
        if L != 0:
            dfs("", 0)
        return output


