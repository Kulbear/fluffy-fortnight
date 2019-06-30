class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = [1 for _ in ratings]

        # ensure the i-th kids has more candies than (i-1)-th kid when needed
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i - 1] + 1

        # ensure the i-th kids has more candies than (i+1)-th kid when needed
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], (result[i + 1] + 1))

        return sum(result)
