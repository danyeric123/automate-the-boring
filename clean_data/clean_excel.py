import pandas as pd

# add d_types if you want, e.g. dtype={'Name': str, 'Value': float}
main_df = pd.read_excel('main.xlsx', index_col=0)
second_df = pd.read_excel('second.xlsx', index_col=0)
third_df = pd.read_excel('third.xlsx', index_col=0)

main_df.drop_duplicates(subset=None, keep='first', inplace=True)

"""
Example of removing duplicates:

df.drop_duplicates(subset=['brand', 'style'], keep='last')
    brand style  rating
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
4  Indomie  pack     5.0
"""

main_df[~main_df.isin(second_df)].dropna()