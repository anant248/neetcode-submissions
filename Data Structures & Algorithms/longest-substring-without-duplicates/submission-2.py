class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers at the start and end of the sliding window
        n = len(s)
        longest, left, right = 0, 0, 0
        current = set()

        while right < n:
            while s[right] in current:
                current.remove(s[left])
                left += 1
            
            longest = max(longest, right - left + 1)
            current.add(s[right])
            right += 1
        return longest