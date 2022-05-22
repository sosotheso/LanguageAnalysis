import pandas as pnd

# df = pnd.read_excel('D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle2')
# pysqldf = lambda q: sqldf(q, globals())
#
# # Number of participants by age
# q = "SELECT df_excel_source.'FCET-1', Count(*) as article_count " \
#     "FROM df_excel_source " \
#     "WHERE df_excel_source.'FCET-1'=='a' " \
#     "GROUP BY df_excel_source.'FCET-1';"
#
# qResult = pysqldf(q)
# print(qResult, "\n")
# print(qResult['article_count'][0])

df = pnd.DataFrame(columns=['A', 'B'])

for i in range(5):
    df = pnd.append({'A': i, 'B': i+1}, ignore_index=True)

print(df)
