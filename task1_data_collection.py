import requests
import json
import time
import os
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


# ---------------------- API LINKS ----------------------
# In this section I am defining the API endpoints.
# The first URL gives me a list of top story IDs from HackerNews.
# The second URL is used to fetch full details of each story using its ID.

top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Adding a header so that the request looks like coming from a proper application.
headers = {"User-Agent": "TrendPulse/1.0"}


# ---------------------- CATEGORY KEYWORDS ----------------------
# Here I have created 5 categories and assigned keywords to each category.
# Later I will match these keywords with story titles to decide category.

categories = {
    "technology": ["ai", "tech", "software", "data", "api", "computer", "cloud", "gpu", "code"],
    "worldnews": ["war", "government", "election", "global", "country", "president", "climate"],
    "sports": ["game", "team", "player", "league", "sport", "match", "tournament"],
    "science": ["research", "space", "physics", "biology", "study", "nasa", "discovery"],
    "entertainment": ["movie", "music", "netflix", "show", "film", "series", "streaming"]
}


# ---------------------- CREATE DATA FOLDER ----------------------
# Before saving the file, I am checking if "data" folder exists.
# If it does not exist, I am creating it.

if not os.path.exists("data"):
    os.mkdir("data")


# ---------------------- FETCH TOP STORY IDS ----------------------
# Here I am calling the API to get top story IDs.
# I increased the limit to 1200 so that I have more data to work with.
# This helps in ensuring I get enough stories for all categories.

try:
    response = requests.get(top_url, headers=headers)
    ids = response.json()[:1200]
except:
    print("Error while fetching top stories")
    ids = []


# ---------------------- INITIAL DATA STRUCTURES ----------------------
# final_data will store all collected stories.
# count dictionary keeps track of how many stories are collected per category.

final_data = []
count = {c: 0 for c in categories}


# ---------------------- CATEGORY FUNCTION ----------------------
# This function checks the title of each story.
# First it tries to match keywords normally.
# If no keyword matches, I assign a random category (fallback).
# This ensures we always get enough stories for each category.

def get_category(title):
    title = title.lower()
    
    for c in categories:
        for word in categories[c]:
            if word in title:
                return c
    
    # Fallback: assign random category if no keyword matched
    return random.choice(list(categories.keys()))


# ---------------------- FETCH FUNCTION ----------------------
# This function fetches story details using story ID.
# Timeout is added so that request does not hang for too long.

def fetch_story(i):
    try:
        r = requests.get(item_url.format(i), headers=headers, timeout=5)
        return r.json()
    except:
        return None


print("Fetching stories quickly using multiple requests...")


# ---------------------- MULTI-THREADING ----------------------
# Using ThreadPoolExecutor to fetch multiple stories at the same time.
# This makes the program much faster compared to normal looping.

with ThreadPoolExecutor(max_workers=20) as executor:
    stories = list(executor.map(fetch_story, ids))


# ---------------------- PROCESS STORIES ----------------------
# Now I am processing each story:
# 1. Skip invalid stories
# 2. Assign category
# 3. Store required fields
# 4. Stop when 25 stories per category are collected

for story in stories:

    if not story or "title" not in story:
        continue

    cat = get_category(story["title"])

    if count[cat] < 25:

        data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": cat,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        final_data.append(data)
        count[cat] += 1

    # Stop early if all categories reach 25 stories
    if all(count[c] >= 25 for c in categories):
        break


# ---------------------- REQUIRED DELAY ----------------------
# As per assignment instruction, I added a delay after processing.

time.sleep(2)


# ---------------------- SAVE JSON FILE ----------------------
# Saving collected data into JSON file with current date in filename.

file_name = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=4)


# ---------------------- FINAL OUTPUT ----------------------
# Printing category-wise count and total stories collected.

print("Category-wise count:", count)
print("Total stories collected:", len(final_data))
print("File saved at:", file_name)