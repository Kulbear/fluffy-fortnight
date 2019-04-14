class Solution
{
  public:
    vector<string> letterCombinations(string digits)
    {
        vector<string> result;
        if (!digits.size())
            return result;
        string mapping[10] = {"0", "1", "abc", "def", "ghi",
                              "jkl", "mno", "pqrs", "tuv", "wxyz"};
        result.push_back("");
        for (int i = 0; i < digits.size(); i++)
        {
            vector<string> temp;
            string candidates = mapping[digits[i] - '0'];
            for (int i = 0; i < candidates.size(); ++i)
                for (int j = 0; j < result.size(); ++j)
                    temp.push_back(result[j] + candidates[i]);
            result = temp;
        }
        return result;
    }
};