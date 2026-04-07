import pandas as pd

data1 = {
    "Name": ["goapl", "swarup", "DEV"],
    "Roll No.": [1, 2, 3],
    "Attendance": ["25", "54", "78"]
}

data2 = {
    "Name": ["goapl", "swarup", "nitesh"],
    "Roll No.": [1,2,4],
    "Marks": ["25", "54", "78"]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)



df_merge = pd.merge(df1, df2, on=["Roll No.","Name"],how="outer")
print(df_merge)
