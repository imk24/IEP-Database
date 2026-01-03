import IEP_combiner
import IEP_setup
import IEP_file

def R_format(read_file, csv_file):
    #Initalizes headers
    students = []
    total_subs = []
    s_subs = []
    teachers = []
    t_subs = []
    
    #Calling needed methods
    out = IEP_file.out_sched(read_file)
    read = IEP_file.read_file(read_file)
    
    #Appends the header values into the students list
    students.append('Subs')
    students.append('Grades')
    students.append('Teacher(s)')
    
    #Goes into the IEP_file method sched_student and checks all str valyes and appends it into the s_subs
    for time in out:
        if type(time) == list:
            for i in range(len(time)):
                #Making sure not to grab grades or minutes
                try:
                    int(time[i])
                    break
                except:
                    if time not in subs:
                        s_subs.append(time[i])
        else:
            #Checking all students in the list
            if ('Student' in time[:len(time)-1]):
                stud = time[:len(time)-1].split(',')[2]
                students.append(stud)
                
                for t in time[:len(time)-1].split(',')[3].split():
                    t = t + (time[:len(time)-1].split(',')[1])
                    if not t in total_subs:
                        total_subs.append(t)
                val = time[:len(time)-1].split(',')[3].split()
               
                val_1 = time[:len(time)].split(',')[4].split()
                
                for i in range(len(val)):
                    s_subs.append((time[:len(time)-1].split(',')[2],val[i],val_1[i], time[:len(time)-1].split(',')[1]))
                    
                    
            if ('Teacher' in time[:len(time)-1]):
                teach = time[:len(time)-1].split(',')[2]
                teachers.append(teach)
                
                t_subs.append((teach, time[:len(time)-1].split(',')[3].split(),time[:len(time)-1].split(',')[1].split())) 
    
    
    students.append('Start Time(s)')
    students.append('End Time(s)')
    with open(csv_file, "w") as file:
        file.write(",".join(students) + "\n")
            
        for i in range(len(total_subs)):
            file.write(total_subs[i] + ",".join([','] * (len(students) -6)) + "\n")
    
    return (s_subs, t_subs, total_subs)

#Adds rest of the info into the premade R_format
def R_add(s_info, t_info, total, csv_file):
    #Found it easiest to use a dictionary to place holder the values
    d = {}
    file = open(csv_file)
    lines = file.readlines()

    for index in range(len(lines)):
        lines[index] = (lines[index].strip().split(','))
    
    
        #Checks if the student data correlates to the subject and student name and then adds the minutes for the student
        for i in range(2, len(lines[index])):
            elm = 0
            for s in s_info:
                for e in range(len(lines[index][0])):
                    if lines[index][0][e] == " ":
                        elm = lines[index][0][:e]

                #Ensuring the value is in both sets
                if lines[0][i] in s and elm in s:
                    
                    lines[index][1] = s[3].strip()
                    lines[index][i] = s[2]
                    if elm in IEP_setup.Grades[0][lines[index][1].strip()]:
                        d[lines[index][0]] = (IEP_setup.get_time(lines[index][1].strip(), elm))
                        #Takes the key and appends the correct one to each data set
                        lines[index][len(lines[index]) -2] = d.get(lines[index][0])[0]
                        lines[index][len(lines[index]) -1] = d.get(lines[index][0])[1]

                    else:
                        line = lines[index][0]
                        for l in range(len(line)):
                            if line[l] == '{':
                                if (line[:l] + '{Gen}') in IEP_setup.Grades[0][lines[index][1].strip()]:
                                    
                                    if not lines[index][0] in d:
                                        d[lines[index][0]] = IEP_setup.get_time(lines[index][0][len(lines[index][0])-1:], line[:l] + '{Gen}')

                                    lines[index][len(lines[index]) -2] = d.get(lines[index][0])[0]
                                    lines[index][len(lines[index]) -1] = d.get(lines[index][0])[1]
                                    
                                #BM and BS were assigned all in this case
                                if line[:l] == 'BM' or line[:l] == 'BS':
                                    d[lines[index][0]] = 'ALL'
                                    
                                    lines[index][len(lines[index]) -2] = 'ALL'
                                    lines[index][len(lines[index]) -1] = 'ALL'    
                                    
            #Adds teachers and grades into appropraite rows                   
            for t in t_info:
                for each in t[1]:
                    if lines[index][0] == (each + " " + t[2][0]):
                        lines[index][1] = t[2][0]
                        lines[index][2] = t[0]
                    
                if len(t[1]) == 1 and (t[1][0] in lines[index][0]) and (t[2][0] in lines[index][0]):
                    lines[index][2] = t[0]
                    lines[index][1] = t[2][0]
                    
    #Renames the col[0] values to get rid of any grade indication 
    for index in range(len(lines)):
        lines[index][0] = (lines[index][0][:len(lines[index][0])-2])
                
    with open(csv_file, "w") as file:
        #Writes the lines in each column according to order
        for i in range(len(total)+1):
            file.write(",".join(lines[i]) + "\n")   
  
# Print statements for the methods.
# L = R_format('IEP_data.txt','R_out.csv')
# R_add(L[0],L[1],L[2], 'R_out.csv')
