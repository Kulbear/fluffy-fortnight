/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
  private:
    bool inbalanced = false;

    int dfs(TreeNode *node)
    {
        if (!node)
            return 0;
        int left = dfs(node->left);
        int right = dfs(node->right);
        if (abs(left - right) > 1)
            inbalanced = true;
        return max(left, right) + 1;
    }

  public:
    bool isBalanced(TreeNode *root)
    {
        if (!root)
            return !inbalanced;
        dfs(root);
        return !inbalanced;
    }
};
