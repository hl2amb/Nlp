import numpy as np
import pandas as pd
from IPython.display import display

meu_dado = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(np.array([[1,2,3],[4,5,6]]))
display(pd.DataFrame(meu_dado))
print(meu_dado.shape)           # 행(row)과 열(colum) 수
print(df.shape)
print(len(df.index))            # 행의 수
print(len(df.columns))          # 열의 수
print(list(df.columns))

my_dic = {'a': ['1', '3'], 'b': ['1', '2'], 'c': ['2', '4']}
display(pd.DataFrame(my_dic))


my_df = pd.DataFrame(data= [4,5,6,7], index=range(0,4), columns= ['A'])
display(pd.DataFrame(my_df))

my_series = pd.Series({"Uk": 'London', 'ROK':'Seoul', 'USA':'Washington DC', 'China':'Beijon', 'Japan':'Tokyo'})
display(pd.DataFrame(my_series))

dt = pd.DataFrame({'A': [1,4,7], 'B': [2,5,8], 'C': [3,6,9]})
display(pd.DataFrame(dt))
display(dt.columns[1])
display(dt.loc[2])              # 특정 행에 있는 열별 데이타 가져 오기
display(dt.loc[1]['B'])         # 특정 형에 특정 열에 있는 데이타 가져 오기