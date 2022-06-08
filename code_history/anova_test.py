import numpy as np
import pandas as pd

# create data
df = pd.DataFrame({'water': np.repeat(['daily', 'weekly'], 15),
                   'sun': np.tile(np.repeat(['low', 'med', 'high'], 5), 2),
                   'height': [6, 6, 6, 5, 6, 5, 5, 6, 4, 5,
                              6, 6, 7, 8, 7, 3, 4, 4, 4, 5,
                              4, 4, 4, 4, 4, 5, 6, 6, 7, 8]})

# view first ten rows of data
print(df)

import statsmodels.api as sm
from statsmodels.formula.api import ols

# perform two-way ANOVA
w = 'water'
c = 'height ~ C('+w+') + C(sun) + C('+w+'):C(sun)'
print(c)
print(type((df['height']).iloc[0]))
model = ols('height ~ C('+w+') + C(sun) + C('+w+'):C(sun)', data=df).fit()

print(sm.stats.anova_lm(model, typ=2))
