class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for c in num:
            while res and k and res[-1] > c:
                res.pop()
                k -= 1
            if c != '0' or (c == '0' and res):
                res.append(c)

        while res and k:
            res.pop()
            k -= 1

        return ''.join(res) if res else '0'
