import pandas as pnd
from pandasql import sqldf

df_excel_source = pnd.read_excel('D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle1')
pysqldf = lambda q: sqldf(q, globals())


# Number of participants by age
q="SELECT df_excel_source.'Age', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count " \
  "FROM df_excel_source " \
  "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
  "GROUP BY df_excel_source.'Age';"

qResult = pysqldf(q)
print(qResult, "\n")

# d1 = pnd.DataFrame(qResult)
# with pnd.ExcelWriter(r'D:\MIRELA\results\result.xlsx', if_sheet_exists="overlay", engine="openpyxl", mode="a",
#                      engine_kwargs={"keep_vba": True}) as writer:
#     d1.to_excel(writer, sheet_name="result", index=False)

# Number of participants by year of study
q = "SELECT df_excel_source.'Year Of Study', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count " \
    " FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'Year Of Study';"
qResult = pysqldf(q)
print(qResult, "\n")
# d1 = pnd.DataFrame(qResult)
# d1.to_excel(r'D:\MIRELA\results\result.xlsx',index=False)
# with pnd.ExcelWriter(r'D:\MIRELA\results\result.xlsx', if_sheet_exists="overlay", engine="openpyxl", mode="a",
#                      engine_kwargs={"keep_vba": True}) as writer:
#     d1.to_excel(writer, sheet_name="result", index=False)

# Number of participants by Gender
q = "SELECT df_excel_source.'Gender', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count " \
    " FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'Gender';"
qResult = pysqldf(q)
print(qResult, "\n")

# Number of participants by University Department
q = "SELECT df_excel_source.'University Department', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) )as Participants_Count " \
    " FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'University Department';"
qResult = pysqldf(q)
print(qResult, "`\n")

# Number of participants by Level of Study
q = "SELECT df_excel_source.'Level of Study', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count " \
    " FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'Level of Study';"
qResult = pysqldf(q)
print(qResult, "\n")

# Number of participants by Year of study
q = "SELECT df_excel_source.'Year of study', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count  " \
    "FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'Year of study';"
qResult = pysqldf(q)
print(qResult, "\n")

# Number of participants by Age of First Exposure to English
q = "SELECT df_excel_source.'Age of First Exposure to English', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count " \
    " FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'Age of First Exposure to English' " \
    "ORDER BY df_excel_source.'Age of First Exposure to English' ;"
qResult = pysqldf(q)
print(qResult, "\n")

# Number of participants by L1
q = "SELECT df_excel_source.'L1', (cast (Count(*) as float) * 100 / cast((select count(*) from df_excel_source WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL )as float) ) as Participants_Count  " \
    "FROM df_excel_source " \
    "WHERE df_excel_source.'Additional Notes'!='EXCLUDED' or df_excel_source.'Additional Notes' IS NULL " \
    "GROUP BY df_excel_source.'L1';"
qResult = pysqldf(q)
print(qResult, "\n")
