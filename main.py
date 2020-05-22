from util import load_data
from classes.simulator import Simulator
from classes.course import Course




if __name__ == "__main__":
    #Cargar datos desde archivo json
    info_data = load_data("./input_files/data.json")
    info_students = load_data("./input_files/students_profiles.json")
    info_courses = load_data("./input_files/curricular_mesh.json")

    #print_mesh( malla.courses_by_level[0][0] )

    #comenzar simulacion en anio/semestre por duration semestres
    sim = Simulator(info_data, info_students, info_courses)
    sim.simulate()