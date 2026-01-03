import IEP_combiner
import IEP_setup

#Displays all teacher information
def read_file(input_file):
    file = open(input_file)
    f_read = file.readlines()
    
    for idv in f_read:
        time_slots = []
        subjects = []
        idv = idv.split()
        for i in range(len(idv)):
            idv[i] = (idv[i].strip(','))
        
        current = 0
        if 'Student' in idv:
            subjects.append([])
            time_slots.append([])
            for i in range(len(idv)):
                try:
                    int(idv[i])
                    if int(idv[i]) > 5:
                        time_slots[len(time_slots)-1].append(idv[i])
                    
                except:
                    if i >= 3:
                        subjects[len(subjects)-1].append(idv[i])
                        i += 1
                        
            current = IEP_combiner.Student(idv[2], idv[1])
            
            for subject in subjects:
                (IEP_combiner.add_student(current, subject, time_slots))
            students = IEP_combiner.Students(current)
            
        
        elif 'Teacher' in idv:
            teacher = IEP_combiner.Teacher(idv[2], idv[1])
            courses = idv[3:]
            for course in courses:
                teacher = IEP_combiner.add_courses(teacher,course)
            teachers = IEP_combiner.Teachers(teacher)
        
    return (IEP_combiner.get_all())

# read_file('IEP_data.txt')
# Print Statement for file, Must Comment out if trying to use IEP_sched

#Used for the IEP_sched.R_format method
def out_sched(read):
    file = open(read)
    f_read = file.readlines()
    return f_read

#Displays all student information
def sched_student(read):
    file = open(read)
    f_read = file.readlines()
    info = []

    for idv in f_read:
        name = 0
        subjects = []
        idv = idv.split()
        for i in range(len(idv)):
            idv[i] = (idv[i].strip(','))
        
        current = 0
        if 'Student' in idv:
            name = idv[2]
            
            for i in range(len(idv)):
                try:
                    int(idv[i])
                    subjects.append(idv[i])
                    
                except:
                    if i >= 3:
                        subjects.append(idv[i])
                        i += 1
                        
        if len(subjects) > 0:
            info.append(name)
            info.append(subjects)   
    return (info)
