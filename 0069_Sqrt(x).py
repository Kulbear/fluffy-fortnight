class Solution:
    # Solution 1 - Binary Search
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            # CRITICAL: don't forget to add 1 on the left side
            # we still need the r = mid to check later
            elif mid ** 2 >= x:
                r = mid
            else:
                l = mid + 1
