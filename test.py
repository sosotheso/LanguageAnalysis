import statistics as st

import pandas as pnd
from pandasql import sqldf

# Import Excel Data to a dataframe
df_excel_source = pnd.read_excel(r'D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle1')

# Filter Excluded rows
df_excel_source = df_excel_source[df_excel_source['Additional Notes'] != 'EXCLUDED']

# Remove right and left blanks
df_excel_source['Participant No.'] = df_excel_source['Participant No.'].str.rstrip()
df_excel_source['Participant No.'] = df_excel_source['Participant No.'].str.lstrip()
df_excel_source['University Department'] = df_excel_source['University Department'].str.rstrip()
df_excel_source['University Department'] = df_excel_source['University Department'].str.lstrip()
df_excel_source['Gender'] = df_excel_source['Gender'].str.rstrip()
df_excel_source['Gender'] = df_excel_source['Gender'].str.lstrip()
df_excel_source['Level of Study'] = df_excel_source['Level of Study'].str.rstrip()
df_excel_source['Level of Study'] = df_excel_source['Level of Study'].str.lstrip()
df_excel_source['L1'] = df_excel_source['L1'].str.rstrip()
df_excel_source['L1'] = df_excel_source['L1'].str.lstrip()
df_excel_source['Additional Notes'] = df_excel_source['Additional Notes'].str.rstrip()
df_excel_source['Additional Notes'] = df_excel_source['Additional Notes'].str.lstrip()

pysqldf = lambda q: sqldf(q, globals())


# stat_year_of_study(): year of study statistics
def stat_year_of_study():
    # Number of participants by year of study
    q = "SELECT df_excel_source.'Year Of Study', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "GROUP BY df_excel_source.'Year Of Study';"
    qResult = pysqldf(q)
    print(qResult, "\n")


# stat_gender(): Gender statistics
def stat_gender():
    # Number of participants by Gender
    q = "SELECT df_excel_source.'Gender', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "GROUP BY df_excel_source.'Gender';"
    qResult = pysqldf(q)
    print(qResult, "\n")


# stat_university_department : University Department statistics
def stat_university_department():
    # Number of participants by University Department
    q = "SELECT df_excel_source.'University Department', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "GROUP BY df_excel_source.'University Department';"
    qResult = pysqldf(q)
    print(qResult, "\n")


#  stat_level_study:Level of Study statistics
def stat_level_study():
    # Number of participants by Level of Study
    q = "SELECT df_excel_source.'Level of Study', Count(*) as Participants_Count " \
        " FROM df_excel_source " \
        "GROUP BY df_excel_source.'Level of Study';"
    qResult = pysqldf(q)
    print(qResult, "\n")


# stat_age_english(): first exposure to English statistics
def stat_age_english():
    d_temp = df_excel_source[(df_excel_source['Age of First Exposure to English'] != 'Early age') & (
            df_excel_source['Age of First Exposure to English'] != 'I don\'t remember')]
    # print(d_temp)
    # print(type(d_temp))
    q = "SELECT MAX(d_temp.'Age of First Exposure to English') as MaxAge " \
        "FROM d_temp;"
    qResult1 = sqldf(q, locals())

    q = "SELECT MIN(d_temp.'Age of First Exposure to English') as MinAge " \
        "FROM d_temp ;"
    qResult2 = sqldf(q, locals())

    print('Age of first exposure to English statistics : \n')
    print('Range : ', qResult2['MinAge'][0], ' - ', qResult1['MaxAge'][0])
    AgeList = d_temp['Age of First Exposure to English'].to_list()
    print('Median:', st.median(AgeList))
    print('Mean is : M = ', st.mean(AgeList))

    # Number of participants by Age of First Exposure to English

    q = "SELECT d_temp.'Age of First Exposure to English', Count(*) as Participants_Count " \
        " FROM d_temp " \
        "GROUP BY d_temp.'Age of First Exposure to English';"
    qResult = sqldf(q, locals())
    print(qResult, "\n")


# stat_l1 : L1 statistics
def stat_l1():
    q = "SELECT df_excel_source.'L1', Count(*) as Participants_Count  " \
        "FROM df_excel_source " \
        "GROUP BY df_excel_source.'L1';"
    qResult = pysqldf(q)
    print(qResult, "\n")


# statAge()  : Age statistics
def stat_age():
    q1 = "SELECT MAX(df_excel_source.'Age') as MaxAge " \
         "FROM df_excel_source ;"
    qResult1 = pysqldf(q1)

    q2 = "SELECT MIN(df_excel_source.'Age') as MinAge " \
         "FROM df_excel_source ;"
    qResult2 = pysqldf(q2)

    print('age range : ', qResult2['MinAge'][0], ' - ', qResult1['MaxAge'][0])
    AgeList = df_excel_source['Age'].to_list()
    print('Age Median is :', st.median(AgeList))
    print('Age Mean is : M = ', st.mean(AgeList))

    # Number of participants by age
    q3 = "SELECT df_excel_source.'Age', Count(*) as Participants_Count " \
         "FROM df_excel_source " \
         "GROUP BY df_excel_source.'Age';"
    qResult = pysqldf(q3)
    print(qResult, "\n")



