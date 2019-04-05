class Solution:
    # Solution 1 - DFS
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if not nums:
                output.append(path)
                # backtracking
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        output = []
        dfs(nums, [])
        return output

    # Solution 2 - Backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            # if we are at the end of the list
            if start == length:
                output.append(nums[:])  # use [:] to do a quick shallow copy
            for i in range(start, length):
                # swap the first and the i-th item
                nums[start], nums[i] = nums[i], nums[start]

                backtrack(start + 1)

                # backtrack (restore to the previous state)
                nums[start], nums[i] = nums[i], nums[start]

        length = len(nums)
        output = []
        backtrack(0)

        return output
