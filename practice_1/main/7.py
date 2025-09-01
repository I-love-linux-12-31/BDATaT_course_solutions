from sklearn.datasets import fetch_california_housing
import pandas as pd
data = fetch_california_housing(as_frame=True)

df: pd.DataFrame = data["frame"]

print("\nTask 8\n")
df.info()

print("\nTask 9\n")
print(df.isna().sum())

# todo
