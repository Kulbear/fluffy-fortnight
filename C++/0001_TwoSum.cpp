class Solution
{
  public:
    vector<int> twoSumOnePass(vector<int> &nums, int target)
    {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (seen.count(complement))
                return {seen[complement], i};
            seen[nums[i]] = i;
        }
        return {};
    }

    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++)
            seen[nums[i]] = i;

        for (int j = 0; j < nums.size(); j++)
        {
            int complement = target - nums[j];
            // use count as exact one solution is guranteed to be existed
            // avoid using the same element twice
            if (seen.count(complement) && seen[complement] != j)
                return {j, seen[complement]};
            else
                continue;
        }

        return {};
    }
};