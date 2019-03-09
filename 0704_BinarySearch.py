class Solution:
    # Solution 1 - Recursive
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, target, start, end):
            # CRITICAL: this covers the case that nums has only one element inside
            if start <= end:
                # this may have the overflow issue in languages like Java or C++
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    # we know mid is larger, can ignore it in the next call
                    return helper(nums, target, start, mid - 1)
                else:
                    return helper(nums, target, mid + 1, end)
            return -1

        return helper(nums, target, 0, len(nums) - 1)

    # Solution 2 - Iterative
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        # CRITICAL: this covers the case that nums has only one element inside
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # we know mid is larger, can ignore it in the next iteration
                end = mid - 1
            else:
                start = mid + 1
        return -1
