# 🎬 Netflix Content Analytics Dashboard

A **Streamlit-based interactive dashboard** that analyzes Netflix Movies and TV Shows using **Python, Pandas, NumPy, Matplotlib, and Seaborn**. The project demonstrates the complete data analysis workflow—from data cleaning and preprocessing to visualization and insights.

## Deployed Link : https://netflix-content-analytic-dashboard.streamlit.app
---

## 📌 Project Overview

This dashboard provides an interactive way to explore Netflix's content library. It includes data cleaning, summary statistics, visualizations, and the ability to download the cleaned dataset.

The project was built as a beginner data analytics project to practice working with real-world datasets and creating interactive dashboards using Streamlit.

---

## ✨ Features

* 📊 Interactive Dashboard
* 🧹 Data Cleaning & Preprocessing
* 📈 Data Visualization
* 🎬 Top 10 Directors Analysis
* 🌍 Top 10 Countries Analysis
* 🍿 Movies vs TV Shows Distribution
* 📥 Download Cleaned Dataset

---

## 📂 Dataset

**Dataset:** Netflix Movies & TV Shows

**Source:** Kaggle

The dataset contains information about Netflix content, including:

* Title
* Type (Movie / TV Show)
* Director
* Cast
* Country
* Rating
* Release Year
* Duration
* Genre
* Date Added

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

* Removed duplicate records
* Removed rows with missing `duration`
* Removed rows with missing `date_added`
* Filled missing values in:

  * Director
  * Cast
  * Country
  * Rating
* Converted `date_added` to DateTime format
* Trimmed unnecessary whitespace from date values

---

## 📊 Dashboard Pages

### 🏠 Dashboard

Displays important KPIs including:

* Total Titles
* Movies
* TV Shows
* Countries
* Directors
* Genres
* Most Common Rating
* Years Covered

---

### 🧹 Data Cleaning

Shows:

* Cleaning process
* Missing values before cleaning
* Missing values after cleaning
* Raw dataset preview
* Cleaned dataset preview

---

### 📈 Visualisations

Includes:

* 🎬 Top 10 Directors
* 🌍 Top 10 Countries
* 🍿 Movies vs TV Shows

Each visualization also provides a short insight.

---

### 📥 Download Dataset

Allows users to download the cleaned dataset in CSV format.

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📷 Screenshots

Add screenshots of the following pages:

* Dashboard
* Data Cleaning
* Visualisations
* Download Dataset

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/rahulgupta7778/Netflix-content-analytics-dashboard.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── Dataset/
│   ├── netflix_titles.csv
│   └── cleaned_netflix_file.csv
│
└── Graphs/
    ├── Movie vs TV Shows.png
    ├── Top 10 Directors.png
    └── Top 10 Countries on Netflix.png
```

---

## 📚 Skills Demonstrated

* Data Cleaning
* Data Preprocessing
* Missing Value Handling
* Exploratory Data Analysis (EDA)
* Data Visualization
* Interactive Dashboard Development
* Streamlit Application Development

---
## 👨‍💻 Developed By

**Rahul Gupta**

