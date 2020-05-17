# Create a list of year/semester of lenght duration (i.e: 2013/1, 2013/2, 2014/1, ...)
def my_semesters(init_year, init_semester, duration):
    semesters=[]
    for i in range(duration):
        item = str(init_year) + "/" + str(init_semester)        
        semesters.append(item)
        if i%2==1:
            init_year+=1
            init_semester=1
        else:
            init_semester+=1
    return semesters

def simulate_semester():
    return 0

def simulate(init_year, init_semester, duration):
    print("Starting simulation from:" + str(init_year) + "/" + str(init_semester) + " for:" + str(duration) + " semesters")
    for i in my_semesters( init_year, init_semester, duration):
        #print(i)
        simulate_semester()