# 1.	Simulate a dataset with 100 customers. 
# The ID column should include customer IDs from a1 to a100. 
# Further, this dataset should include a second column indicating the months of 2016 for every customer. 
# Months should be of the format "2016-01-01"("YYYY-MM-DD"). 
# The final table should have one record per customer per month.
library(lubridate)

Cust_id <- paste("a", 1:100, sep = "")
Month <- seq(from = dmy("01-01-2016"), to = ymd("2016-12-31"), by="month")
MyTable <- expand.grid(Cust_id=Cust_id, Month=Month)

MyTable <- data.table(MyTable)
MyTable
