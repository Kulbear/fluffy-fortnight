from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # note that this function returns whether there exists any cycle
        def takeCourse(course):
            if status[course] == 1:
                return True  # has cycle
            if status[course] == 2:
                return False  # no cycle, pre has been done

            status[course] = 1
            for futureCourse in graph[course]:
                if takeCourse(futureCourse):
                    return True

            status[course] = 2
            return False

        # new = 0, taking = 1, finished = 2
        status = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for course, pre in prerequisites:
            # a fun fact is that graph[course].append(pre) also works, could think about why
            graph[pre].append(course)

        for course in range(numCourses):
            if takeCourse(course):
                return False

        return True
