import pandas as pd
import numpy as np

count = 0
data=pd.read_pickle('record/500.pkl')
x,y,z = data['alpha_feat'].shape

for i in range(x):
    for j in range(y):
        for k in range(z):
            if(data['alpha_feat'][i][j][k]<4 and data['alpha_feat'][i][j][k]==0):
                count = count + 1

print(x*y*z)
print(count/(x*y*z))
