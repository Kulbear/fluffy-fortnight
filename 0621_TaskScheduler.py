class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        m = max(map(lambda x: x[1], c.items()))
        l = len([k for k in c if c[k] == m])
        return max(len(tasks), (m - 1) * (n + 1) + l)
