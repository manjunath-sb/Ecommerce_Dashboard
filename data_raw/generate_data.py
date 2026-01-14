import pandas as pd
import numpy as np
from datetime import timedelta
import random

np.random.seed(42)

# ---------------- PRODUCTS ----------------
categories = {
    "Electronics": ["Mobile", "Laptop", "Accessories"],
    "Fashion": ["Clothing", "Footwear"],
    "Home": ["Kitchen", "Furniture"]
}

products = []
for i in range(1, 51):
    cat = random.choice(list(categories.keys()))
    sub = random.choice(categories[cat])
    products.append([f"PROD_{i:03}", cat, sub])

products_df = pd.DataFrame(products, columns=["product_id", "category", "sub_category"])

# ---------------- CUSTOMERS ----------------
customers = []
start_signup = pd.to_datetime("2023-01-01")

for i in range(1, 501):
    signup = start_signup + timedelta(days=random.randint(0, 120))
    region = random.choice(["North", "South", "East", "West"])
    customers.append([f"CUST_{i:04}", signup, "Unknown", region])

customers_df = pd.DataFrame(customers, columns=["customer_id", "signup_date", "customer_type", "region"])

# ---------------- ORDERS ----------------
orders = []
start_order = pd.to_datetime("2023-02-01")

for i in range(1, 1001):
    cust = customers_df.sample(1).iloc[0]
    order_date = start_order + timedelta(days=random.randint(0, 180))
    status = random.choices(
        ["Delivered", "Shipped", "Cancelled"],
        weights=[0.7, 0.2, 0.1]
    )[0]

    delivery_date = (
        order_date + timedelta(days=random.randint(2, 7))
        if status == "Delivered" else pd.NaT
    )

    orders.append([
        f"ORD_{i:05}",
        order_date,
        cust["customer_id"],
        status,
        delivery_date,
        cust["region"]
    ])

orders_df = pd.DataFrame(
    orders,
    columns=["order_id", "order_date", "customer_id", "order_status", "delivery_date", "region"]
)

# ---------------- ORDER ITEMS ----------------
items = []

for order_id in orders_df["order_id"]:
    for _ in range(random.randint(1, 3)):
        prod = products_df.sample(1).iloc[0]
        qty = random.randint(1, 4)
        price = random.randint(200, 5000)
        items.append([order_id, prod["product_id"], qty, price])

items_df = pd.DataFrame(
    items,
    columns=["order_id", "product_id", "quantity", "unit_price"]
)

# ---------------- SAVE FILES ----------------
products_df.to_csv("data_raw/products.csv", index=False)
customers_df.to_csv("data_raw/customers.csv", index=False)
orders_df.to_csv("data_raw/orders.csv", index=False)
items_df.to_csv("data_raw/order_items.csv", index=False)

print("CSV files generated successfully")
