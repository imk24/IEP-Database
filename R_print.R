#Start off by making a copy of the data frame
df <- R_out
View(R_out)


#View All Headers
names(df)

#View all subjects, grades, and associated teachers
x1 <- df[1:3]

View(x1)

#Replaces all blank teachers with entry 'Not Found'
x1[["Teacher.s."]][x1[["Teacher.s."]] == ""] <- "Not Found"

df[1:3] <- x1

r_count <- nrow(df)

#Now getting rid of all of the na's to clean up the chart
x1 <- df[4:r_count]

x1[is.na(x1)] <- ""

df[4:r_count] <- x1

#Final Product
View(df)
                              

