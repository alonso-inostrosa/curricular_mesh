from classes.course import Course

class CurricularMesh:
    semesters = {0:2,1:1}

    def __init__(self, mesh_data):
        """Curricular mesh constructor
        This constructor initializes different data structures to organize courses of a career.

        self.career is the career's name
        self.list_of_courses_data holds a list with parsed json/data of the curricular mesh.
        self.courses_by_name is a dictionary holding pairs of course's names (keys) and course objects (values).
        self.courses_by_level is a list of career levels, in each level is a list containing the courses
        self.courses_by_semester is a dict/list holding two lists of courses (at 1, there is a list containing semesters tought in the first semester of every year. The same is valid for 2 as the second semester).

        Parameters:
        mesh_data: Parsed json data converted into dictionaries/lists of the courses composing a career curricular mesh.

        """

        self.career = mesh_data["career"]
        self.duration = mesh_data["duration"] #Doesn't consider admission and graduation
        self.list_of_courses_data = mesh_data["courses"] #List of every course (info) in the mesh (as on the file)

        self.courses_by_name = dict() #Hold pairs of "Course Name" keys and References to the Course Object.
        self.courses_by_semester = {new_list: [] for new_list in range(1,3)} #

        self.mesh = {new_list: [] for new_list in range(1,mesh_data["duration"]+1)}

        #Courses organized by the semester they are tought.
        # Semester 0 is the admission process, leads to first level courses.
        # Semester duration+1 is the last semester
        # Semester duration+2 is the graduation semester
        self.courses_by_level = {new_list: [] for new_list in range(mesh_data["duration"]+2)}




    def build_curricular_mesh(self):
        """This function creates the curricular mesh of courses structures
        """

        #Marks the career begining
        #self.courses_by_level[0] = Course("Admision", 0)
        #self.courses_by_name[self.courses_by_level[0].name] = self.courses_by_level[0]

        #Links course objects and its prerequisites
        #Organize course objects by level and by the semester they are tought
        for course_item in self.list_of_courses_data:
            #Course by name (dictionary)
            course = Course(course_item["name"],course_item["level"])
            self.courses_by_name[course.name] = course

            #Courses tought in each semester (1st or 2nd), does not consider admission nor graduation
            if course.level not in [0,self.duration]:
                self.courses_by_semester[self.semesters[course_item["level"]%2]].append(course)

            #Courses according to their level (1, 2,...,n)
            self.courses_by_level[course_item["level"]].append(course)
            #print("Level: " + str(course_item["level"]) + " - Course: " + str(course))

            #Set prerequisites for each course
            for prereq in course_item["prerequisites"]:
                course.prerequisites.append(self.courses_by_name[prereq])

        #Set next courses of each course. I.e: sets which courses the current course is a prerequisite of.
        for course_name in self.courses_by_name:
            for prereq_course in self.courses_by_name[course_name].prerequisites:
                #print(prereq_course.name + " -> " + self.courses_by_name[course_name].name)
                prereq_course.next_courses.append(self.courses_by_name[course_name])

        #Sets the first courses upon admission
        #for course_item in self.courses_by_level[1]:
        #    self.courses_by_level[0].next_courses.append(course_item)


        #self.courses_by_level[0] = Course("Egreso", self.duration+1)
        #self.courses_by_name[self.courses_by_level[0].name] = self.courses_by_level[0]