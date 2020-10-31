import pandas as pd
from .models import Pet

data = pd.read_excel('./DataSet.xlsx', header=1)
print(data.head())
for pet_row in data.itertuples():
    Pet(name=pet_row[0])
