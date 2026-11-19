# setwd("your path here")
# Load libraries
library(data.table)
library(lubridate)
library(randomNames)
library(stringr)

# 1 Load the file "demographics.csv" and add a column Names with the random names for each customer.
participants <- fread("Applied-Programming/R-Seminar-10/participants_list.csv")
demo <- fread("Applied-Programming/R-Seminar-10/demographics.csv")
demo
demo$Names <- randomNames(length(demo), gender = demo$Gender)
demo

# 2.	Split the column Names into two columns (one for the first name, another one for the last name) 
# by using the command str_split_fixed() and save the output as a data.table named customer_names. 
# Rename the first column First_Name, and the second column Last_Name.

customer_names <- data.table(str_split_fixed(demo$Names, ",", 2))
setnames(customer_names, old = c("V1", "V2"), new = c("Last_Name", "First_Name"))
setcolorder(customer_names, c("First_Name", "Last_Name"))

head(customer_names)
