
import pandas as pd

# Load the Excel dataset
df = pd.read_excel("data/Online_Retail.xlsx")

# Display first five rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# Display dataset dimensions
print("\n--- DATASET SHAPE ---")
print(df.shape)

# Display column information
print("\n--- DATASET INFO ---")
print(df.info())

# Display statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

# ---------------------------------
# DETAILED DATA INVESTIGATION
# ---------------------------------

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE RECORDS ---")
print("Total duplicates:", df.duplicated().sum())

print("\n--- NEGATIVE QUANTITY ---")
print("Negative quantity records:",
      (df["Quantity"] < 0).sum())

print("\n--- ZERO QUANTITY ---")
print("Zero quantity records:",
      (df["Quantity"] == 0).sum())

print("\n--- NEGATIVE UNIT PRICE ---")
print("Negative UnitPrice records:",
      (df["UnitPrice"] < 0).sum())

print("\n--- ZERO UNIT PRICE ---")
print("Zero UnitPrice records:",
      (df["UnitPrice"] == 0).sum())

print("\n--- CANCELLED INVOICES ---")
cancelled = df["InvoiceNo"].astype(str).str.startswith("C")

print("Cancelled invoice records:", cancelled.sum())

print("\n--- DATE RANGE ---")
print("First date:", df["InvoiceDate"].min())
print("Last date:", df["InvoiceDate"].max())

print("\n--- COUNTRY DISTRIBUTION ---")
print(df["Country"].value_counts().head(10))

# =====================================
# INVESTIGATE DATA QUALITY ISSUES
# =====================================

# 1. Inspect duplicate records

print("\n--- DUPLICATE RECORD EXAMPLES ---")

duplicate_rows = df[df.duplicated(keep=False)]

print("Total rows involved in duplicate groups:",
      len(duplicate_rows))

print(duplicate_rows.head(10))


# 2. Inspect cancelled invoices

print("\n--- CANCELLED INVOICE EXAMPLES ---")

cancelled = df["InvoiceNo"].astype(str).str.startswith("C")

print(
    df.loc[
        cancelled,
        ["InvoiceNo", "Quantity", "UnitPrice", "InvoiceDate"]
    ].head(10)
)


# 3. Inspect negative quantity records

print("\n--- NEGATIVE QUANTITY EXAMPLES ---")

print(
    df.loc[
        df["Quantity"] < 0,
        ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]
    ].head(10)
)


# 4. Inspect negative unit price

print("\n--- NEGATIVE UNIT PRICE EXAMPLES ---")

print(
    df.loc[
        df["UnitPrice"] < 0,
        ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]
    ]
)


# 5. Inspect zero unit price

print("\n--- ZERO UNIT PRICE EXAMPLES ---")

print(
    df.loc[
        df["UnitPrice"] == 0,
        ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]
    ].head(10)
)
# Export dataset to CSV format
df.to_csv("data/Online_Retail.csv", index=False)

print("\n--- CSV EXPORT ---")
print("CSV file created successfully!")