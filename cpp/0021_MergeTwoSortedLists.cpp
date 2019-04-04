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
    ListNode *mergeTwoListsIterative(ListNode *l1, ListNode *l2)
    {
        ListNode dummy(INT_MIN);
        ListNode *cur = &dummy;

        while (l1 && l2)
        {
            if (l1->val < l2->val)
            {
                cur->next = l1;
                l1 = l1->next;
            }
            else
            {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }

        cur->next = l1 ? l1 : l2;

        return dummy.next;
    }

    ListNode *mergeTwoListsRecursive(ListNode *l1, ListNode *l2)
{
        if (l1 == NULL || l2 == NULL)
        {
            return l1 ? l1 : l2;
        }

        if (l1->val < l2->val)
        {
            l1->next = mergeTwoListsRecursive(l1->next, l2);
            return l1;
        }
        else
        {
            l2->next = mergeTwoListsRecursive(l1, l2->next);
            return l2;
        }
    }
};