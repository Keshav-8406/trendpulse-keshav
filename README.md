
---

# 📥 Task 1 — Data Collection (API Fetching)

📌 File: `task1_data_collection.py`

### What I did:
- Connected to HackerNews API 🔗  
- Fetched top 500 story IDs  
- Collected story details (title, score, comments, author)  
- Categorized stories into:
  - 💻 Technology  
  - 🌍 World News  
  - ⚽ Sports  
  - 🔬 Science  
  - 🎬 Entertainment  

### Output:
- JSON file saved in `data/trends_YYYYMMDD.json`
- Minimum 100+ stories collected

---

# 🧹 Task 2 — Data Cleaning

📌 File: `task2_data_processing.py`

### What I did:
- Loaded JSON data into Pandas 📊  
- Removed duplicate stories  
- Handled missing values  
- Converted data types properly  
- Removed low-quality stories (score < 5)  
- Cleaned text fields (titles)  

### Output:
- Clean CSV saved as `data/trends_clean.csv`
- Structured and ready data for analysis

---

# 📊 Task 3 — Data Analysis

📌 File: `task3_analysis.py`

### What I did:
- Loaded cleaned CSV file  
- Performed statistical analysis using NumPy 🔢  
- Calculated:
  - Mean score  
  - Median score  
  - Standard deviation  
  - Max & Min values  
- Found:
  - Most active category 🏆  
  - Most commented story 💬  
- Created new columns:
  - `engagement = comments / (score + 1)`  
  - `is_popular = score > average score`  

### Output:
- Final dataset saved as `data/trends_analysed.csv`

---

# 📈 Task 4 — Data Visualization

📌 File: `task4_visualization.py`

### What I did:
- Created visual insights using Matplotlib 📊  
- Built 3 main charts:

### 📌 Chart 1:
📉 Top 10 stories by score (bar chart)

### 📌 Chart 2:
📊 Number of stories per category

### 📌 Chart 3:
🔵 Scatter plot (Score vs Comments)
- Popular vs non-popular stories shown with different colors

### 📌 Bonus Dashboard:
📊 Combined all charts into one view

### Output:
Saved images in `outputs/` folder:
- chart1_top_stories.png  
- chart2_categories.png  
- chart3_scatter.png  
- dashboard.png  

---

# 📂 Final Project Structure

```

trendpulse-keshav/
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── data/
│   ├── trends_20260410.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
└── outputs/
├── chart1_top_stories.png
├── chart2_categories.png
├── chart3_scatter.png
└── dashboard.png

```

-----

# 👨‍💻 Author

👤 Keshav Kaushik  
🎓 B.Sc Computer Science Student (IInd Year)  
📍 Government Holkar Science College, Indore  

---

# ⭐ Thank You

If you liked this project, feel free to ⭐ the repository!
