
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Define project directories
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "Online_Retail.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "daily_sales.png"

# Load transaction data
df = pd.read_csv(DATA_PATH)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Calculate transaction revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Extract transaction date
df["Date"] = df["InvoiceDate"].dt.date

# Aggregate revenue by day
daily_sales = df.groupby("Date")["Revenue"].sum()

# Create daily sales trend chart
plt.figure(figsize=(14, 6))

plt.plot(
    daily_sales.index,
    daily_sales.values,
    linewidth=1.5
)

plt.title("Daily Sales Trend - UCI Online Retail Dataset")
plt.xlabel("Date")
plt.ylabel("Daily Revenue (£)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save chart
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
plt.close()

print(f"Chart saved successfully: {OUTPUT_PATH}")
