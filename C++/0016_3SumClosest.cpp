class Solution
{
  public:
    int threeSumClosest(vector<int> &nums, int target)
    {

        int closest = nums[0] + nums[1] + nums[2];
        sort(nums.begin(), nums.end());

        // we need three pointers, one at start, one at end
        // and one does scanning in between
        for (int start = 0; start < nums.size() - 2; ++start)
        {
            if (start > 0 && nums[start] == nums[start - 1])
                continue;
            int mid = start + 1;
            int end = nums.size() - 1;
            while (mid < end)
            {
                int curSum = nums[start] + nums[mid] + nums[end];
                if (curSum == target) // sum is indeed target
                    return curSum;
                if (abs(target - curSum) < abs(target - closest))
                    // update closest if curSum is closer
                    closest = curSum;
                if (curSum > target) // shrink at end
                    --end;
                else // mid move to the next position
                    ++mid;
            }
        }
        return closest;
    }
};