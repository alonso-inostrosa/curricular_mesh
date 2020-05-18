from util import load_data
from simulator import *
from classes.course import *
from classes.curricular_mesh import *

def print_mesh(course):
    print("Course: " + course.name)
    for n in course.next_courses:
        print_mesh(n)

if __name__ == "__main__":
    #Cargar datos desde archivo json
    infodata = load_data("./input_files/data.json")

    infocursos = load_data("./input_files/curricular_mesh.json")

    #Cargar la malla de cursos
    malla = CurricularMesh(infocursos)
    malla.build_curricular_mesh()

    print_mesh( malla.courses_by_level[0][0] )

    #comenzar simulacion en anio/semestre por duration semestres
    #simulate(infodata["init_year"], infodata["init_semester"], infodata["sim_duration"])