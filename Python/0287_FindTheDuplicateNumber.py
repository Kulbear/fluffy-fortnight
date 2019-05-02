class Solution:
    # Solution 1 - Binary Search
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            count = 0
            mid = low + (high - low) // 2
            for num in nums:
                count += 1 if num <= mid else 0
            if count > mid:
                high = mid - 1
            else:
                low = mid + 1

        return low
