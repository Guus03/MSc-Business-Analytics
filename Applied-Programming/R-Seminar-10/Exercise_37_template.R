library(data.table)

# Read-in data
participants <- fread("Applied-Programming/R-Seminar-10/participants_list.csv")
participants[, name := paste(`First Name`, `Last Name`)]


# 1. Extend the function which samples student names. Add another argument to specify the number of students’ names being drawn. 
# Set a default for this argument, i.e., if not specified 5 student names should be returned.
pick_a_random_student <- function(names, n = 5){
  student <- sample(names, n, replace = FALSE)
  return(student)}


pick_a_random_student(participants[,name], 4) # Test your function
