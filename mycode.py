import pandas as pd
import os
data={'name': ['Alice', 'Bob', 'Charlie'],'age': [25, 30, 35],'city': ['New York', 'Los Angeles', 'Chicago']}
df=pd.DataFrame(data)
new_row={'name': 'David', 'age': 40, 'city': 'Houston'}
df=df._append(new_row, ignore_index=True)
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'data.csv')
df.to_csv(file_path,index=False)