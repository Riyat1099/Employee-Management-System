import streamlit as st
import mysql.connector
import datetime
import pandas as pd
st.title("Employee Management System")
choice=st.sidebar.selectbox("My Menu",("HOME","EMPLOYEE","ADMIN"))
if(choice=="HOME"):
    st.image("https://kredily.com/wp-content/uploads/2023/01/emp-mng-sys-1024x585.png")
    st.write("This application is used for employee management system")
elif(choice=="EMPLOYEE"):
    if"login" not in st.session_state:
        st.session_state['login']=False
    eid=st.text_input("Enter employeee id")
    pwd=st.text_input("Enter employee password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
        c=mydb.cursor()
        c.execute("select * from details")
        d=c.fetchall()
        #st.write(d)
        for r in d:
            if(r[0]==eid and r[1]==pwd):
                st.session_state['login']=True
                break
        if(not st.session_state['login']):
            st.write("Incorrect Id or Password")
        if(st.session_state['login']):
            st.write("Login Successfull")
            choice2=st.selectbox("Features",("View Profile","Apply for leave"))
            if(choice2=="View Profile"):
                mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
                c=mydb.cursor()
                c.execute("select * from details where id=%s",(eid,))# , is used to make it look like a tuple
                d=c.fetchall()[0]
                st.write("Name:",d[2])
                st.write("Employee ID:",d[0])
                st.write("Password:",d[1])
                st.write("Salary:",d[3])
            elif(choice2=="Apply for leave"):
                desc=st.text_input("Enter Description for leave")
                btn2=st.button("Apply")
                if btn2:
                    dt=str(datetime.datetime.now())
                    mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
                    c=mydb.cursor()
                    c.execute("insert into leave_app values(%s,%s,%s)",(dt,eid,desc))#import package datetime
                    mydb.commit()
                    st.success("Leave Applied Successfully")
elif(choice=="ADMIN"):
    if"login2" not in st.session_state:
        st.session_state['login2']=False
    eid=st.text_input("Enter Admin Id")
    pwd=st.text_input("Enter Admin Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
        c=mydb.cursor()
        c.execute("select * from admins")
        d=c.fetchall()
        for r in d:
            if(r[0]==eid and r[1]==pwd):
                st.session_state['login2']=True
                break
        if(not st.session_state['login2']):
            st.write("Incorrect Id or Password")
        if(st.session_state['login2']):
            st.write("Login Successfull")
            choice2=st.selectbox("Features",("View Employee","Add Employee"))
            if(choice2=="View Employee"):
                mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
                c=mydb.cursor()
                c.execute("select * from details")# , is used to make it look like a tuple
                c.fetchall()
                df=pd.DataFrame(data=c.fetchall(),columns=c.column_names)
                st.dataframe(df)
            elif(choice2=="Apply for leave"):
                desc=st.text_input("Enter Description for leave")
                btn2=st.button("Apply")
                if btn2:
                    dt=str(datetime.datetime.now())
                    mydb=mysql.connector.connect(host="localhost",user="root",password="mumbaikar@1099",database="ems")
                    c=mydb.cursor()
                    c.execute("insert into details values(%s,%s,%s)",(eis,pwd,name,desc))#import package datetime
                    mydb.commit()
                    st.success("Successfully")
                    
