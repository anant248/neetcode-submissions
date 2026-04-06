class Solution:
    def reorganizeString(self, s: str) -> str:
        # have a frequency counter
        # each time use the most frequent letter (that is allowed to be used)
        freq = Counter(s)
        maxHeap = []
        res = []
        notAllowed = None

        # place (-count, letter) in maxHeap
        for letter, count in freq.items():
            heapq.heappush(maxHeap, (-count, letter))

        for i in range(len(s)):
            # if there is a notAllowed but heap is empty, we dont have a solution
            if notAllowed and not maxHeap:
                return ""
            
            # get the most frequent letter that is allowed
            # add it to our result list
            # increment the count (since negative) of it and place it back in the heap only if the count is not 0
            count, letter = heapq.heappop(maxHeap)
            res.append(letter)
            count += 1

            # add the previously notAllowed value back to the heap
            if notAllowed:
                heapq.heappush(maxHeap, notAllowed)
                notAllowed = None

            # update the not allowed value for the next round
            if count != 0:
                notAllowed = (count, letter)

        return "".join(res)