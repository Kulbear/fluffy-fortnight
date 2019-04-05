struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
  public:
    bool isValidBST(TreeNode *root)
    {
        prev_ = nullptr;
        return inOrder(root);
    }

    bool isValidBSTRecursive(TreeNode *root)
    {
        long long min = LLONG_MIN, max = LLONG_MAX;
        return isValidBSTHelper(root, min, max);
    }

    bool isValidBSTIterative(TreeNode *root)
    {
        if (!root)
            return true;

        stack<vector<TreeNode *>> s;
        s.push({root, NULL, NULL});

        while (s.size())
        {
            vector<TreeNode *> v = s.top();
            s.pop();
            TreeNode *cur = v[0], *min = v[1], *max = v[2];
            if ((min && cur->val <= min->val) || (max && cur->val >= max->val))
                return false;

            if (cur->left)
                s.push({cur->left, min, cur});
            if (cur->right)
                s.push({cur->right, cur, max});
        }

        return true;
    }

  private:
    TreeNode *prev_;

    bool inOrder(TreeNode *root)
    {
        if (!root)
            return true;
        if (!inOrder(root->left))
            return false;
        if (prev_ && root->val <= prev_->val)
            return false;
        prev_ = root;
        return inOrder(root->right);
    }

    bool isValidBSTHelper(TreeNode *root, long long min, long long max)
    {
        if (!root)
            return true;

        if (root->val >= max || root->val <= min)
            return false;

        return isValidBSTHelper(root->left, min, root->val) &&
               isValidBSTHelper(root->right, root->val, max);
    }
}
