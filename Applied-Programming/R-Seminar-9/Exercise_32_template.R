library(data.table)
library(lubridate)
getwd()

# 1.	Read in participants_list.csv. 
participants <- fread("Applied-Programming/R-Seminar-9/participants_list.csv")
setnames(participants,c("first","last","gender"))
participants[,name := paste(first,last)]
participants


# 2. Create a variable q.type that can be set to either of 2 values: theory or coding. 
q.type <- "theory"


# 3. Write an if else statement
# If we provide a theory question, make sure that a male participant (gender = 1) is drawn,
# if it's a coding question, 
# make sure a girl (gender = 0) will answer the question.
# To randomly draw an element, use sample(x, size = 1).
if(q.type=="coding"){
  sample(participants[gender== 0, name], 1) 
} else{
  sample(participants[gender== 1, name], 1) 
}


# 4. Introduce a variable q.difficulty with values difficult or easy. 
q.difficulty <- "difficult"
q.difficulty <- "easy"
q.type <- "coding"

# If the question is difficult, the question should go to both
# male and female participants (independent of q.type).  

if(q.difficulty=="difficult"){                          # if question is "difficult"
  sample(participants[,first], 1)              # question can go to male and female participants
} else if(q.type=="coding"){                      # if question not "difficult" and question is theory 
  sample(participants[gender==0, name], 1)   # select male participants
}else {
  sample(participants[gender==1, name], 1)   # otherwise female participant
}


