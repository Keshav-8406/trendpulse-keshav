import pandas as pd
import os


# ---------------------- FILE PATH SETUP ----------------------
# Here I am defining the file path of the JSON file created in Task 1.
# Make sure the file name matches your actual file inside the data folder.

file_path = "data/trends_20260410.json"   # you can change date if needed


# ---------------------- LOAD JSON FILE ----------------------
# In this step, I am loading the JSON data into a Pandas DataFrame.
# This helps in handling data easily like filtering, cleaning, etc.

try:
    df = pd.read_json(file_path)
    print(f"Loaded {len(df)} stories from {file_path}")
except:
    print("Error loading JSON file")
    df = pd.DataFrame()


# ---------------------- REMOVE DUPLICATES ----------------------
# Here I am removing duplicate rows based on post_id.
# Sometimes same story might appear more than once, so this step ensures uniqueness.

before = len(df)
df = df.drop_duplicates(subset="post_id")
after = len(df)

print(f"After removing duplicates: {after}")


# ---------------------- REMOVE MISSING VALUES ----------------------
# In this step, I am removing rows where important fields are missing.
# Required fields are post_id, title, and score.

before = len(df)
df = df.dropna(subset=["post_id", "title", "score"])
after = len(df)

print(f"After removing nulls: {after}")


# ---------------------- FIX DATA TYPES ----------------------
# Here I am making sure that score and num_comments are integers.
# Sometimes they may be read as float or object, so I convert them.

df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# ---------------------- REMOVE LOW QUALITY DATA ----------------------
# In this step, I am removing stories where score is less than 5.
# This helps in filtering out low-quality or less popular stories.

before = len(df)
df = df[df["score"] >= 5]
after = len(df)

print(f"After removing low scores: {after}")


# ---------------------- CLEAN TITLE COLUMN ----------------------
# Here I am removing extra spaces from title column.
# Sometimes titles may have unnecessary spaces at start or end.

df["title"] = df["title"].str.strip()


# ---------------------- SAVE CLEAN DATA ----------------------
# Now I am saving the cleaned data into a CSV file.
# This file will be used in next tasks.

output_path = "data/trends_clean.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")


# ---------------------- SUMMARY ----------------------
# Finally, I am printing number of stories per category.
# This gives a quick overview of data distribution.

print("\nStories per category:")

category_counts = df["category"].value_counts()

for category, count in category_counts.items():
    print(f"  {category:<15} {count}")