import pandas as pd
import numpy as np


# ---------------------- LOAD DATA ----------------------
# In this step, I am loading the cleaned CSV file created in Task 2.
# This file already has cleaned and structured data, so analysis becomes easier.

file_path = "data/trends_clean.csv"

try:
    df = pd.read_csv(file_path)
    print(f"Loaded data: {df.shape}")
except:
    print("Error loading CSV file")
    df = pd.DataFrame()


# ---------------------- BASIC EXPLORATION ----------------------
# Here I am printing first 5 rows of the dataset to understand how data looks.

print("\nFirst 5 rows:")
print(df.head())


# Here I'm printing average score and average number of comments
# This gives an overall idea about engagement level of stories.

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")


# ---------------------- NUMPY ANALYSIS ----------------------
# In this section, I am using NumPy to perform statistical calculations.
# NumPy is faster and commonly used for numerical operations.

scores = df["score"].values
comments = df["num_comments"].values

print("\n--- NumPy Stats ---")

# Mean score
mean_score = np.mean(scores)
print(f"Mean score   : {mean_score:.2f}")

# Median score
median_score = np.median(scores)
print(f"Median score : {median_score:.2f}")

# Standard deviation
std_score = np.std(scores)
print(f"Std deviation: {std_score:.2f}")

# Max and Min score
print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")


# ---------------------- CATEGORY ANALYSIS ----------------------
# Finding which category has most number of stories.

category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")


# ---------------------- MOST COMMENTED STORY ----------------------
# Finding the story which has maximum number of comments.

max_comments_index = df["num_comments"].idxmax()
top_story_title = df.loc[max_comments_index, "title"]
top_story_comments = df.loc[max_comments_index, "num_comments"]

print(f'\nMost commented story: "{top_story_title}" — {top_story_comments} comments')


# ---------------------- ADD NEW COLUMNS ----------------------
# Now I am adding two new columns as required in assignment.

# 1. Engagement column
# Formula: num_comments / (score + 1)
# +1 is added to avoid division by zero

df["engagement"] = df["num_comments"] / (df["score"] + 1)


# 2. is_popular column
# If score is greater than average score → True, else False

df["is_popular"] = df["score"] > avg_score


# ---------------------- SAVE UPDATED DATA ----------------------
# Saving the updated DataFrame into a new CSV file.

output_path = "data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")