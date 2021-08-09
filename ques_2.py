import psycopg2
import logging
from openpyxl.workbook import Workbook
import pandas as pd
# importing packages

class Total_compensation:
    # function to list the Total compensation given till his/her last date or till now and store it in a excel file
    def compensation(self):
        try:
            # trying to connect to postgresql database
            conn = psycopg2.connect(
                host="localhost",
                database="assignment",
                user="postgres",
                password="munna1998")
            cur = conn.cursor()
            # connection established
            script = """select emp.ename, emp.empno, dept.dname, (case when enddate is not null then ((enddate-startdate+1)/30)*(jobhist.sal) else ((current_date-startdate+1)/30)*(jobhist.sal) end)as Total_Compensation,
(case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp 
where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno"""
            # query to list the Total compensation given till his/her last date or till now and store it in a excel file
            cur.execute(script)




            columns = [desc[0] for desc in cur.description]
            data = cur.fetchall()
            df = pd.DataFrame(list(data), columns=columns)
            # storing data in dataframe

            writer = pd.ExcelWriter('ques_2.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()
            # storing data in dataframe

        except Exception as e:
            # if exception thrown in try block
            logging.error("Error", e)
        finally:
            # after completion of above block,closing the connection
            if conn is not None:
                cur.close()
                conn.close()

#main method
#creating an object of employees class and calling the emp_manager method
if __name__=='__main__':
    conn = None
    cur = None
    comp = Total_compensation()
    comp.compensation()








