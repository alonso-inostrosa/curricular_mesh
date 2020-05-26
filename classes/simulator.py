from classes.course import Course
from classes.student import Student
from classes.curricular_mesh import CurricularMesh

# Create a list of year/semester of lenght duration (i.e: 2013/1, 2013/2, 2014/1, ...)
def my_semesters(init_year, init_semester, duration):
    semesters = dict()
    for i in range(1,duration+1):
        item = str(init_year) + "/" + str(init_semester)
        semesters[i]=item
        if i % 2 == 1:
            init_semester += 1
        else:
            init_year += 1
            init_semester = 1

    return semesters

def print_mesh(course):
    print("Course: " + course.name)
    for n in course.next_courses:
        print_mesh(n)

class Simulator:

    def __init__(self, info_data, info_students, info_courses):
        self.name = info_data["name"]
        self.init_year = info_data["init_year"]
        self.init_semester = info_data["init_semester"]
        self.duration = info_data["sim_duration"]

        self.info_students_data = info_students

        #Cargar la malla de cursos
        self.curricular_mesh = CurricularMesh(info_courses)
        
        #Unique student ID (starts in 1)
        self.id_to_students = 1


    def load_students_by_profile(self, year_admission, semester_admission):
        student_dict = dict()
        for student_profile in self.info_students_data["students_profiles"]:
            for _ in range(0, student_profile["quantity"]):
                student_dict[self.id_to_students] = Student(self.id_to_students, student_profile, year_admission, semester_admission)
                self.id_to_students += 1
        return student_dict


    # Simulate semester considering courses are tought one semester a year
    def simulate_semester(self, semester_to_simulate, semester_name):
        semester_number = 1 if semester_to_simulate % 2 == 1 else 2
        print("SIMULATOR - Simulating semester:" + str(semester_to_simulate) + " - Semester Number:" + str(semester_number) +  " - Semester Name:" + semester_name)
        
        #If semester is 1, move admission students to first semester courses
        if semester_number == 1:
            for courses in self.curricular_mesh.admission.next_courses:
                admission_students = self.curricular_mesh.admission.current_students
                courses.current_students.update(admission_students)

        #Iterating over courses of the current semester
        #defininf approved/failed students to each course of the semester
        semester_courses = self.curricular_mesh.courses_by_semester
        for course in semester_courses[semester_number]:
            # Detemine failed and approved students
            # Obtain approved and failed students as lists
            approved, _ = course.simulate_final()
            
            for next_course in course.next_courses:
                #Assign current course's approved students to next course
                #dict() of students with incomplete prerequisites
                for stdnt in approved:
                    print("SIMULATOR - Current course:" + course.name + "\tNext:" + next_course.name)
                    next_course.students_incomplete_prerequisites[stdnt.student_id] = stdnt
        
        #Iterating over courses of the current semester
        #Students that fulfill the prerequisites of each of the next courses
        #is moved to the course.current_student dict()
        semester_courses = self.curricular_mesh.courses_by_semester
        for course in semester_courses[semester_number]:
            for next_course in course.next_courses:
                #Assign current course's approved students to next course
                #dict() of students with incomplete prerequisites
                print("SIMULATOR - Trying to Enroll-Students from Course:" + course.name + "\tinto course:" + next_course.name)
                next_course.enroll_students()


        return 0

    def simulate(self):
        print("SIMULATOR - Starting simulation from:" + str(self.init_year) + "/" + str(self.init_semester) + " for:" + str(self.duration) + " semesters")
        #Generate a list of pairs Year/Semesters. I.e: 2020/1, 2020/2, ...
        semesters = my_semesters(self.init_year, self.init_semester, self.duration)

        #Build the career curricular mesh
        self.curricular_mesh.build_curricular_mesh()

        #Displays the curricular mesh starting from admission
        #print_mesh(self.curricular_mesh.admission)

        #Semester begin in 1
        for semester in range(1,self.duration+1):
            print("SIMULATOR - Attempting to simulate semester " + semesters[semester])
            # Admission
            # Create/Load first year students, and assign to addmission "course"
            if semester % 2 == 1:
                self.curricular_mesh.admission.current_students = self.load_students_by_profile( self.init_year, self.init_semester)
                #print("Semester " + semesters[semester] + " i=" + str(semester) + " - admitted " + str(len(self.curricular_mesh.admission.current_students)))

            #Simulate semester by semester
            self.simulate_semester(semester, semesters[semester])

            # Graduation

        print("SIMULATOR - Ending Simulation after semester:" + str(self.duration))
        print("SIMULATOR - ***********Metrics***********")
        for sem in self.curricular_mesh.courses_by_semester.keys():
            print("SIMULATOR - Semester " + str(sem))
            for course in self.curricular_mesh.courses_by_semester[sem]:
                print( "SIMULATOR - Course:" + course.name + "\tLevel:" + str(course.name) + "\tTotal_Approved:" + str(course.total_approved) + "\tTotal_Failed:" + str(course.total_failed) + "\tFailed Once:" + str(course.total_failed_once) + "\tFailed Twice:" + str(course.total_failed_twice) + "\tFailed Thrice:" + str(course.total_failed_thrice))

        #TODO: Print metrics from students