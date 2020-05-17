from classes.course import Course

class CurricularMesh:
    semesters = {0:2,1:1}

    def __init__(self, mesh_data):
        self.career = mesh_data["career"]
        self.list_of_courses = mesh_data["courses"] #List of every course (info) in the mesh (as on the file)

        self.courses_by_name = dict()
        self.courses_by_semester = {new_list: [] for new_list in range(1,3)}
        self.mesh = {new_list: [] for new_list in range(1,mesh_data["duration"]+1)}
        self.courses_by_level = {new_list: [] for new_list in range(mesh_data["duration"]+1)} #considers level 0 (admission)

    def build_curricular_mesh(self):
        #Marks the career begining
        self.courses_by_level[0] = Course("Ingreso", 0)
        self.courses_by_name[self.courses_by_level[0].name] = self.courses_by_level[0]

        for course_item in self.list_of_courses:
            #Course by name (dictionary)
            course = Course(course_item["name"],course_item["level"])
            self.courses_by_name[course.name] = course

            #Courses tought in each semester (1st or 2nd)
            self.courses_by_semester[self.semesters[course_item["level"]%2]].append(course)

            #Courses according to their level (1, 2,...,n)
            self.courses_by_level[course_item["level"]].append(course)

            #Set prerequisites for each course
            for prereq in course_item["prerequisites"]:
                course.prerequisites.append(self.courses_by_name[prereq])

            #self.mesh[course["level"]].append(course)

        #Sets the first courses upon admission
        for course_item in self.courses_by_level[1]:
            self.courses_by_level[0].next_courses.append(course_item)