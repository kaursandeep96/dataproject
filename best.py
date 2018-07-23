import pandas as pd
import numpy as np 
import nltk
from functools import partial 
aisles_data = pd.read_csv('instacart/aisles.csv')
print('Total no. of aisles: {}'.format(aisles_data.shape[0]))
aisles_data
departments_data = pd.read_csv('instacart/departments.csv')
%%time
top = 15
top_products = pd.merge(
    left=pd.DataFrame(order_details.groupby(['product_id'])['order_id']\
    .apply(lambda x: len(x.unique())).sort_values(ascending=False)[:top].reset_index('product_id')),
    right=goods,
    how='left')
top_products