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
        
        self.id_to_students = 1


    def load_students_by_profile(self, year_admission, semester_admission):
        student_dict = dict()
        for student_profile in self.info_students_data["students_profiles"]:
            for i in range(0, student_profile["quantity"]):
                student_dict[self.id_to_students] = Student(self.id_to_students, student_profile, year_admission, semester_admission)
                self.id_to_students += 1
        return student_dict

    def simulate_semester(self):

        return 0

    def simulate(self):
        print("Starting simulation from:" + str(self.init_year) + "/" + str(self.init_semester) + " for:" + str(self.duration) + " semesters")

        #Generate a list of pairs Year/Semesters. I.e: 2020/1, 2020/2, ...
        semesters = my_semesters(self.init_year, self.init_semester, self.duration)

        #Build the career curricular mesh
        self.curricular_mesh.build_curricular_mesh()

        #Displays the curricular mesh
        admission = self.curricular_mesh.admission
        #print_mesh(admission)



        for semester in range(1,self.duration+1):

            # Create/Load first year students, and assign to addmission "course"
            if semester % 2 == 1:
                admission.current_students = self.load_students_by_profile( self.init_year, self.init_semester)
                print("Semester " + semesters[semester] + " i=" + str(semester) + " - admitted " + str(len(admission.current_students)))
                
                

            #self.simulate_semester()
