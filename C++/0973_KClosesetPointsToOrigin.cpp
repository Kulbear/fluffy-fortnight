class Solution
{
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int K)
    {
        priority_queue<vector<int>, vector<vector<int>>, compare> pq;
        for (int i = 0; i < points.size(); ++i)
        {
            pq.push(points[i]);
            if (pq.size() > K)
                pq.pop();
        }
        vector<vector<int>> ans;
        while (!pq.empty())
        {
            ans.push_back(pq.top());
            pq.pop();
        }
        return ans;
    }

private:
    struct compare
    {
        bool operator()(vector<int> &p, vector<int> &q)
        {
            return p[0] * p[0] + p[1] * p[1] < q[0] * q[0] + q[1] * q[1];
        }
    };
};