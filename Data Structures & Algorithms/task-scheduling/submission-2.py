class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we should do the most freqeunt tasks as soon we can to allow enough cooldown cycles
        # keep 2 heaps: one for tasksRemaining, one for tasks on cooldown timer
        # first add all (task, count) to tasksRemaining, cooldownTasks is empty, cpu cycles = 0
            # do the most frequent task by:
                # pop it from tasksRemaining, do count -= 1, if count > 0 add it to cooldownTasks by (task, availableAt)
                # availableAt is at what CPU cycle this task is next available at; availableAt = curr CPU cycle + n
            # check the top of cooldownTasks
                # if it is now available, pop it from cooldownTasks and add it to tasksRemaining
            # each time we do a task (only from tasksRemaining), increment cpuCycles
        
        taskCounter = Counter(tasks)
        tasksRemaining = [(-count, task) for task, count in taskCounter.items()] # maxHeap (-count, task)
        cooldownTasks = [] # minHeap (availableAt, -count, task)
        cycles = 0
        heapq.heapify(tasksRemaining)

        # keep looping until both heaps are empty!
        while tasksRemaining or cooldownTasks:
            cycles += 1

            # first check if a cooldown task is ready to be done
            if cooldownTasks and cooldownTasks[0][0] <= cycles:
                availableAt, count, task = heapq.heappop(cooldownTasks)
                heapq.heappush(tasksRemaining, (count, task))
            
            # now do the task on the top of tasksRemaining (if there is any) and increment cycles
            if tasksRemaining:
                count, task = heapq.heappop(tasksRemaining)
                count += 1 # adding one since the tasks are negative
                if count < 0:
                    availableAt = cycles + n + 1
                    heapq.heappush(cooldownTasks, (availableAt, count, task))             

        return cycles
