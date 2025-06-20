import matplotlib.pyplot as plt
from restaurant_recommender import recommend_restaurants

# You can change these inputs or get them dynamically
cuisine = "North Indian"
price_range = 2

recommendations = recommend_restaurants(cuisine, price_range)

plt.figure(figsize=(10, 6))
plt.barh(recommendations['Restaurant Name'], recommendations['Aggregate rating'], color='teal')
plt.xlabel('Rating')
plt.title(f'Top Restaurant Recommendations for "{cuisine}" in Price Range {price_range}')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
