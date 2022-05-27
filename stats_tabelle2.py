import pandas as pnd
from pandasql import sqldf

df_excel_source = pnd.read_excel('D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle2')
pysqldf = lambda q: sqldf(q, globals())

Question_no = ['FCET1', 'FCET2', 'FCET3', 'FCET4', 'FCET5', 'FCET6', 'FCET7', 'FCET8', 'FCET9', 'FCET10',
               'FCET11', 'FCET12', 'FCET13', 'FCET14', 'FCET15', 'FCET16', 'FCET17', 'FCET18', 'FCET19',
               'FCET20', 'FCET21', 'FCET22', 'FCET23', 'FCET24']

Article = ['a', 'the', 'zero article']


# return dataframe: Article, frequency, percentage for each Question_no
# (the article x which means the participant didn't make any choice is not processed in this project)
def stat_tabelle2():
    df_result = pnd.DataFrame(columns=['Question_no', 'Article', 'frequency', 'percentage'])
    i = 0
    for qst in Question_no:
        for art in Article:
            # Number of participants by age
            q = "SELECT Count(*) as article_count " \
                "FROM df_excel_source " \
                "WHERE df_excel_source.{0} = '{1}';"
            q = q.format(qst, art)
            qResult = pysqldf(q)
            df_result = pnd.concat([df_result, pnd.DataFrame(
                {'Question_no': qst, 'Article': art, 'frequency': qResult['article_count'][0],
                 'percentage': qResult['article_count'][0] * 100 / 133}, index=[i])])
            i = i + 1
    with pnd.ExcelWriter(r'D:\MIRELA\results\Tabelle2_Statistics.xlsx') as writer:
        # df_result.to_excel(writer, sheet_name='FREQUENCY', index=False)
        df_result.to_excel(writer, sheet_name='PERCENTAGE', index=False)
    return df_result


# return dataframe: statistics about definite (+ and -) and specific (+ and -)questions
def stat_definite_specific():
    df_result = pnd.DataFrame(columns=['category', 'the', 'a', 'zero article'])
    df_source = stat_tabelle2().head(48)
    category = ['+definite +specific', '+definite -specific', '-definite +specific', '-definite -specific']
    i = 1
    j = 0
    for c in category:
        list_question = ['FCET' + str(i), 'FCET' + str(i + 1), 'FCET' + str(i + 2), 'FCET' + str(i + 3)]
        i = i + 4
        df_temp = df_source[df_source['Article'] == 'a']
        df_temp = df_temp[
            (df_temp['Question_no'] == list_question[0]) | (df_temp['Question_no'] == list_question[1]) | (
                    df_temp['Question_no'] == list_question[2]) | (df_temp['Question_no'] == list_question[3])]
        # print(df_temp)
        df_temp2 = df_source[df_source['Article'] == 'the']
        df_temp2 = df_temp2[
            (df_temp2['Question_no'] == list_question[0]) | (df_temp2['Question_no'] == list_question[1]) | (
                    df_temp2['Question_no'] == list_question[2]) | (df_temp2['Question_no'] == list_question[3])]
        # print(df_temp2)
        df_temp3 = df_source[df_source['Article'] == 'zero article']
        df_temp3 = df_temp3[
            (df_temp3['Question_no'] == list_question[0]) | (df_temp3['Question_no'] == list_question[1]) | (
                    df_temp3['Question_no'] == list_question[2]) | (df_temp3['Question_no'] == list_question[3])]
        df_result = pnd.concat([df_result, pnd.DataFrame({'category': c,
                                                          'the': df_temp2['percentage'].sum() / 4,
                                                          'a': df_temp['percentage'].sum() / 4,
                                                          'zero article': df_temp3['percentage'].sum() / 4},
                                                         index=[j])])
        j = j + 1
    return df_result


print(stat_definite_specific())
