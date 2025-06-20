import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("Dataset.csv")

# Preprocessing
df.dropna(subset=['Cuisines', 'Price range'], inplace=True)
df.drop_duplicates(inplace=True)

# Fill missing values if any
df['Cuisines'] = df['Cuisines'].fillna('')
df['Price range'] = df['Price range'].astype(str)

# Combine features
df['combined_features'] = df['Cuisines'] + " " + df['Price range']

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

# Similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index for easier lookup
df = df.reset_index()

# Recommendation function
def recommend_restaurants(user_cuisine, user_price_range, top_n=5):
    user_input = user_cuisine + " " + str(user_price_range)
    user_vec = vectorizer.transform([user_input])
    sim_scores = cosine_similarity(user_vec, tfidf_matrix).flatten()
    
    top_indices = sim_scores.argsort()[-top_n:][::-1]
    recommendations = df.iloc[top_indices][['Restaurant Name', 'Cuisines', 'Price range', 'City', 'Aggregate rating']]
    
    return recommendations
