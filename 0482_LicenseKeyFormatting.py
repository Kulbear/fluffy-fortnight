class Solution:
    # Solution 1
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = (S.replace('-', '')).upper()
        for i in range(len(S) - 1, -1, -K):
            S = S[:i + 1] + '-' + S[i + 1:]
        return S.strip('-')
