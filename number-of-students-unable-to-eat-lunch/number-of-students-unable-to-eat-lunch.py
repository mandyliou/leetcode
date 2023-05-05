class Solution:
    def countStudents(self, students: List, sandwiches: List) -> int:
        for i in sandwiches:
            if i in students:
                students.remove(i)
            else: break
        return len(students)
