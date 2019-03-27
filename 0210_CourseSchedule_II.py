class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            # add to done list, due to the fact this post-order traversal, we need to reverse it later
            order.append(course)
            return False

        # new = 0, taking = 1, finished = 2
        status = [0 for _ in range(numCourses)]
        # we don't really need a hash table...
        graph = [[] for _ in range(numCourses)]
        order = []
        for course, pre in prerequisites:
            # a fun fact is that graph[course].append(pre) also works, could think about why
            graph[pre].append(course)

        for course in range(numCourses):
            if takeCourse(course):
                return []

        # don't forget to reverse it...
        return order[::-1]
