import pandas as pd

products = pd.read_csv("data/raw/products.csv")
sales = pd.read_csv("data/raw/sales.csv")
inventory = pd.read_csv("data/raw/inventory.csv")

products.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)
inventory.drop_duplicates(inplace=True)

products["price"].fillna(0, inplace=True)
products["discount"].fillna(0, inplace=True)

products["discount_percent"] = (products["discount"] / products["price"]) * 100
inventory["in_stock"] = inventory["stock_qty"].apply(
    lambda x: "Yes" if x > 0 else "No"
)

fact_sales = sales.merge(products, on="product_id", how="left")

dim_products = products[
    ["product_id", "product_name", "category", "brand", "price", "discount_percent"]
]

dim_inventory = inventory

fact_sales.to_csv("fact_sales.csv", index=False)
dim_products.to_csv("dim_products.csv", index=False)
dim_inventory.to_csv("dim_inventory.csv", index=False)

print("Done")
