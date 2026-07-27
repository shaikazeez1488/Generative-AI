import pandas as pd

n = int(input("Enter number of students: "))
names, marks = [], []

for i in range(n):
    names.append(input("Name: "))
    m = input("Marks (NA if missing): ")
    marks.append(None if m == "NA" else float(m))

df = pd.DataFrame({"Name": names, "Marks": marks})

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Score:", df["Marks"].max())