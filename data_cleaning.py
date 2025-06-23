import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\Apoorva P\Desktop\netflixdataset.csv")
#view basic info
print("Initial Data Info:")
print(df.info())
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# --- 2. Drop duplicates
df.drop_duplicates(inplace=True)

# --- 3. Standardize column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# --- 4. Handle missing values
# Forward fill for director, cast, country
for col in ['director', 'cast', 'country']:
    if col in df.columns:
        df[col] = df[col].fillna(method='ffill')

# Fill missing values in 'rating' with mode
if 'rating' in df.columns:
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# --- 5. Convert 'date_added' to datetime
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# --- 6. Convert release_year to int (if needed)
if 'release_year' in df.columns:
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')

# --- 7. Clean 'duration' column (optional: split into duration_int and duration_type)
if 'duration' in df.columns:
    df['duration'] = df['duration'].fillna('0 min')
    df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
    df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce').astype('Int64')

# --- 8. Final check
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nCleaned Data Info:")
print(df.info())

# --- 9. Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_dataset.csv'")
