class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build out a course map of course : list(pre-reqs)
        # do a dfs on each course (we could have disjoint sets) keeping track 
        # of current courses visited in this journey, if repeats return false
        # if we are able to get through all courses then return true
        courseMap = {}
        visited = set()
        safe = set()

        def dfs(course):
            # if this we are in a loop return false
            if course in visited: 
                return False
            
            # courses that we know are good to complete (cache)
            if course in safe:
                return True
            
            # add this course to our seen set and do a dfs for all other prereqs
            visited.add(course)
            for item in courseMap[course]:
                if not dfs(item):
                    return False
                else:
                    safe.add(item)
            # remove this course from the current visited set
            visited.remove(course)
            return True
        
        # initialize all courses with empty list
        for i in range(numCourses):
            courseMap[i] = []

        # add the prereqs to the courseMap
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        
        # run a dfs for each course
        for course in courseMap:
            if not dfs(course):
                return False
        
        return True