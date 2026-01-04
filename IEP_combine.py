import IEP_add
import IEP_setup
d= {}

def dict_clear():
    d.clear()
    return d

#makes dictionary log based on grade and teacher name  
def make_dict():
     #change so subjects are in right d also change so students are in right dict
    for T in IEP_add.T_list:
        spot = 0
        temp = 0
        clss = {}
        classroom = {}
        for i in range(len(T)):
            if type(T[i][1]) != list:
                #makes nested dict for Grade Level
                if (i % 2 == 0) and not(T[i][1] in d):
                    whom = {}
                    spot = T[i][1]
                    d[spot] = whom

                    if (len(T) - 1 >= i):
                        
                        #Makes new dictionary key (NAME) = New Dict
                        whom[T[i][0]] = clss
                        
                        #Makes new dictionary key (SUBJECT) = (Classroom)
                        current = T[i+1][1:]
                        lst = []
                        o_lst = []
                        for idv in current:
                            
                            #Checks if there are mutiple students, in the event not
                            if len(idv) <= 4:
                                ##Fix this
                                if not idv[0] in clss:
                                    o_lst.append([idv[2],idv[1]])
                                    clss[idv[0]] = o_lst
                                    
                                else:
                                    o_lst.append([idv[2],idv[1], idv[3]])
                                
                            #In the event yes there are extras
                            else:
                
                                for j in range(1, len(idv)):
                                    if j % 2 == 0:
                                        if len(lst) == 0:
                                            lst.append([idv[j], idv[j-1]])
                                        else:
                                            lst.append([idv[j+1], idv[j], idv[j-1]])
                                    
                                clss[idv[0]] = lst
                        
            else:
                lst = []
                if (IEP_add.find_course(T, T[i][0])):
                    if T[0][1] in d:
                        
                        d[T[0][1]][T[0][0]] = clss
                        start = T[i][1][0]
                        end = T[i][1][len(T[i][1])-1]
                        
                        for j in range(len(T[i])):
                            if type(T[i][j]) == list and len(T[i][j]) > 2:
                                lst.append([T[i][j][2], T[i][j][1], T[i][j][3]])
                                clss[T[i][0]] = lst
                                    
    return d

#Returns and prints a statement containing all teacher info and students in the associated classes      
def get_all(in_file):
    file = open(in_file, 'w+')
    result = ""
    make_dict()
    current = []
    j = 0
    
    for i in d:
        c_lst = []
        
        total_min = 0
        for name in d[i].keys():
            current.append(name)
            
        values = d[i].values()
        for value in values:
            
            if len(d[i]) < 2:
                result += "\n---------------\nTeacher: " + current[j] + "\nGrade: " + str(i) + "\n---------------\n"
                print("---------------\nTeacher: " + current[j] + "\nGrade: " + str(i) + "\n--------------\n")
                
            else:
                result += "\n---------------\nTeacher: " + current[j] + "\nGrade: " + str(i) + "\n---------------\n"
                print("---------------\nTeacher: " + current[j] + "\nGrade: " + str(i) + "\n---------------\n")
            j += 1

            for sub in value:
                max_time = 0
                min_time = 1000
                Students = ""
                #Checks if the teacher has multiple students
                if type(value.get(sub)[0]) == list:
                    
                    for val in value.get(sub):
                        for index in range(len(val)):
                            if index % 2 == 0:
                                if type(val[index]) == str and val[index] not in Students:
                                    #Only grabs names not time or grades
                                    try:
                                        int(val[index])
                                        break
                                    
                                    except:
                                        if not val[index] in c_lst:
                                            c_lst.append(val[index])
                                            
                                        Students += (val[index] + " ")
                                
                            else:
                                try:
                                    if max_time < int(val[index]):
                                        max_time = int(val[index])
                                    
                                    if min_time > int(val[index]):
                                        min_time = int(val[index])
                                except:
                                    break
                    
                    result += "\nSubject: " + sub + "\nMaximum Time: " + str(max_time) + "\nMinimum Time: " + str(min_time) + "\nStudents: " + str(Students) +"\n"
                    print("Subject: " + sub + "\nMaximum Time: " + str(max_time) + "\nMinimum Time: " + str(min_time) + "\nStudents: " + str(Students) +"\n")
                        

                else:
                    if 'Sped' in sub:
                        val = value.get(sub)
                        for index in range(len(val)):
                            if index % 2 == 0:
                                if not val[index] in c_lst:
                                    c_lst.append(val[index])
                                Students += val[index]
                                
                            else:
                                if max_time < int(val[index]):
                                    max_time = int(val[index])
                                    
                                if min_time > int(val[index]):
                                    min_time = int(val[index])
                        result += "\nSubject: " + sub + "\nMaximum Time: " + str(max_time) + "\nMinimum Time: " + str(min_time) + "\nStudents: " + str(Students) +"\n"
                        print("Subject: " + sub + "\nMaximum Time: " + str(max_time) + "\nMinimum Time: " + str(min_time) + "\nStudents: " + str(Students) +"\n")
                        
                    else:
                        for val in (value.get(sub)[len(value.get(sub))-1]):
                            if type(val) == str and not val in Students:
                                Students += val + " "
                        
                        result += "Subject: " + sub  + "\nAllocated Time: " +  str(value.get(sub)[:2]) + "\nMinutes: " + str(len(IEP_setup.time(value.get(sub)[0], value.get(sub)[1])) * 5) + "\nStudents: " + Students +'\n'
                        print("Subject: " + sub  + "\nAllocated Time: " +  str(value.get(sub)[:2]) + "\nMinutes: " + str(len(IEP_setup.time(value.get(sub)[0], value.get(sub)[1])) * 5) + "\nStudents: " + Students +'\n')
            
            result += ("\nAll Students ")
            for c in c_lst:
                result += c + " "
            result += '\n'
            
    dict_clear()
    
    print("All Logs Returned")
    result += "\nAll Logs Returned"
    
    file.write(result)
    file.close()
    
    return "All Logs Returned" 
