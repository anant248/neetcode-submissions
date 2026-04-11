class TimeMap:
    # store a hashmap of key: list of tuples [(timestamp, value)]
    # do binary search on the list of tuples

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or not self.timemap[key]:
            return ""
        
        valueList = self.timemap[key]
        valTime, value = self.binarySearch(valueList, timestamp)
        return value
    
    def binarySearch(self, valueList, timestamp):
        left = 0
        right = len(valueList) - 1
        resTime, resValue = -1, ""

        while left <= right:
            mid = left + (right - left) // 2
            currTime = valueList[mid][0]
            currValue = valueList[mid][1]

            if currTime == timestamp:
                return (currTime, currValue)
            elif currTime < timestamp:
                resTime, resValue = currTime, currValue # store this as a possible answer then try bigger
                left = mid + 1
            else:
                right = mid - 1
        return (resTime, resValue)
        
        

            
        
