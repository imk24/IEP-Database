import IEP_add
import IEP_combine
import IEP_setup

#Displays all teacher information
def read_file(input_file, in_file):
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
                        
            current = IEP_add.Student(idv[2], idv[1])
            
            for subject in subjects:
                (IEP_add.add_student(current, subject, time_slots))
            students = IEP_add.Students(current)
            
        
        elif 'Teacher' in idv:
            teacher = IEP_add.Teacher(idv[2], idv[1])
            courses = idv[3:]
            for course in courses:
                teacher = IEP_add.add_courses(teacher,course)
            teachers = IEP_add.Teachers(teacher)
        
    return (IEP_combine.get_all(in_file))

# read_file('IEP_data.txt', 'IEP_write.txt')
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
#END
