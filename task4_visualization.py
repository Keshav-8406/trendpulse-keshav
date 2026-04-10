import pandas as pd
import matplotlib.pyplot as plt
import os


# ---------------------- LOAD DATA ----------------------
# In this step, I am loading the analysed CSV file created in Task 3.
# This file already contains cleaned data along with new columns like engagement and is_popular.

file_path = "data/trends_analysed.csv"

try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully")
except:
    print("Error loading CSV file")
    df = pd.DataFrame()


# ---------------------- CREATE OUTPUT FOLDER ----------------------
# Before saving charts, I am checking if "outputs" folder exists or not.
# If it does not exist, I am creating it so that all images can be stored properly.

if not os.path.exists("outputs"):
    os.mkdir("outputs")


# ---------------------- CHART 1: TOP 10 STORIES BY SCORE ----------------------
# Here I am selecting top 10 stories based on score.
# I am using horizontal bar chart for better readability of titles.

top10 = df.sort_values(by="score", ascending=False).head(10)

# Shortening long titles (more than 50 characters)
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(10, 6))
plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()   # highest score on top

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
# plt.show()


# ---------------------- CHART 2: STORIES PER CATEGORY ----------------------
# In this chart, I am counting how many stories are present in each category.
# Then I am plotting a bar chart.

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
# plt.show()


# ---------------------- CHART 3: SCATTER PLOT ----------------------
# In this chart, I am plotting score vs number of comments.
# I am using different colors for popular and non-popular stories.

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(8, 6))

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
# plt.show()


# ---------------------- DASHBOARD (BONUS) ----------------------
# Here I am combining all three charts into one single dashboard.
# This helps in visualizing everything at one place.

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1 in dashboard
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top 10 Stories")
axes[0].invert_yaxis()

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")

# Chart 3 in dashboard
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

fig.suptitle("TrendPulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")


# ---------------------- FINAL MESSAGE ----------------------
# Printing confirmation that all charts are saved.

print("All charts saved in outputs/ folder")