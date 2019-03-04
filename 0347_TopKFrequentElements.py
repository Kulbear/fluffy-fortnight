from collections import defaultdict


class Solution:
    # Solution 1 - Heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # usually we need heap for top-k like problem
        d = defaultdict(int)
        for num in nums:  # O(n)
            d[num] += 1

        # create the heap is O(nlog(k)), because we have n elements and each add operation is log(k)
        # find the top k is O(klog(k)), because we need fetch k elements from the heap top and each fetch is log(k)
        return heapq.nlargest(k, d.keys(), key=d.get)
