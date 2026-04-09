class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # nested for loop continuously checking for warmer
        # time: O(N^2)
        # space: O(1) not including res output array
        n = len(temperatures)
        res = []

        for i in range(n):
            curr  = temperatures[i]
            for j in range(i + 1, n):
                future = temperatures[j]

                if future > curr:
                    res.append(j - i)
                    break

                if future <= curr and j == n - 1:
                    res.append(0)
                    break

        res.append(0)
        return res
