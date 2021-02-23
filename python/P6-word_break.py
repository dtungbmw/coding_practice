
#https://www.youtube.com/watch?v=YxtQUbKbdUs
#https://www.youtube.com/watch?v=oKxhj8JElGI
#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine
#if s can be segmented into a space-separated sequence of one or more dictionary words.

def isBreak():
    "here mem[idx] refer to if s[:idx+1] can be segmented into words"

    def recurse(idx, mem):
        if (idx) == len(s):
            return True
        if mem[idx] != 0:
            return mem[idx]
        for word in wordDict:
            "apple.. in [apple, pen]"
            if s[idx:idx + len(word)] == word:
                mem[idx] = True
                if recurse(idx + len(word), mem):
                    mem[idx + len(word)] = True
        return mem[len(s)]

    if not s:
        return False
    mem = [0] * (len(s) + 1)
    return recurse(0, mem)