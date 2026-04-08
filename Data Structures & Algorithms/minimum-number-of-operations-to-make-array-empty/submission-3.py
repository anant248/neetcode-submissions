class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # greedy approach
        # do a frequency count, then take ceil of / 3
        numberCount = Counter(nums)
        total = 0

        for number, freq in numberCount.items():
            if freq == 1: return -1
            total += math.ceil(freq / 3)
        return total