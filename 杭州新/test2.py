import pandas as pd

df = pd.read_excel("last_result.xlsx", sheet_name="Sheet1")

df["年份"] = pd.to_datetime(df["申请日"]).dt.year

for year, group in df.groupby("年份"):
    group.to_excel(f"{year}.xlsx", index=False)
