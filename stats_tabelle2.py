import pandas as pd
import pandas as pnd
from pandasql import sqldf
from scipy import stats
from statsmodels.stats.anova import AnovaRM

df_excel_source = pnd.read_excel('D:\MIRELA\MainFile.xlsx', sheet_name='Tabelle2')
pysqldf = lambda q: sqldf(q, globals())

Question_no = ['FCET1', 'FCET2', 'FCET3', 'FCET4', 'FCET5', 'FCET6', 'FCET7', 'FCET8', 'FCET9', 'FCET10',
               'FCET11', 'FCET12', 'FCET13', 'FCET14', 'FCET15', 'FCET16', 'FCET17', 'FCET18', 'FCET19',
               'FCET20', 'FCET21', 'FCET22', 'FCET23', 'FCET24']

Article = ['a', 'the', 'zero article']
sub_article = ['a', 'the']


# return dataframe: Article, frequency, percentage for each Question_no
# (the article x which means the participant didn't make any choice is not processed in this project)
def stat_tabelle2():
    df_result = pnd.DataFrame(columns=['Question_no', 'Article', 'frequency', 'percentage'])
    i = 0
    for qst in Question_no:
        for art in Article:
            # Number of article by question
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
    i = 0
    j = 0
    for c in category:
        df_temp = df_source[df_source['Article'] == 'a'].iloc[i:i + 4]
        print(df_temp)
        df_temp2 = df_source[df_source['Article'] == 'the'].iloc[i:i + 4]
        print(df_temp2)
        df_temp3 = df_source[df_source['Article'] == 'zero article'].iloc[i:i + 4]
        print(df_temp3)
        df_result = pnd.concat([df_result, pnd.DataFrame({'category': c,
                                                          'the': df_temp2['percentage'].sum() / 4,
                                                          'a': df_temp['percentage'].sum() / 4,
                                                          'zero article': df_temp3['percentage'].sum() / 4},
                                                         index=[j])])
        j = j + 1
        i = i + 4
    return df_result


# paired two tailed t test for means (definite + specific versus definite -specific)
#                                    (indefinite +specific versus indefinite -specific)
def t_test_specificity():
    for art in Article:
        print('Paired t-test for ', art, '\n')
        df_test = (df_excel_source.iloc[:, 0:17]).replace(art, 1)
        df_test.iloc[:, 1:] = (df_test.iloc[:, 1:]).replace(to_replace=r'.*', value=0, regex=True)
        # print(df_test)
        df_temp = pnd.DataFrame(columns=['Participant', '+d+s', '+d-s', '-d+s', '-d-s'])
        df_temp['Participant'] = df_test['Participant No.']
        df_temp['+d+s'] = df_test.iloc[:, 1:5].sum(axis=1)
        df_temp['+d-s'] = df_test.iloc[:, 5:9].sum(axis=1)
        df_temp['-d+s'] = df_test.iloc[:, 9:13].sum(axis=1)
        df_temp['-d-s'] = df_test.iloc[:, 13:17].sum(axis=1)

        t_test_the_d = stats.ttest_rel(df_temp['+d+s'].to_numpy(), df_temp['+d-s'].to_numpy(), alternative='two-sided')
        print('Definite context : -specific vs +specific : ', t_test_the_d)

        t_test_the_ind = stats.ttest_rel(df_temp['-d+s'].to_numpy(), df_temp['-d-s'].to_numpy(),
                                         alternative='two-sided')
        print('InDefinite context : -specific vs +specific : ', t_test_the_ind, '\n')


