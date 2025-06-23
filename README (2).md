Netflix Dataset Cleaning - Internship Task 1

This project contains the cleaned Netflix Movies and TV Shows dataset for the Data Analyst Internship Task 1.

Task Objective:
Clean and preprocess a raw dataset by:
- Removing missing and duplicate values
- Standardizing column names
- Formatting inconsistent data (like dates and durations)
- Preparing the data for analysis

Dataset Used:
Original file: netflixdataset.csv  
Cleaned file: cleaned_dataset.csv

Tools Used:
Python  
Pandas

Cleaning Steps Performed:
1. Dropped duplicate records
2. Standardized column names to lowercase and underscore format
3. Forward-filled missing values in 'director', 'cast', and 'country'
4. Filled missing 'rating' values using the mode
5. Converted 'date_added' to datetime format
6. Converted 'release_year' to integer type
7. Cleaned the 'duration' column and split it into 'duration_int' and 'duration_type'

Files in This Repository:
netflix_cleaning.py - Python cleaning script  
cleaned_dataset.csv - Final cleaned dataset  
README.md - Task description and summary

Output:
The cleaned dataset is saved as cleaned_dataset.csv

Submission Link:
https://forms.gle/o2uMAByM719GzebC7

Author:
Apoorva P
BCA Data Science Student
