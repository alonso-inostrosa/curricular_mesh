class Course:
    def __init__(self, name, level, fail_chance = 0.0):
        self.name = name
        self.level = level
        self.prerequisites = []
        self.next_courses = []
        self.fail_chance = fail_chance

    def __str__(self):
        return (super().__str__() + " - CourseName=" + self.name + ", CourseLevel=" + str(self.level))
