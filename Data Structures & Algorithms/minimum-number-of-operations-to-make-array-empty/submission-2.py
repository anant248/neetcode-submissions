class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # using DP with memoization
        cache = {}
        def dfs(count):
            if count in [2,3]:
                return 1
            if count <= 1:
                return float("inf")
            if count in cache:
                return cache[count]
            
            cache[count] = 1 + min(dfs(count - 2), dfs(count - 3))
            return cache[count]

        numCounter = Counter(nums)
        totalOperations = 0
        for number, freq in numCounter.items():
            totalOperations += dfs(freq)
            if totalOperations == float('inf'):
                return -1
        return totalOperations
