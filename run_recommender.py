from restaurant_recommender import recommend_restaurants

print("🍽️ Welcome to the Restaurant Recommender System!")

# Get user preferences
cuisine = input("Enter your preferred cuisine (e.g., North Indian, Italian, Chinese): ")
price_range = input("Enter your desired price range (1=low, 2=medium, 3=high, 4=very high): ")

# Show recommendations
results = recommend_restaurants(cuisine, price_range)

print("\nTop Restaurant Recommendations for You:\n")
for idx, row in results.iterrows():
    print(f"🏨 {row['Restaurant Name']} | 🍽️ {row['Cuisines']} | 💰 Price Range: {row['Price range']} | 📍 {row['City']} | ⭐ Rating: {row['Aggregate rating']}")
print("\nThank you for using the Restaurant Recommender System! Enjoy your meal! 🍽️")