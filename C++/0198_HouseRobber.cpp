class Solution
{
  public:
    int rob(vector<int> &nums)
    {
        int prev = 0, cur = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            int temp = cur;
            cur = max(prev + nums[i], cur);
            prev = temp;
        }

        return cur;
    }
};