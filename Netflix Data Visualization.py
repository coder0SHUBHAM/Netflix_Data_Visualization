
# Project: Netflix Data Visualization (Matplotlib)
# Author: Shubham Sonar

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_titles.csv")

df = df.dropna(subset=['show_id','type','title','director','cast','country',
                       'date_added','release_year','rating','duration','listed_in','description'])


type_count = df['type'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values, color=['orange','green'])
plt.title("Distribution of Movies and TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

for i, v in enumerate(type_count.values):
    plt.text(i, v+20, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()


rating_count = df['rating'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(rating_count, labels=rating_count.index, autopct='%1.1f%%',
        startangle=90, explode=[0.05]*len(rating_count))
plt.title("Distribution of Ratings")
plt.tight_layout()
plt.show()


movies = df[df['type'] == 'Movie'].copy()
movies = movies[movies['duration'].str.contains("min", na=False)]
movies['duration_min'] = movies['duration'].str.replace(" min", "", regex=False).astype(int)

plt.figure(figsize=(10,6))
plt.hist(movies['duration_min'], bins=20, color="skyblue", edgecolor="black", alpha=0.8)
plt.axvline(movies['duration_min'].mean(), color='red', linestyle='--', linewidth=2,
            label=f"Mean: {movies['duration_min'].mean():.0f} min")

plt.title("Distribution of Movie Durations on Netflix")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()


release_count = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12,6))
plt.scatter(release_count.index, release_count.values, color="red", s=40, label="Titles")
plt.plot(release_count.index, release_count.values, color="blue", linewidth=2, alpha=0.7)

plt.title("Release Year vs Number of Titles")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()


country_count = df['country'].value_counts().head(10)

plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title("Top 10 Countries with the Most Titles on Netflix")
plt.xlabel("Number of Titles")

for i, v in enumerate(country_count.values):
    plt.text(v+5, i, str(v), va='center', fontweight='bold')

plt.tight_layout()
plt.show()

yearly_counts = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)

plt.figure(figsize=(12,6))
plt.plot(yearly_counts.index, yearly_counts['Movie'], marker='o', color="blue", label="Movies")
plt.plot(yearly_counts.index, yearly_counts['TV Show'], marker='s', color="red", label="TV Shows")

plt.title("Movies vs TV Shows Released Each Year on Netflix")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()
