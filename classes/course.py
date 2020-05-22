class Course:
    def __init__(self, name, level, course_type, fail_chance = 0.0):
        self.name = name
        self.level = level
        self.course_type = course_type
        self.prerequisites = []
        self.next_courses = []
        self.fail_chance = fail_chance
        
        #Students currently in the course
        self.current_students = dict()

        #Students that need to fulfill some prerequisites to enroll in the course
        self.students_incomplete_prerequisites = dict()

        #No todos los estudiantes toman el curso (aun cuando puedan)
        #TODO Definir una probabilidad de que un estudiante tome o no el curso

        #metrics
        self.total_approved = 0
        self.total_failed = 0
        self.total_failed_once = 0
        self.total_failed_twice = 0
        self.total_failed_thrice = 0
        self.total_dropped = 0 #Total of students that dropped the career at this course
        self.total_expelled = 0 #Total of students that were expelled by failing this course



    def __str__(self):
        return (super().__str__() + " - CourseName=" + self.name + ", CourseLevel=" + str(self.level))
