import pandas as pd

df = pd.read_csv("orders_dirty.csv")

df["product"] = df["product"].str.strip().str.title()
df["category"] = df["category"].str.strip().str.title()
df["payment_method"] = df["payment_method"].str.strip().str.title()
df["status"] = df["status"].str.strip().str.title()

df["unit_price"] = df["unit_price"].str.strip()

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df.loc[df["quantity"] < 0, "quantity"] = pd.NA

df["unit_price"] = df["unit_price"].str.replace(",", ".")
df["unit_price"] = pd.to_numeric(df["unit_price"])
df.loc[df["unit_price"] < 0, "unit_price"] = pd.NA

mask = df["discount"].astype(str).str.endswith("%")

df["discount"] = df["discount"].astype(str).str.rstrip("%")
df["discount"] = pd.to_numeric(df["discount"], errors="coerce")

df.loc[mask, "discount"] = df.loc[mask, "discount"] / 100
df.loc[df["discount"] > 1, "discount"] = pd.NA

df["order_date"] = df["order_date"].str.strip()
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

df["total"] = df["unit_price"] * df["quantity"] * (1 - df["discount"])
df.to_csv("orders_clean.csv", index=False)
print(df.head(30))
