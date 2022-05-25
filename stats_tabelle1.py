import statistics as st
import pandas as pnd
from pandasql import sqldf

df_excel_source = pnd.read_excel(r'D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle1')
pysqldf = lambda q: sqldf(q, globals())


# stat1() : Number of participantes by age, year of study, gender ...
def stat1():
    # Number of participants by age
    q = "SELECT df_excel_source.'Age', Count(*) as Participants_Count " \
        "FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'Age';"
    qResult = pysqldf(q)
    print(qResult, "\n")

    # Number of participants by year of study
    q = "SELECT df_excel_source.'Year Of Study', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'Year Of Study';"
    qResult = pysqldf(q)
    print(qResult, "\n")

    # Number of participants by Gender
    q = "SELECT df_excel_source.'Gender', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'Gender';"
    qResult = pysqldf(q)
    print(qResult, "\n")

    # Number of participants by University Department
    q = "SELECT df_excel_source.'University Department', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'University Department';"
    qResult = pysqldf(q)
    print(qResult, "`\n")

    # Number of participants by Level of Study
    q = "SELECT df_excel_source.'Level of Study', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'Level of Study';"
    qResult = pysqldf(q)
    print(qResult, "\n")

    # Number of participants by Year of study
    q = "SELECT df_excel_source.'Year of study', Count(*) as Participants_Count  " \
        "FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'Year of study';"
    qResult = pysqldf(q)
    print(qResult, "\n")

    # Number of participants by Age of First Exposure to English
    q = "SELECT df_excel_source.'Age of First Exposure to English', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'Age of First Exposure to English';"
    qResult = pysqldf(q)
    print(qResult, "\n")

    # Number of participants by L1
    q = "SELECT df_excel_source.'L1', Count(*) as Participants_Count  " \
        "FROM df_excel_source " \
        "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
        "GROUP BY df_excel_source.'L1';"
    qResult = pysqldf(q)
    print(qResult, "\n")


# stat2()  : age (range, medium, median) + age of first exposure to english (range, medium, median)
def stat2():
    q1 = "SELECT MAX(df_excel_source.'Age') as MaxAge " \
         "FROM df_excel_source " \
         "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL ;"
    qResult1 = pysqldf(q1)

    q2 = "SELECT MIN(df_excel_source.'Age') as MinAge " \
         "FROM df_excel_source " \
         "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL ;"
    qResult2 = pysqldf(q2)

    print('age range : ', qResult2['MinAge'][0], ' - ', qResult1['MaxAge'][0])
    df_src=df_excel_source[df_excel_source['Additional Notes'] != 'EXCLUDED']
    AgeList= df_src['Age'].to_list()
    print('Age Median is :', st.median(AgeList))
    print('Age Mean is : M = ', st.mean(AgeList))



stat2()
