class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize indegree array and adjacency list
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        # Fill the indegree array and adjacency list
        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        # Queue to keep track of courses with no prerequisites (indegree 0)
        queue = [course for course in range(numCourses) if indegree[course] == 0]

        # Counter to keep track of the number of courses that can be taken
        count = 0

        # Process courses with no prerequisites
        while queue:
            course = queue.pop(0)  # Dequeue a course
            count += 1  # Increment the count since this course can be taken
            
            # Decrease the indegree of courses that have the current course as a prerequisite
            for next_course in graph[course]:
                indegree[next_course] -= 1
                # If the next course has no prerequisites now, enqueue it
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If count equals the total number of courses, all courses can be taken
        return count == numCourses
