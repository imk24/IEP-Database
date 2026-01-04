import IEP_setup

S_list = []
T_list = []
             
def Teacher(name, grade):
    o_lst = []
    
    t_lst = []
    t_lst.append(name)
    t_lst.append(grade)
    
    o_lst.append(t_lst)
    return o_lst

def Student(name, grade):
  
    s_lst = []
    points = 0
    s_lst.append(name)
    s_lst.append(grade)
    s_lst.append(points)
    
    return s_lst

def Students(s):
    for i in s:
        S_list.append(s)
        return S_list
    
#A method to shorten the print, finds the exact course for teach using the teach obj and course name
def find_course(t_lst, course):
    try:
        return IEP_setup.get_time(str(t_lst[0][1]),course)
    except:
        return False

#Adds a course and time into the teacher list
def add_courses(t_lst, course):
    t_lst.append([])
    if course == 'Sped':
        t_lst[len(t_lst)-1].append(course)
        return t_lst
    
    #Time uses the time method in set_up to find the whole time frame for the course
    time = IEP_setup.time(find_course(t_lst, course)[0], find_course(t_lst, course)[1])
    
    #In the event this is the first course added
    if len(t_lst) < 3:
        time = IEP_setup.time(find_course(t_lst, course)[0], find_course(t_lst, course)[1])
        t_lst[len(t_lst)-1].append(course)
        t_lst[len(t_lst)-1].append([time[0],time[len(time)-1]])
        return t_lst
     
    else:
        time = IEP_setup.time(find_course(t_lst, course)[0], find_course(t_lst, course)[1])
        for t in t_lst:
            for i in t:
                #Checks if the point in time is already taken
                if (type(i) == list) and (s_time in i):
                    return print("Time slot is taken")
                
            else:
                #Appends into the teacher list
                if not (course in t):
                    t_lst[len(t_lst)-1].append(course)
                    t_lst[len(t_lst)-1].append([time[0],time[len(time)-1]])
                    return t_lst
       
   
def Teachers(t_lst):
    T_list.append(t_lst)
    return T_list

#Adds a student and associated subject into the appropraite teacher list
def add_student(s_lst, subject, time):
   
    #GOTTA ADD A STUDENT LIST CHECKER< SIZE
    g_val = False
    s_val = False
    val = 0
    grade = s_lst[1]
    
    #Goes inside of the Teacer list, and if both grade and subject are in the list
    #adds student to the list

    for T in T_list:
       
        for index in T:
            for i in range(len(index)):
                if (grade == (index[i])):
                    g_val = True
                
                if (subject == (index[i])):
                    s_val = True
        
            if s_val == False:
                for sub in subject:
                    if type(index[0]) == str:
                        if (index[0] in sub):
                            s_val = True
        
        if (s_val and g_val) == True:
        
            for index in T:
                
                for i in index:
                
                    for sub in range(len(subject)):
                
                        if type(i) == str:
                            
                            
                            temp = 0
                            
                                    
                            if ('Gen' in subject[sub]) and i not in subject[sub]:
                                for out in range(len(T_list)):
                                    for inner in T_list[out]:
                                        if (subject[sub] in inner) and (s_lst[0] not in inner):
                                            inner.append(s_lst[0])
                            
                        
                            for j in range(2, len(index)):
                                if(subject[sub] in index[j], subject[sub], s_lst[0]):
                                    temp = j   
                                    
                            if (i in subject[sub]) and not(subject[sub] in index[temp]):
                                log = [0]
                                if subject[sub] in (IEP_setup.get_courses(s_lst[1])):
                                    log = ((IEP_setup.get_time(s_lst[1], subject[sub]), subject[sub]))
                                    index.append([subject[sub], time[0][sub], s_lst[0], log[0]])
                                else:
                                    for s in range(len(subject[sub])):
                                        if subject[sub][s] == '{':
                                            title = (subject[sub][:s]) + "{Gen}"
                                            if title in IEP_setup.Grades[0][s_lst[1]]:
                                                log = (IEP_setup.get_time(s_lst[1],title))
                                        
                                    index.append([subject[sub], time[0][sub], s_lst[0], log])
                                
                                
                            elif (i in subject[sub]) and (subject[sub] in index[temp]):
                                (index[index.index(index[temp])].append(time[0][sub]))
                                (index[index.index(index[temp])].append(s_lst[0]))

    return T_list


# This method adds all courses for the grade into the schedule
def add_all(t_lst):
    for i in t_lst:
        grade = i[1]
    
    courses = IMB_setup.get_courses(grade)
    for i in courses:
        t_lst.append([])
        t_lst[len(t_lst)-1].append(i)
        t_lst[len(t_lst)-1].append([courses[i]])
    return (t_lst)
    
## END OF CODE
