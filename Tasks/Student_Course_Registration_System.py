class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id  
        self.name = name
        self.enrolled_courses = {}  

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name}"

class Course:
    def __init__(self, course_code: str, name: str, capacity: int):
        self.course_code = course_code  
        self.name = name
        self.capacity = capacity  
        self.enrolled_students = {}  

    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.capacity

    def __str__(self):
        enrollment_count = len(self.enrolled_students) 
        return f"[{self.course_code}] {self.name} ({enrollment_count}/{self.capacity})"

class RegistrationSystem:
    def __init__(self):
        self.students = {}  
        self.courses = {}   
   
    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_course(self, course_code):
        return self.courses.get(course_code)

    def add_student(self, student_id, name):
        if student_id in self.students:
            return f"Error: Student ID {student_id} already exists."
        self.students[student_id] = Student(student_id, name) 
        return f"Student '{name}' added successfully."

    def add_course(self, course_code, name, capacity):
        if course_code in self.courses:
            return f"Error: Course code {course_code} already exists."
        self.courses[course_code] = Course(course_code, name, capacity) 
        return f"Course '{name}' added successfully."

    def enroll_student(self, student_id, course_code):
        student = self.get_student(student_id)
        course = self.get_course(course_code)

      
        if not student: return "Error: Student not found." 
        if not course: return "Error: Course not found." 
        if course_code in student.enrolled_courses: 
            return "Error: Student already enrolled in this course."
        if course.is_full(): 
            return "Error: Course is at maximum capacity."

       
        student.enrolled_courses[course_code] = course
        course.enrolled_students[student_id] = student
        return f"Enrolled {student.name} in {course.name}."

    def drop_course(self, student_id, course_code):
        student = self.get_student(student_id)
        course = self.get_course(course_code)

        if not student or not course: return "Error: Invalid ID or Code."
        if course_code not in student.enrolled_courses: 
            return "Error: Student is not enrolled in this course."

        
        del student.enrolled_courses[course_code]
        del course.enrolled_students[student_id]
        return f"Dropped {student.name} from {course.name}."


def main():
    sys = RegistrationSystem()
    while True:
        print("\n--- Student Registration System ---")
        print("1. Add Student\n2. Add Course\n3. Enroll\n4. Drop\n5. View Students\n6. View Courses\n7. View Student Schedule\n8. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            print(sys.add_student(sid, name))
        elif choice == '2':
            code = input("Enter Course Code: ")
            name = input("Enter Course Name: ")
            cap = int(input("Enter Capacity: "))
            print(sys.add_course(code, name, cap))
        elif choice == '3':
            sid = input("Enter Student ID: ")
            code = input("Enter Course Code: ")
            print(sys.enroll_student(sid, code))
        elif choice == '4':
            sid = input("Enter Student ID: ")
            code = input("Enter Course Code: ")
            print(sys.drop_course(sid, code))
        elif choice == '5': 
            for s in sys.students.values(): print(s)
        elif choice == '6': 
            for c in sys.courses.values(): print(c)
        elif choice == '7': 
            sid = input("Enter Student ID: ")
            student = sys.get_student(sid)
            if student:
                print(f"Schedule for {student.name}:")
                for c in student.enrolled_courses.values(): print(f" - {c}")
            else:
                print("Student not found.")
        elif choice == '8':
            break

if __name__ == "__main__":
    main()