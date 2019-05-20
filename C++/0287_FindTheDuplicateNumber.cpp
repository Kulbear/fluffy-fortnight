class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        while (low <= high) {
            int count = 0;
            int mid = low + (high - low) / 2;
            for (int i = 0; i < nums.size(); ++i) 
                count += nums[i] <= mid ? 1 : 0;
            if (count > mid) 
                high = mid - 1;
            else
                low = mid + 1;
        }
        return low;
    }
};