def anova_new():
    result = list()
    for art in sub_article:
        print('ANOVA test for ', art, '\n')
        df_test = (df_excel_source.iloc[:, 0:17]).replace(art, 1)
        df_test.iloc[:, 1:] = (df_test.iloc[:, 1:]).replace(to_replace=r'.*', value=0, regex=True)
        df_temp = pnd.DataFrame(columns=['Participant', '+d+s', '+d-s', '-d+s', '-d-s'])
        df_temp['Participant'] = df_test['Participant No.']
        df_temp['+d+s'] = df_test.iloc[:, 1:5].sum(axis=1)
        df_temp['+d-s'] = df_test.iloc[:, 5:9].sum(axis=1)
        df_temp['-d+s'] = df_test.iloc[:, 9:13].sum(axis=1)
        df_temp['-d-s'] = df_test.iloc[:, 13:17].sum(axis=1)
        # print(df_temp)
        # create dataframe : ANOVA test input--------------------------------------------------------------
        df_temp2 = pnd.DataFrame(columns=['Participant', 'definiteness', 'specificity', art])
        l = len(df_temp.iloc[:, 0:1])
        for i in range(0, l):
            for j in range(1, 5):
                df_temp2 = pnd.concat([df_temp2, pnd.DataFrame({'Participant': df_temp['Participant'].iloc[i],
                                                                'definiteness': (df_temp.columns[j])[0:2],
                                                                'specificity': (df_temp.columns[j])[2:4],
                                                                art: (df_temp[df_temp.columns[j]]).iloc[i]},
                                                               index=[j + i * 4])])

        df_temp2[art] = pnd.to_numeric(df_temp2[art])
        print(df_temp2)
        # ------------------------------------------------------------------------------------------------
        print('ANOVA test for specificity * definiteness \n')
        # perform repeated two-way ANOVA

        # model = ols(art + ' ~ C(definiteness) + C(specificity) + C(definiteness):C(specificity)', data=df_temp2).fit()
        # print(sm.stats.anova_lm(model, typ=2))

        model = AnovaRM(df_temp2, art, 'Participant', within=['definiteness', 'specificity'])
        res2way = model.fit()
        result.append(res2way)
    return result


# statistics for : +d+s previous mention definite (simple definite , q17-q20) ,
#                  -d-s first mention indefinite (simple indefinite) q21-q24
def stat_def_indef():
    df_result = pnd.DataFrame(columns=['category', 'the', 'a', 'zero article'])
    df_source = stat_tabelle2().iloc[48:, :]
    # print(df_source)
    category = ['+definite +specific simple definite ', '-definite -specific simple indefinite']
    i = 0
    j = 0
    for c in category:
        df_temp = df_source[df_source['Article'] == 'a'].iloc[i:i + 4]
        # print(df_temp)
        df_temp2 = df_source[df_source['Article'] == 'the'].iloc[i:i + 4]
        # print(df_temp2)
        df_temp3 = df_source[df_source['Article'] == 'zero article'].iloc[i:i + 4]
        # print(df_temp3)
        df_result = pnd.concat([df_result, pnd.DataFrame({'category': c,
                                                          'the': df_temp2['percentage'].sum() / 4,
                                                          'a': df_temp['percentage'].sum() / 4,
                                                          'zero article': df_temp3['percentage'].sum() / 4},
                                                         index=[j])])
        j = j + 1
        i = i + 4
    return df_result


# paired two tailed t test for means (+definite + specific: simple definite versus obligatory definite)
#                                    (-definite -specific: simple indefinite versus obligatory indefinite )
def t_test_definiteness_type():
    for art in Article:
        print('Paired t-test for ', art, '\n')
        df_test = pnd.concat(
            [
                (df_excel_source.iloc[:, 0:5]).replace(art, 1), (df_excel_source.iloc[:, 13:17]).replace(art, 1),
                (df_excel_source.iloc[:, 17:25]).replace(art, 1)
            ], axis=1
        )
        df_test.iloc[:, 1:] = (df_test.iloc[:, 1:]).replace(to_replace=r'.*', value=0, regex=True)
        # print(df_test)
        # test

        df_temp = pnd.DataFrame(
            columns=['Participant', '+d+s obligatory', '-d-s obligatory', '+d+s simple', '-d-s simple'])
        df_temp['Participant'] = df_test['Participant No.']
        df_temp['+d+s obligatory'] = df_test.iloc[:, 1:5].sum(axis=1)
        df_temp['-d-s obligatory'] = df_test.iloc[:, 5:9].sum(axis=1)
        df_temp['+d+s simple'] = df_test.iloc[:, 9:13].sum(axis=1)
        df_temp['-d-s simple'] = df_test.iloc[:, 13:17].sum(axis=1)
        # print(df_temp)
        t_test_the_d = stats.ttest_rel(df_temp['+d+s obligatory'].to_numpy(), df_temp['+d+s simple'].to_numpy(),
                                       alternative='two-sided')
        print('Definite context : obligatory definite vs simple definite : ', t_test_the_d)
        # #
        t_test_the_ind = stats.ttest_rel(df_temp['-d-s obligatory'].to_numpy(), df_temp['-d-s simple'].to_numpy(),
                                         alternative='two-sided')
        print('InDefinite context : obligatory indefinite vs simple indefinite : ', t_test_the_ind, '\n')


