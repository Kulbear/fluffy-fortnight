class Solution:
    # Solution 1 - DFS Recursion
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path=[]):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        res = []
        nums.sort()
        dfs(0)
        return res
