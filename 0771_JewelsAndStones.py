from collections import Counter


class Solution:
    # Solution 1 - Hash Table
    def numJewelsInStones(self, J: str, S: str) -> int:
        set_J = set(J)
        ct = Counter(list(S))
        num = 0
        for char in ct:
            if char in set_J:
                num += ct[char]

        return num
