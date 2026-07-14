# Import the class data using the data module.
from data.course_data import student_data, assignment_data, submission_data

from tools.course import Course
from tools.student import Student
from tools.assignment import Assignment
from tools.submission import Submission

def add_students(course: Course) -> None:
    for student in student_data:
        student_instance = Student(student["id"], student["name"])
        course.add_student(student_instance)

def add_assignments(course: Course) -> None:
    for assignment in assignment_data:
        assignment_instance = Assignment(assignment["id"], assignment["name"])
        course.add_assignment(assignment_instance)

def add_submissions(course: Course) -> None:
    for submission in submission_data:
        student = course.get_student(submission["student_id"])
        assignment = course.get_assignment(submission["assignment_id"])
        submission_instance = Submission(student, assignment, submission["grade"])
        student.add_submission(submission_instance)

if __name__ == "__main__":
    # create course
    course = Course("Dans Basketball Mastery Course")

    # Add students to the course
    add_students(course)

    # Add assignments to the course
    add_assignments(course)

    # Add submissions to the course
    add_submissions(course)

    print(course)

    print(f"Course Average: {course.get_course_average()}")

    # Comparison example (added a custom __eq__ to the student class)
    student1 = course.students[0]
    submission_student = course.students[0].submissions[0].student
    student_one = Student(1, "Dan")

    if student1 == student_one:
        print("This be the same!")
    else:
        print("No equals") 

    # Sorting Example (added a custom sorting to the Submissions class)

    student_submissions = course.students[0].submissions

    ascending_submissions = sorted(student_submissions)

    for submission in ascending_submissions:
        print(submission)

