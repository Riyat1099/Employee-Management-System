import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
c=mydb.cursor()#c is object, cursor is class
# the above code is common, rest further operation begins:
# to retrive data
#c.execute("select * from details")#for cursor class there is execute function in that execute function you need to add sql query)
#mydata=c.fetchall() # all the details are retrieved in c object and it will fetch all data in c object, fetchall function will return all the data stored inside itself)
#mycolumns=c.column_names # it is a tuple and it is going to return the column lables

# here we get columns and data seperately and we need a organised data so we need to install pandas
 #import pandas at the starting of the code
#df=pd.DataFrame(data=mydata,columns=mycolumns)
#print(df)
#to send somedata(to add a new row in data base)
e_id=input("Enter employee id")
e_password=input("Enter employee password")
e_name=input("Enter employee name")
e_salary=input("Enter employee salary")
c.execute("insert into details values(%s,%s,%s,%s)",(e_id,e_password,e_name,e_salary))
mydb.commit() # to save the changes made
