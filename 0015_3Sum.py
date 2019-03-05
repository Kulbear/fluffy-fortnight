class Solution:
    # Solution 1 - Reduce to Two Sum by Sorting
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            # condition 1: nums[i] > 0 and nums is sorted
            # all elements on the right side of nums[i] will be > 0
            # impossible to have sum equal to 0 then
            if nums[i] > 0:
                break

            # condition 2: nums[i - 1] == nums[i] and nums is sorted
            # avoid duplicated triplets
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # condition 3: sum is smaller than 0
                # we need to find a larger nums[l]
                if s < 0:
                    l += 1
                # condition 4: sum is greater than 0
                # we need to find a smaller nums[r]
                elif s > 0:
                    r -= 1
                # condition 5: a triplet is found
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # skip duplicated values
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # skip duplicated values
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return ans
