import psycopg2
from openpyxl.workbook import Workbook
import pandas as pd
import logging
# importing packages

class Total_compensation:
    # function to list total compensation given at Department level till date
    def compensation(self):
        try:
            # trying to connect to postgresql database
            conn = psycopg2.connect(

                database="assignment",
                user="postgres",
                password="munna1998")
            cursor = conn.cursor()
            # connection established
            script = """
                    select dept.deptno, dept_name, sum(total_compensation) from Compensation, dept
                    where Compensation.dept_name=dept.dname
                    group by dept_name, dept.deptno
                    """
            # query to list total compensation given at Department level till date
            cursor.execute(script)

            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)
            # storing data in dataframe
            writer = pd.ExcelWriter('ques_4.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()
        # using the data frame to generate excel file
        except Exception as e:
            print("Error", e)

        finally:
            # after completion of above block,closing the connection
            if conn is not None:
                cursor.close()
                conn.close()
                #commit to the database
#main method
#creating an object of employees class and calling the compensation_by_dept method

if __name__ == '__main__':
    conn = None
    cur = None
    comp = Total_compensation()
    comp.compensation
    #call the meethod using paranthesis
