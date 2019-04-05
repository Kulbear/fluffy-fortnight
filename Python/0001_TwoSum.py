class Solution:
    # Solution 1 - 1-Pass Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            if target - num in complements:
                return [complements[target - num], idx]
            complements[num] = idx

    # Solution 2 - 2-Pass Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            complements[num] = idx
        for idx, num in enumerate(nums):
            if target - num in complements:
                # for skipping itself
                if idx != complements[target - num]:
                    # CRITICAL: the order changed!
                    return [idx, complements[target - num]]

    # TODO: Solution 3 - Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
