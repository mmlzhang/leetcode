class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        i, flag = 0, -1

        result = ""

        for c in s:
            result += c

            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(result)
