class Student:
    def __init__(self, student_id, student_profile, admission_year, admission_semester):
        self.student_id = student_id
        self.student_type = student_profile["student_type"]
        self.admission_year = admission_year
        self.admission_semester = admission_semester
        self.course_type_skills = student_profile["course_type_skills"]
        #print(self.course_type_skills)
        
        self.graduation_year = None
        self.graduation_semester = None
        self.level = 0
        self.current_courses = dict() #Pair CourseName,CourseObject
        self.courses_approved = dict() #Pair CourseName,CourseObject
        self.courses_failed = dict() #Pair CourseName, times_failed
        self.career_expelled_times = 0 #Times the student has failed more than twice a course

    # Evaluar si tiene perdida de carrera
    def evaluate_career_expelled(self):
        #Definir condiciones para perdida carrera
        #Has failed one or more courses more than twice
        expelled_condition = True if len([True for (key, value) in self.courses_failed.items() if value >=2 ]) > 0 else False
        
        return expelled_condition

    #Register and/or Increment the amount of times the student has failed a course
    def fail_course(self, course_name):
        self.courses_failed[course_name] = 1 if course_name not in self.courses_failed.keys() else self.courses_failed[course_name]+1

    def __str__(self):
        return (super().__str__() + " - StudentID=" + str(self.student_id) + " - StudentType=" + str(self.student_type))
