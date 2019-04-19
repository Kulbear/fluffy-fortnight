class Solution
{
  public:
    int trap(vector<int> &height)
    {
        int ans = 0;
        for (int i = 0; i < height.size(); ++i)
        {
            int left = 0, right = 0;
            for (int j = i; j >= 0; --j)
                left = max(left, height[j]);
            for (int h = i; h < height.size(); ++h)
                right = max(right, height[h]);

            ans += min(left, right) - height[i];
        }
        return ans;
    }
};