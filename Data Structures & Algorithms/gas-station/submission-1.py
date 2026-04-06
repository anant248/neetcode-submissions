class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # try starting from each
        n = len(gas)
        completed = False

        for i in range(n):
            station = i
            currentGas = gas[station]
            while currentGas - cost[station] >= 0:
                currentGas -= cost[station]
                station += 1
                station %= n

                # check if we have done a loop
                if station == i:
                    completed = True
                    break

                currentGas += gas[station]

            if completed:
                return i
        return -1

        # currentGas = 0
        # station = 3
        # i = 3
