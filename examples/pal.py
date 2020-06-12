
def expand_pal(s, left, right):
    while left >= 0 and right < len(s) \
            and s[left] == s[right]:
        left = left - 1
        right = right + 1
    return s[left + 1:right]

def lps(str):
    length = len(str) -1
    max_str = ""
    max_len = 0
    for i in range(length):
        for j in {i, i+1}:
            curr_str = expand_pal(str, i, j)
            curr_len = len(curr_str)
            if curr_len > max_len:
                max_len = curr_len
                max_str = curr_str
    return max_str


if __name__ == '__main__':
    str = "ABDCBCDBDCBBC"
    str="dfmom"
    print("lps is", lps(str))
