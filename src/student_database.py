# Write your solution here
def add_student(students: dict, name: str):
    if is_student(students, name):
        print(f"Student '{name}' is already in the database")
        return 
    
    students[name] = {
        "Completed Courses": []
        }


def is_student(students: dict, name: str) -> bool:
    return name in students

def add_course(students: dict, name: str, course_tuple:tuple):
    add_course = course_tuple[0]
    add_grade = course_tuple[1]

    if is_student(students, name):
        courses = students[name]["Completed Courses"]

        if add_grade == 0:
            return
        
        for i, (course_name, course_grade) in enumerate(courses):
            if course_name == add_course:
                if add_grade < course_grade:
                    return
                else:
                    courses[i] = (add_course, add_grade)
                    return

        courses.append((add_course, add_grade))

def print_courses(students: dict, name: str):
    if not students[name]["Completed Courses"]:
        print(f" no completed courses")
    else:
        grade_sum = 0
        courses = students[name]["Completed Courses"]
        print(f" {len(courses)} completed courses:")
        for course in courses:
            grade_sum += course[1]
            print(f"  {course[0]} {course[1]}")
        print(f" average grade {grade_sum / len(courses)}")


def print_student(students: dict, name: str):
    if is_student(students, name):
        print(f"{name}:")
        print_courses(students, name)
    else:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    student_number = len(students)
    best_student, best_avg = best_average(students)
    most_courses_student, most_courses_count = most_courses(students)

    print(f"students {student_number}")    
    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_avg} {best_student}")
   
def best_average(students: dict) -> tuple:
    best_student = None
    best_average = 0

    for name, info in students.items():
        total_grade = sum(course[1] for course in info["Completed Courses"])
        num_courses = len(info["Completed Courses"])

        if num_courses > 0:
            average_grade = total_grade / num_courses
            if average_grade > best_average:
                best_average = average_grade
                best_student = name
 
    return best_student, best_average    

def most_courses(students: dict) -> tuple:
    best_student = None
    most_courses = 0

    for name, info in students.items():

        if len(info["Completed Courses"]) > most_courses:
            most_courses = len(info["Completed Courses"])
            best_student = name
 
    return best_student, most_courses

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)


