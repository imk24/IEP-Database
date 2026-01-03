View(R_out)

#View All Headers
names(R_out)

#View all subjects, grades, and associated teachers
x1 <- R_out[1:3]

View(x1)

#Replaces all blank teachers with entry 'Not Found'
x1[["Teacher.s."]][x1[["Teacher.s."]] == ""] <- "Not Found"
R_out[1:3] <- x1

View(R_out)
                              

