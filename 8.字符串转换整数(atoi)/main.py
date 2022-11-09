

class Solution:

    def myAtoi(self, s: str) -> str:
        s = s.lstrip()
        multi = 1
        if not s:
            return 0
        if s[0] == "-":
            multi = -1
            s = s[1:]
        elif s[0] == "+":
            multi = 1
            s = s[1:]

        max_v = 2 ** 31 - 1
        min_v = -(2**31)

        res = 0
        for w in s:
            if w.isdigit():
                print("-->>: ", res)
                res = res * 10 + int(w)
                if res >= max_v and multi == 1:
                    return max_v
                if res >= -min_v and multi == -1:
                    return min_v
            else:
                return res * multi

        return res * multi


if __name__ == "__main__":

    for n in [
        "sdfsa sdfa 56723 dsad",
        "  -42",
        '  4  5 ',
        "-91283472332"
    ]:

        r = Solution().myAtoi(n)
        print(r, type(r))
