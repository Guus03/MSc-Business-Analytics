
# 1.	Please create the following sequences:
# a.	Use rep with x equals to 1:10, times equal to 2, and each equal to 3.
list1 <- rep(1:10, times = 2, each = 3)
list1
# b.	Use rnorm to generate 100 numbers with mean qual to 3, and sd equal to 1.
list2 <- rnorm(100, mean = 3, sd = 1)
list2
# c.	Put this two vectors together with the function c(), 
# then use sample() to pick 3 numbers out of all these numbers with replacement.
sample(c(list1,list2), 3)

# d.	Add set.seed() in your code to ensure that you will get the same 3 numbers every time. 
set.seed(123)
list1 <- rep(1:10, times = 2, each = 3)
list2 <- rnorm(100, mean = 3, sd = 1)
sample(c(list1,list2), 3)
