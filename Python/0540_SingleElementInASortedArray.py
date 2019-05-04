class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 0:
                n = m + 1
            else:
                n = m - 1

            if nums[n] == nums[m]:
                l = m + 1
            else:
                r = m

        return nums[l]
