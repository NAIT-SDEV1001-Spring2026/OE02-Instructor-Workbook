class Submission:
    def __init__(self, student, assignment, grade):
        self.student = student
        self.assignment = assignment
        self.grade = grade

    # Custom lt for Sorting purposes
    def __lt__(self, other: Submission) -> bool:
        return self.grade < other.grade

    def __str__(self):
        return f"{self.student.name} received {self.grade} on {self.assignment}"