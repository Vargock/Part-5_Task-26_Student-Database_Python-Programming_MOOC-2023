# Function to add a new student to the 'students' dictionary
def add_student(students: dict, name: str):
    # Check if the student is already in the dictionary
    if is_student(students, name):
        print(f"Student '{name}' is already in the database")
        return 
    
    # If the student doesn't exist, add the student with an empty "Completed Courses" list
    students[name] = {
        "Completed Courses": []
        }


# Function to check if a student already exists in the 'students' dictionary
def is_student(students: dict, name: str) -> bool:
    return name in students

# Function to add a course and grade for a student
def add_course(students: dict, name: str, course_tuple: tuple):
    # Extract course name and grade from the tuple
    add_course = course_tuple[0]
    add_grade = course_tuple[1]

    # Check if the student exists in the dictionary
    if is_student(students, name):
        # Extract completetd courses and their grades from the list of student's completed courses
        courses = students[name]["Completed Courses"]

        # If the grade is 0, don't add the course
        if add_grade == 0:
            return
        
        # Iterate over the courses the student has completed
        for i, (course_name, course_grade) in enumerate(courses):
            # If the student already has the course, update the grade if it's higher
            if course_name == add_course:
                if add_grade < course_grade:
                    return
                else:
                    courses[i] = (add_course, add_grade)
                    return

        # If the student hasn't taken the course, append the new course and grade
        courses.append((add_course, add_grade))

# Function to print all completed courses and average grade for a student
def print_courses(students: dict, name: str):
    # Check if the student has completed any courses
    if not students[name]["Completed Courses"]:
        print(f" no completed courses")
    else:
        grade_sum = 0
        courses = students[name]["Completed Courses"]
        print(f" {len(courses)} completed courses:")
        # Iterate through each course and print the course name and grade
        for course in courses:
            grade_sum += course[1]
            print(f"  {course[0]} {course[1]}")
        # Print the average grade for the student
        print(f" average grade {grade_sum / len(courses)}")

# Function to print student information including completed courses
def print_student(students: dict, name: str):
    # Check if the student exists in the database
    if is_student(students, name):
        print(f"{name}:")
        print_courses(students, name)
    else:
        print(f"{name}: no such person in the database")

# Function to print summary of all students' information
def summary(students: dict):
    student_number = len(students)
    best_student, best_avg = best_average(students)
    most_courses_student, most_courses_count = most_courses(students)

    print(f"students {student_number}")    
    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_avg} {best_student}")
   
# Function to find the student with the best average grade
def best_average(students: dict) -> tuple:
    best_student = None
    best_average = 0

    # Iterate through all students to calculate their average grade
    for name, info in students.items():
        total_grade = sum(course[1] for course in info["Completed Courses"])
        num_courses = len(info["Completed Courses"])

        # Only calculate average if the student has completed any courses
        if num_courses > 0:
            average_grade = total_grade / num_courses
            # Update the best student if the current one has a higher average
            if average_grade > best_average:
                best_average = average_grade
                best_student = name
 
    return best_student, best_average    

# Function to find the student with the most completed courses
def most_courses(students: dict) -> tuple:
    best_student = None
    most_courses = 0

    # Iterate through all students to find the one with the most courses
    for name, info in students.items():
        # If the current student has more courses, update the record
        if len(info["Completed Courses"]) > most_courses:
            most_courses = len(info["Completed Courses"])
            best_student = name
 
    return best_student, most_courses

# Main program block to test the functions
if __name__ == "__main__":
    students = {}
    # Add students to the database
    add_student(students, "Peter")
    add_student(students, "Eliza")
    # Add courses and grades to the students
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # Display a summary of the students' data
    summary(students)