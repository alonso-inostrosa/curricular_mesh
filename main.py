from util import load_data
from simulator import *
from classes.course import *

if __name__ == "__main__":
    #Cargar datos desde archivo json
    infodata = load_data("./input_files/data.json")

    infocursos = load_data("./input_files/curricular_mesh.json")
    print(infocursos)



    #comenzar simulacion en anio/semestre por duration semestres
    simulate(infodata["init_year"], infodata["init_semester"], infodata["duration"])