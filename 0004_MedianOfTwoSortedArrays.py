class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        # we assume n1 <= n2
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        # k is the middle idx if we merge the two lists, say it is L
        k = (n1 + n2 + 1) // 2

        # the idea behind is that, we only do binary search on the shorter list
        l = 0
        r = n1

        while l < r:
            # we need m1 elements from nums1 to make the first half of L
            m1 = (l + r) // 2
            # therefore only m2 = k - m1 elements from nums2 are needed to make the first half of L
            m2 = k - m1
            # nums1[m1] < nums2[m2 - 1] means we need more from nums1
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            # otherwise we need less elements from nums1 (more from nums2)
            else:
                r = m1

        m1 = l
        m2 = k - l

        # handling the case that m1 or m2 can be 0
        # which means the elements in one of the lists are all smaller or greater than all elements in another list
        c1 = max(nums1[m1 - 1] if m1 > 0 else -float('inf'),
                 nums2[m2 - 1] if m2 > 0 else -float('inf'))

        # odd elements in the two lists
        if (n1 + n2) % 2:
            return c1

        # even elements in the two lists
        c2 = min(nums1[m1] if m1 < n1 else float('inf'),
                 nums2[m2] if m2 < n2 else float('inf'))
        return (c1 + c2) / 2
