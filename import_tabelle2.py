import pandas as pnd
from pandasql import sqldf

df_excel_source = pnd.read_excel('D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle2')
pysqldf = lambda q: sqldf(q, globals())

Question_no = ['FCET1', 'FCET2', 'FCET3', 'FCET4', 'FCET5', 'FCET6', 'FCET7', 'FCET8', 'FCET9', 'FCET10',
               'FCET11', 'FCET12', 'FCET13', 'FCET14', 'FCET15', 'FCET16', 'FCET17', 'FCET18', 'FCET19',
               'FCET20', 'FCET21', 'FCET22', 'FCET23', 'FCET24']

Article = ['a', 'the', 'zero article']

df_result = pnd.DataFrame(columns=['Question_no', 'Article', 'frequency'])

for qst in Question_no:
    for art in Article:
        # Number of participants by age
        q = "SELECT Count(*) as article_count " \
            "FROM df_excel_source " \
            "WHERE df_excel_source.{0} = '{1}';"
        q = q.format(qst, art)
        qResult = pysqldf(q)
        df_result = pnd.concat([df_result, pnd.DataFrame(
            {'Question_no': qst, 'Article': art, 'frequency': qResult['article_count'][0]}, index=[0])])

df_result_percentage = pnd.DataFrame(columns=['Question_no', 'Article', 'percentage'])

for qst in Question_no:
    for art in Article:
        # Number of participants by age
        q = "SELECT Count(*) as article_count " \
            "FROM df_excel_source " \
            "WHERE df_excel_source.{0} = '{1}';"
        q = q.format(qst, art)
        qResult = pysqldf(q)
        df_result_percentage = pnd.concat([df_result_percentage, pnd.DataFrame(
            {'Question_no': qst, 'Article': art, 'percentage': qResult['article_count'][0] * 100 / 133}, index=[0])])

with pnd.ExcelWriter(r'D:\MIRELA\results\Tabelle2_Statistics.xlsx') as writer:
    df_result.to_excel(writer, sheet_name='FREQUENCY', index=False)
    df_result_percentage.to_excel(writer, sheet_name='PERCENTAGE', index=False)

print(df_result_percentage)
