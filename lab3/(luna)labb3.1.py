
#3. Transformation (DOB to AGE)
#3.1
import pandas as pd

data=pd.read_csv('D:/python_prog/data_with_age.csv')
print("Original Data")
print(data[0:5])

data["DOB"] = pd.to_datetime(data["DOB"])
today = pd.to_datetime("today")
data["AGE"] = (today - data["DOB"]).dt.days / 365.25
data["AGE"] = data["AGE"].astype(int)

print("Transformed Data")

print(data.to_string(index=False))