class Solution
{
  public:
    bool isValidSerialization(string preorder)
    {
        int cap = 1;
        preorder += ",";
        for (int i = 0; i < preorder.size(); ++i)
        {
            if (preorder[i] != ',')  // skip commas
                continue;
            if (--cap < 0)  // if no capacity left, fail
                return false;
            if (preorder[i - 1] != '#') // last node is not null
                cap += 2;
        }

        return cap == 0;
    }
};