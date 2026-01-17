import pandas as pd

# ------------------------------
# Creating Series
# ------------------------------
s = pd.Series([10, 20, 30, 40, 50])
print("Series:\n", s)

# Series operations
print("Sum:", s.sum())
print("Mean:", s.mean())
print("Max:", s.max())
print("Min:", s.min())
print("Describe:\n", s.describe())

# ------------------------------
# Creating DataFrame
# ------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ------------------------------
# DataFrame basic info
# ------------------------------
print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nIndex:", df.index)
print("\nInfo:")
df.info()

# ------------------------------
# Selection & Indexing
# ------------------------------
print("\nSingle Column:\n", df["Marks"])
print("\nMultiple Columns:\n", df[["Name", "Marks"]])
print("\nRow using loc:\n", df.loc[1])
print("\nRow using iloc:\n", df.iloc[2])

# Adding & Removing Columns

df["Passed"] = df["Marks"] >= 80
print("\nAfter Adding Column:\n", df)

df.drop("Passed", axis=1, inplace=True)
print("\nAfter Dropping Column:\n", df)

# Handling Missing Values

df.loc[2, "Marks"] = None
print("\nWith Missing Value:\n", df)

print("\nIs Null:\n", df.isnull())
print("\nFill Null:\n", df.fillna(df["Marks"].mean()))
print("\nDrop Null:\n", df.dropna())

# Sorting

print("\nSorted by Marks:\n", df.sort_values("Marks"))

# ------------------------------
# Statistical Functions
# ------------------------------
print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nStd Dev:\n", df.std(numeric_only=True))

# ------------------------------
# GroupBy
# ------------------------------
group = df.groupby("Age")["Marks"].mean()
print("\nGroupBy Age (Mean Marks):\n", group)

# Apply & Map

df["Marks"] = df["Marks"].fillna(0)
df["Marks"] = df["Marks"].apply(lambda x: x + 2)
print("\nAfter Apply:\n", df)

# ------------------------------
# Reading & Writing Files
# ------------------------------
df.to_csv("students.csv", index=False)
new_df = pd.read_csv("students.csv")
print("\nRead from CSV:\n", new_df)

# DataFrame Utilities
print("\nDuplicated:\n", df.duplicated())
print("\nDrop Duplicates:\n", df.drop_duplicates())

# ------------------------------
# Value Counts
# ------------------------------
print("\nValue Counts (Age):\n", df["Age"].value_counts())
