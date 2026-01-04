grade = {}
Grades = [grade]

#Time takes the strings of a start and end time and out puts all time values in between
def time(start_time, end_time):
    #Define Parameters
    lst = []
    s_hour = ''
    s_min = ''
    
    e_hour = ''
    e_min = ''
    
    #Seperating hour and minute
    for i in range(len(start_time)):
        if start_time[i] != ':':
            s_hour += str(start_time[i])
        else:
            s_min += str(start_time[i + 1:])
            break
        
    for i in range(len(end_time)):
        if end_time[i] != ':':
            e_hour += str(end_time[i])
        else:
            e_min += str(end_time[i + 1:])
            break
        
    c_time = 0
    #Changes e_hour into military time
    if int(e_hour) < int(s_hour):
        e_hour = int(e_hour)
        e_hour += 12
    
    for i in range(int(s_hour), int(e_hour)+1):
        for j in range(0, 60, 5):
            #Return statement
            if len(str(j)) == 1:
                if (str(i) + ':' + '0' + str(j)) == str(e_hour) + ':' + e_min:
                    if (i-12) > 0:
                        lst.append(str(i-12)+ ':' + '0' + str(j))
                    else:
                        lst.append(str(i) + ':' + '0' + str(j))
                    return (lst)
            else:
                if (str(i) + ':' + str(j)) == str(e_hour) + ':' + e_min:
                    if (i-12) > 0:
                        lst.append(str(i-12)+ ':' + str(j))
                    else:
                        lst.append(str(i) + ':' + str(j))
                    return (lst)
            
            #In the event of a single digit minute
            if len(str(j)) == 1:
                c_time = int(str(i) + '0' + str(j))
            else:
                c_time = int(str(i) + str(j))
            
            #Outputs time
            if int(s_hour + s_min) <= c_time:
                if i > 12:
                    if len(str(j)) == 1:
                        lst.append(str(i-12)+ ':0' + str(j))
                    else:
                        lst.append(str(i-12)+ ':' + str(j))
                else:
                    if len(str(j)) == 1:
                        lst.append(str(i)+ ':0' + str(j))
                    else:
                        lst.append(str(i)+ ':' + str(j))

#Set up calls the hrade fimctopms nio;domg a schedu
def set_up():
    for level in Grades:
        level['PK'] = {}
        level['K'] = {}
        level['1'] = {}
        level['2'] = {}
        level['3'] = {}
        level['4'] = {}
        level['5'] = {}
    
#         i = 0
#         while i < len(Subjects):
#             for level in Grades:
#                 for clss in level:
#                     for sub in Subjects:
#                         level[clss][Subjects[i]] = 0
#             i += 1
   

#SPECIFIC GIVEN TIME DATA FROM SCHOOL
    def P_gen(): 
        Grades[0]['PK']['Reading{Gen}'] = ('9:20', '10:40')
        Grades[0]['PK']['Math{Gen}'] = ('12:50', '1:45')
        
    def K_gen():
        Grades[0]['K']['Reading{Gen}'] = ('9:00', '10:30')
        Grades[0]['K']['Win{Gen}'] = ('10:45','11:10')
        Grades[0]['K']['Reading{Sped}'] = ('11:55', '12:25')
        Grades[0]['K']['Math{Gen}'] = ('12:55','1:50' )
        Grades[0]['K']['SS{Gen}'] = ('2:35','3:20')
        
    def F_gen():
        Grades[0]['1']['Language Arts{Gen}'] = ('9:45','11:25')
        Grades[0]['1']['Win{Gen}'] = ('12:15', '12:45')
        Grades[0]['1']['Language Arts{Sped}'] = ('12:45', '1:15')
        Grades[0]['1']['SS{Gen}'] = ('1:15', '2:05')
        Grades[0]['1']['Math{Gen}'] = ('2:05', '3:20')
        
    def S_gen():
        Grades[0]['2']['Language Arts{Gen}{50}'] = ('8:35', '9:25')
        Grades[0]['2']['Win{Gen}{30}'] = ('9:25', '9:55')
        Grades[0]['2']['Language Arts{Gen}{70}'] = ('10:40','11:50')
        Grades[0]['2']['SS/SC{Gen}'] = ('11:50', '12:40')
        Grades[0]['2']['Win{Gen}'] = ('1:35', '2:05')
        Grades[0]['2']['Math{Gen}'] = ('2:05', '3:20')
    
    def T_gen():
        Grades[0]['3']['Language Arts{Gen}{120}'] = ('8:45', '10:45')
        Grades[0]['3']['Win{Gen}{30}'] = ('11:40', '12:10')
        Grades[0]['3']['Win{Gen}{15}'] = ('1:05', '1:20')
        Grades[0]['3']['SS/SC{Gen}'] = ('1:20', '2:10')
        Grades[0]['3']['Math{Gen}'] = ('2:10', '3:20')
        
    def Four_gen():
        Grades[0]['4']['Win{Gen}'] = ('8:35', '9:05')
        
    def Five_gen():
        Grades[0]['5']['Win{Gen}'] = ('10:10', '10:40')
        
    
    P_gen()
    K_gen()
    F_gen()
    S_gen()
    T_gen()
    Four_gen()
    Five_gen()
    return Grades

def del_method(grade, subject):
    del(Grades[0][grade][subject])

def get_time(grade, subject):
    return Grades[0][str(grade)][subject]

def get_courses(grade):
    return Grades[0][str(grade)]


set_up()
