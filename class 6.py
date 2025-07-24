import pandas as pd
import numpy as np

s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(np.random.randint(10000, high=30001, size=100,
dtype='l'))
print(s1, s2, s3)

housemkt = pd.concat([s1, s2, s3], axis=1)
housemkt.head()

housemkt.rename(columns = {0: 'bedrs', 1: 'bathrs', 2:
'price_sqr_meter'}, inplace=True)
housemkt.head()

bigcolumn = pd.concat([s1, s2, s3], axis=0)

bigcolumn = bigcolumn.to_frame()

print(type(bigcolumn))

len(bigcolumn)
print(300)

bigcolumn.reset_index(drop=True, inplace=True)
print(bigcolumn)
