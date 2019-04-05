class Solution:
    # Solution 1 - Recursion
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(start, end):
            if start >= end:
                return

            s[start], s[end] = s[end], s[start]
            reverse(start + 1, end - 1)

        if len(s) < 2:
            return

        start = 0
        end = len(s) - 1
        reverse(start, end)
