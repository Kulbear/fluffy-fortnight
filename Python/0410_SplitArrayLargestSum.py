class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def min_groups(limit):
            sum = 0
            groups = 1
            for num in nums:
                if (sum + num) > limit:
                    sum = num
                    groups += 1
                else:
                    sum += num
            return groups

        left = max(nums)
        right = sum(nums) + 1
        while left < right:
            limit = (left + right) // 2
            if min_groups(limit) > m:
                left = limit + 1
            else:
                right = limit
        return left
