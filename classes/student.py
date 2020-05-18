class Student:
    def __init__(self, student_id, admission_year, admission_semester):
        self.id = student_id
        self.admission_year = admission_year
        self.admission_semester = admission_semester
        self.graduation_year = None
        self.graduation_semester = None
        self.level = 1
        self.current_courses = dict() #Pair CourseName,CourseObject
        self.courses_approved = dict() #Pair CourseName,CourseObject
        self.courses_failed = dict() #Pair CourseName,CourseObject
        self.total_failed_once = dict() #Pair CourseName,CourseObject
        self.total_failed_twice = dict() #Pair CourseName,CourseObject
        self.total_failed_thrice = dict() #Pair CourseName,CourseObject

    def evaluar_perdida_carrera(self):
        #Definir condiciones para perdida carrera
        return 0

    def __str__(self):
        return (super().__str__() + " - StudentID=" + str(self.id))
