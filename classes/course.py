import random
from classes.student import Student

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

    def enroll_students(self):
        students_all_prereq_fulfilled = list()

        for student_key in self.students_incomplete_prerequisites.keys():
            stdnt = self.students_incomplete_prerequisites[student_key]
            #Check if student fulfill prerequisites of the course
            #Student has a dict of approved courses
            amount = 0
            print("COURSE - Course:" + self.name + "\tAmount of Prerequisites=" + str(len(self.prerequisites)))
            for pre_course in self.prerequisites:
                if pre_course.name in stdnt.courses_approved.keys():
                    #print("Course:" + self.name + "\tPrereq YES:" + pre_course.name + "\Student:" +  str(stdnt.student_id))
                    amount+=1
                else:
                    break
                    #print("Course:" + self.name + "\tPrereq NOT:" + pre_course.name + "\Student:" +  str(stdnt.student_id))
            
            #Fulfill prerequisites? Then copied to current_students
            if amount == len(self.prerequisites) and amount != 0:
                print("COURSE - Student:" + str(stdnt.student_id) + "\tFulfills Prerequisites for Course:" + self.name)
                self.current_students[stdnt.student_id] = stdnt
                students_all_prereq_fulfilled.append(stdnt)

        #Remove enrolled students from prerequisites dict
        for student in students_all_prereq_fulfilled:
            self.students_incomplete_prerequisites.pop(student.student_id)


    def simulate_final(self):
        print("COURSE - Simulating approval/failure for Course:" + self.name + " - qty:" + str(len(self.current_students)) + "\tcourse_type:" + str(self.course_type))
        
        #Simulating aproved/failed
        approved = list()
        failed = list()
        for student_key in self.current_students.keys():
            chance_fail = self.current_students[student_key].course_type_skills[self.course_type-1]["fail_chance"]
            #Approves?
            nbr = random.uniform(0,1)
            stdnt = self.current_students[student_key]
            if( nbr > chance_fail):
                print("COURSE - Student:" + str(self.current_students[ student_key ]) + "\APPROVES random_chance=" + str(nbr) + "\tStudent chance of failure:" + str(chance_fail))
                self.total_approved += 1
                approved.append(self.current_students[ student_key ])
                stdnt.courses_approved[self.name] = self
            else:
                #If Failed, then register failed course and times has failed current course
                self.total_failed+=1
                if self.name in stdnt.courses_failed:
                    stdnt.courses_failed[self.name]+=1
                else:
                    stdnt.courses_failed[self.name]=1

                #Register amount of times failed by each students
                if stdnt.courses_failed[self.name] == 1:
                    self.total_failed_once += 1
                elif stdnt.courses_failed[self.name] == 2:
                    self.total_failed_twice += 1
                elif stdnt.courses_failed[self.name] == 3:
                    self.total_failed_thrice += 1

                print("COURSE - Student:" + str(self.current_students[ student_key ]) + "\FAILS random_chance=" + str(nbr) + "\tStudent chance of failure:" + str(chance_fail))
                failed.append(self.current_students[ student_key ])

        #Remove students that approved the course from current_students
        #Failed students remain in current course
        [self.current_students.pop(key.student_id) for key in approved]

        return approved, failed

    def __str__(self):
        return (super().__str__() + " - CourseName=" + self.name + ", CourseLevel=" + str(self.level))
