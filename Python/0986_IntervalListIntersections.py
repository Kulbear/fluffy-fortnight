class Solution:
    def intervalIntersection(self, A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        ans = []

        # two pointer
        i, j = 0, 0
        while i < len(A) and j < len(B):
            # no overlap and A[i] is left to B[j]
            if A[i][1] < B[j][0]:
                i += 1
            # no overlap and B[j] is left to A[i]
            elif B[j][1] < A[i][0]:
                j += 1
            # overlap
            else:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                # A[i] has overlap with B[j]
                # A's tail is left to B's tail, means A[i + 1] might be overlapped with B[j]
                if A[i][1] < B[j][1]:
                    i += 1
                else:
                    j += 1

        return ans
