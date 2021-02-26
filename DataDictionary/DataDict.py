import pandas as pd

df = pd.read_csv('SP_results.csv')
data_dict = {'Data dictionary': ' [project name]','':''}

for i in df.columns:
    x = {i:' [description]'}
    data_dict.update(x)

pd.Series(data_dict).to_csv('data_dict_template.txt', header = False, sep = ':')
