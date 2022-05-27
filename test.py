import pandas as pd

# making a dict of list
info = {'Name': ['Parker', 'Smith', 'William'],
        'age': [32, 28, 39]}
data = pd.DataFrame(info)
# sum of all salary stored in 'total'
data['total'] = data['age'].sum()
print(data['age'].sum())
