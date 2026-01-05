#Using R To sharpen output
df <- R_out

#View All Headers
names(df)

#View all subjects, grades, and associated teachers
x1 <- df[1:3]

View(x1)

#Replaces all blank teachers with entry 'Not Found'
x1[["Teacher.s."]][x1[["Teacher.s."]] == ""] <- "Not Found"

df[1:3] <- x1

#Subtract by two to not include start and end time col headers.
x = ncol(df) - 2
#Now getting rid of all of the na's to clean up the chart
x1 <- df[3:x]

x1[is.na(x1)] <- ""

df[3:x] <- x1

#Final Product
View(df)

