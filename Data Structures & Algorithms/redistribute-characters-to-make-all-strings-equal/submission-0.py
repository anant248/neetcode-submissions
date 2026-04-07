class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # use a hashmap (counter) to count all letters and frequencies
        # if each letter can evenly be divided into total number of words then true, else false
        n = len(words)
        letterCount = defaultdict(int)

        # add all letters into the hashmap
        for word in words:
            for letter in word:
                letterCount[letter] += 1
        
        for letter, count in letterCount.items():
            if count % n != 0: return False

        return True