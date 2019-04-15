/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
  public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode d(0);
        d.next = head;
        ListNode *slow = &d;
        ListNode *fast = &d;

        for (int i = 0; i < n; ++i)
            fast = fast->next;

        while (fast->next)
        {
            slow = slow->next;
            fast = fast->next;
        }

        slow->next = slow->next->next;

        return d.next;
    }
};