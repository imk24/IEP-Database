# IEP-Database
A database for tracking IEP students. This includes class times, minutes per week, teachers, etc... This database also takes into account associated teachers for subjects as well as the students in said subjects. Data can output into a txt or R Format Chart, up to user to decide. This is a small-scale database.

Quick guidlines are methods:

Time method is the first method made used to track and implement time. Steps are in increments of 5

Teacher method builds a “Teacher object” using name and grade for creation same instance for student method which builds “Student object”

Students: takes a given student (s) and the overall Student List and adds the student to said student list

Add_courses: takes a “Teacher object” and the courses given start and end time. If time slot is taken it outputs “Time slot is taken”. If there is a prior course already given, the new course and times are added into the Teacher’s times

Teachers: adds teachers into overarching teachers list

Find_courses: Uses the IEP_setup.time method to check if the subject has a designated time slot

Add_student: takes a given student name and a given subject and time slot. If time slot and subject available returns class added and adds student into Teachers class. Else prints “Time slot” unavailable if time slot is full or not found. And “Role: name not found” if student or teacher object not created

Rem_person: takes a given name and removes said person from the entire entry. If it is a student it displays all student information as well as classes student is in. If it is a teacher it displays all teacher information, time slots, classes, and associated students in classes. 

Make_dict:  Creates a data sheet that displays all grade levels and associated teachers, subjects, and students in classes

Get_all: takes a name and displays all associated information of the person. If teacher it displays the name, grade, and all subjects taught as well as allocated time and students for subject. If student it displays name, grade, and all subjects the student is in as well as time and points.


Now for use of the project all you need is a txt file which consits of student and teacher names, subjects, and duration. This is the appropriate format: Role, Grade, Name, Class, Minutes. If adding multiple keep the format and seperate with a space. 

Student, 1, Kim, Math{Gen} Reading{Gen} Reading{Sped} Math{Sped} SS{Gen} SS{Sped}, 150 150 150 150 150 150
Student, 1, Justin, SS{Sped} SS{Sped} Reading{Gen}, 75 50 150

Once data is input, change the times in the IEP_setup file to specific times. 

When wanting to print the data simply either use the IEP_file or IEP_sched. IEP_file prints it out into a txt.format, while IEP_sched prints out in a csv.format which can then be displayed in a Excel or R_chart.


Some quick fixes if the code stops.

Some issues:
The code may have problems in the IEP_sched where it runs out of index. Just change the R_format method specifically this line. 
file.write(total_subs[i] + ",".join([','] * (len(students) -15)) + "\n") 
You may have to write this to check if all lines are equal, simple decode:
print(len(lines[0]))
print(len(lines[1]))
and change accordingly.

You may also run into problems with the file itself and names missing:
Please include anyone doing special education at the top prior to other subjects, IE:

*Also include this at the very top
Role, Grade, Name, Class, Minutes
Teacher, K, AbrahamB, Sped
Teacher, K, BrittanyL, Math{Gen}

I'd reccomend changing the times as well as changing the way you wanted outputted. The style I had was specific but the way the code is written it should allow for minor changes, ie: adding getting rid of courses, grade levels, etc...




