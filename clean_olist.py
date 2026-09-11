import numpy as np
import pandas as pd

df = pd.read_csv("olist_master_data.csv")

# 1. Filter out canceled or unavailable orders to focus on completed fulfillment
df_clean = df[df["order_status"] == "delivered"].copy()

# 2. Convert timestamps to datetime format
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
for col in date_cols:
  df_clean[col] = pd.to_datetime(df_clean[col], errors="coerce")

# 3. Drop records with missing delivery dates or review scores
df_clean = df_clean.dropna(
    subset=["order_delivered_customer_date", "review_score"]
)

# 4. Fill missing product categories with 'unknown'
df_clean["product_category_name"] = df_clean["product_category_name"].fillna(
    "unknown"
)

# 5. Feature Engineering: Delivery duration and delays
df_clean["delivery_days"] = (
    df_clean["order_delivered_customer_date"]
    - df_clean["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 3600)
df_clean["estimated_days"] = (
    df_clean["order_estimated_delivery_date"]
    - df_clean["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 3600)
df_clean["delay_days"] = (
    df_clean["order_delivered_customer_date"]
    - df_clean["order_estimated_delivery_date"]
).dt.total_seconds() / (24 * 3600)
df_clean["is_delayed"] = (df_clean["delay_days"] > 0).astype(int)
df_clean["freight_ratio"] = df_clean["freight_value"] / (
    df_clean["price"] + 0.01
)

# 6. Remove invalid/negative delivery days (outliers/data anomalies)
df_clean = df_clean[
    (df_clean["delivery_days"] >= 0) & (df_clean["delivery_days"] <= 120)
]

# Save to upload as 'Processed Data'
df_clean.to_csv("olist_processed_data.csv", index=False)