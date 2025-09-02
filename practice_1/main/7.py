from sklearn.datasets import fetch_california_housing
import pandas as pd
data = fetch_california_housing(as_frame=True)

df: pd.DataFrame = data["frame"]

print("\nTask 8\n")
df.info()

print("\nTask 9\n")
print(df.isna().sum())

print("\nTask 10\n")
filtered_df = df.loc[(df['AveRooms'] > 50) & (df['Population'] > 2500)]
print(filtered_df)

print("\nTask 11\n")
max_medinc = df['MedInc'].max()
min_medinc = df['MedInc'].min()
print(f"Max med price: {max_medinc}")
print(f"Min med price: {min_medinc}")

print("\nTask 12\n")
mean_values = df.apply(lambda x: x.mean())
for column, mean_value in mean_values.items():
    print(f"{column}: {mean_value}")
