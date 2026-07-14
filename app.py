import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Netflix Content Analytics Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

file_url = r"Dataset/netflix_titles.csv"
df = pd.read_csv(file_url , encoding="latin1")

def clean_data(df):

    df = df.copy()

    df.drop_duplicates(inplace=True)
    df.dropna(subset=["duration" , "date_added"] , inplace=True)
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Unknown")
    df["date_added"] = df["date_added"].str.strip()
    df["date_added"] = pd.to_datetime(df["date_added"])
    df["director"] = df["director"].fillna("Unknown")

    return df

df = clean_data(df)


total_titles = len(df)
total_movies = len(df[df["type"] == "Movie"])
total_tv = len(df[df["type"] == "TV Show"])
countries = (
    df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)
total_countries = countries.nunique()
oldest_year = df["release_year"].min()
latest_year = df["release_year"].max()
most_common_rating = df["rating"].mode()[0]
genres = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)
total_genres = genres.nunique()
total_directors = (
    df[df["director"] != "Unknown"]["director"]
    .str.split(",")
    .explode()
    .str.strip()
    .nunique()
)
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/75/Netflix_icon.svg",
    width=80
)

st.sidebar.title("Netflix Dashboard")
selected_page = st.sidebar.selectbox("" , ['Dashboard' , 'Data Cleaning'  , 'Visualisation' , 'Download Dataset'])

if selected_page == 'Dashboard':
    with st.container():
        st.title("Netflix Content Analytics Dashboard")
        st.divider()
        st.subheader('''Explore Netflix's catalog through interactive visualizations, data cleaning insights, and statistical analysis.''')
        st.write('''This dashboard analyzes Netflix's Movies and TV Shows dataset using Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit. It provides interactive visualizations, content statistics, and insights into Netflix's global library.''')
    st.divider()
    with st.container():
        col1 , col2 , col3 , col4 = st.columns(4)
        with col1:
            st.metric("Total Titles", total_titles)

        with col2:
            st.metric("Movies", total_movies)

        with col3:
            st.metric("TV Shows", total_tv)

        with col4:
            st.metric("Countries", total_countries)
        

        col5 , col6 , col7 , col8 = st.columns(4)
        with col5:
            st.metric("Directors", total_directors)

        with col6:
            st.metric("Genres", total_genres)

        with col7:
            st.metric("Most common Rating",  most_common_rating)

        with col8:
            st.metric("Years Covered", f"{oldest_year} - {latest_year}")
    st.divider()

    with st.container():
        st.subheader("Tech Stack")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("🐍 Python")
            st.info("🐼 Pandas")

        with col2:
            st.info("🔢 NumPy")
            st.info("📊 Matplotlib")

        with col3:
            st.info("🎨 Seaborn")
            st.info("🌐 Streamlit")

    st.divider()

    with st.container():
        st.subheader("Dataset Information")
        st.info("""
        **Dataset Source**

        Netflix Movies & TV Shows Dataset

        Source: Kaggle
        """)

    st.divider()
    with st.container():
        st.subheader("Features")

        st.markdown("""
        - 📊 Interactive Dashboard
        - 🧹 Data Cleaning
        - 📈 Data Visualization
        - 🌍 Country-wise Analysis
        - 🎬 Director Analysis
        """)


    st.divider()

    with st.container():
        st.caption(
            "Developed by Rahul Gupta | Python • Pandas • NumPy • Matplotlib • Seaborn • Streamlit"
        )
    st.divider()

elif selected_page == 'Data Cleaning':
    st.title(" Data Cleaning")

    st.write("""
    The original Netflix dataset was cleaned before analysis.

    The following preprocessing steps were performed:
    - Removed duplicate rows
    - Removed rows with missing duration
    - Removed rows with missing date_added
    - Filled missing values in:
        - Director
        - Cast
        - Country
        - Rating
    - Converted date_added to datetime format
    """)
    st.divider()
    raw_df = pd.read_csv(file_url)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows Before Cleaning", raw_df.shape[0])

    with col2:
        st.metric("Rows After Cleaning", df.shape[0])

   
    col1,col2 = st.columns(2)
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Before Cleaning")
        st.dataframe(raw_df.isnull().sum())

    with col2:
        st.subheader("After Cleaning")
        st.dataframe(df.isnull().sum())

    tab1, tab2 = st.tabs(["Raw Dataset", "Cleaned Dataset"])

    with tab1:
        st.dataframe(raw_df)

    with tab2:
        st.dataframe(df)
        st.success("Dataset cleaned successfully ✅")
    
elif selected_page == "Download Dataset":

    st.title("Download Dataset")

    st.write("Download the cleaned Netflix dataset used for analysis.")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_netflix_titles.csv",
        mime="text/csv"
    )

elif selected_page == 'Visualisation':
    st.title("Netflix Visualisations")
    st.write("Explore Netflix's content through interactive charts and insights.")
    st.divider()
    tab1 , tab2 , tab3 = st.tabs(["Top 10 Director", "Movies vs TV Shows" , "Top 10 Countries"])
    with tab1 : 
        with st.container():
            st.subheader("Top 10 Directors")
        top_directors = (
        df[df["director"] != "Unknown"]["director"]   # Remove Unknown
        .str.split(",")                               # Split multiple directors
        .explode()                                    # Create separate rows
        .str.strip()                                  # Remove extra spaces
        .value_counts()                               # Count titles
        .head(10)                                     # Top 10
    )
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.barh(top_directors.index, top_directors.values)

        ax.set_title("Top 10 Directors on Netflix")
        ax.set_xlabel("Number of Titles")
        ax.set_ylabel("Director")

        st.pyplot(fig)
        st.info(
        f"**{top_directors.index[0]}** is the most featured director "
        f"with **{top_directors.iloc[0]} titles**."
        )
    st.divider()

    with tab2:
        st.subheader("Movies vs TV Shows")
        shows_count = df['type'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 6))

        ax.pie(shows_count, labels=shows_count.index , startangle=90 , explode = (0.05 , 0) , autopct='%1.1f%%')
        ax.set_title("Movie Vs TV shows")
        st.pyplot(fig)
        st.info(
        f"Movies dominate the Netflix catalog with **{shows_count['Movie']} titles**, "
        f"while TV Shows account for **{shows_count['TV Show']} titles**."
        )
        top_countries = (
        df["country"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
        )
    st.divider()

    with tab3 : 
        st.subheader("Top 10 Countries")
        fig, ax = plt.subplots(figsize=(10,6))

        ax.barh(top_countries.index, top_countries.values)

        ax.set_title("Top 10 Countries on Netflix")
        ax.set_xlabel("Number of Titles")
        ax.set_ylabel("Country")

        st.pyplot(fig)
        st.info(
        f"**{top_countries.index[0]}** has the largest number of Netflix titles "
        f"({top_countries.iloc[0]} titles)."
        )