# we are expecting at least a score of 2/4 for each participant for each category question
# (example : q1 q2 q3 q4 , expectation of at least  2/4 correct answers)
#
def percentage_correct_answer_by_category():
    df_temp = pnd.DataFrame(columns=['Participant', '+d+s', '+d-s', '-d+s', '-d-s', 'q17q20', 'q21q24'])
    # +D+S +D-S processing
    df_test = (df_excel_source.iloc[:, 0:9]).replace('the', 1)
    df_test.iloc[:, 1:] = (df_test.iloc[:, 1:]).replace(to_replace=r'.*', value=0, regex=True)
    # print(df_test)
    df_temp['Participant'] = df_test['Participant No.']
    df_temp['+d+s'] = df_test.iloc[:, 1:5].sum(axis=1)

    df_temp['+d-s'] = df_test.iloc[:, 5:9].sum(axis=1)
    print(type(df_temp['+d+s']))
    # print(df_temp)

    df_temp['+d+s'] = df_temp['+d+s'].map(lambda x: 1 if x > 1 else 0)
    df_temp['+d-s'] = df_temp['+d-s'].map(lambda x: 1 if x > 1 else 0)
    # print(df_temp)

    # -D+S -D-S processing
    df_test = (df_excel_source.iloc[:, 9:17]).replace('a', 1)
    df_test.iloc[:, 0:] = (df_test.iloc[:, 0:]).replace(to_replace=r'.*', value=0, regex=True)
    # print(df_test)
    df_temp['-d+s'] = df_test.iloc[:, 0:4].sum(axis=1)

    df_temp['-d-s'] = df_test.iloc[:, 4:8].sum(axis=1)

    df_temp['-d+s'] = df_temp['-d+s'].map(lambda x: 1 if x > 1 else 0)
    df_temp['-d-s'] = df_temp['-d-s'].map(lambda x: 1 if x > 1 else 0)
    # print(df_temp)

    # Processing q17q20
    df_test = (df_excel_source.iloc[:, 17:21]).replace('the', 1)
    df_test.iloc[:, 0:] = (df_test.iloc[:, 0:]).replace(to_replace=r'.*', value=0, regex=True)
    # print(df_test)
    df_temp['q17q20'] = df_test.iloc[:, 0:4].sum(axis=1)
    df_temp['q17q20'] = df_temp['q17q20'].map(lambda x: 1 if x > 1 else 0)
    # print(df_temp)

    # Processing q21q24
    df_test = (df_excel_source.iloc[:, 21:25]).replace('a', 1)
    df_test.iloc[:, 0:] = (df_test.iloc[:, 0:]).replace(to_replace=r'.*', value=0, regex=True)
    # print(df_test)
    df_temp['q21q24'] = df_test.iloc[:, 0:4].sum(axis=1)
    df_temp['q21q24'] = df_temp['q21q24'].map(lambda x: 1 if x > 1 else 0)
    # print(df_temp)
    # print(df_excel_source)

    # Calculate result
    df_res = pnd.DataFrame(columns=['+d+s', '+d-s', '-d+s', '-d-s', 'q17q20', 'q21q24'])
    df_res['+d+s'] = pd.Series([df_temp['+d+s'].sum() / 133 * 100])
    df_res['+d-s'] = pd.Series([df_temp['+d-s'].sum() / 133 * 100])
    df_res['-d+s'] = pd.Series([df_temp['-d+s'].sum() / 133 * 100])
    df_res['-d-s'] = pd.Series([df_temp['-d-s'].sum() / 133 * 100])
    df_res['q17q20'] = pd.Series([df_temp['q17q20'].sum() / 133 * 100])
    df_res['q21q24'] = pd.Series([df_temp['q21q24'].sum() / 133 * 100])

    return df_res


print (percentage_correct_answer_by_category())
