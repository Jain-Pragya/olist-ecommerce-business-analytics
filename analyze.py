import pandas as pd

# Load the core CSVs
orders = pd.read_csv("olist_orders_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")

# 1. Merge items with orders on order_id
df = items.merge(orders, on="order_id", how="inner")

# 2. Merge with products on product_id
df = df.merge(products, on="product_id", how="left")

# 3. Merge with reviews on order_id (drop duplicate review entries per order if any)
reviews = reviews.drop_duplicates(subset=["order_id"])
df = df.merge(
    reviews[["order_id", "review_score"]], on="order_id", how="left"
)

# Export the master raw dataset (~110,000 rows)
df.to_csv("olist_master_data.csv", index=False)