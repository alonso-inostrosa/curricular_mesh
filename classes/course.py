class Course:

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.prerequisites = []
        self.next_courses = []