import pandas as pd
import matplotlib.pyplot as plt

# ===== Load Dataset Once =====
df = pd.read_csv("practicedata.csv")

# Clean column names globally
df.columns = df.columns.str.strip().str.lower()

# ===== Graph 1: Bar Chart - Most Common CPU Types =====
cpu_df = df.copy()
cpu_df['core'] = cpu_df['core'].dropna().astype(str).str.strip()

cpu_counts = cpu_df['core'].value_counts()

plt.figure()
cpu_counts.plot(kind='bar')

plt.xlabel("CPU Type")
plt.ylabel("Number of Laptops")
plt.title("Most Common Laptop CPUs")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ===== Graph 2: Pie Chart - Brand Distribution =====
brand_df = df.copy()
brand_df['brand'] = brand_df['brand'].dropna().astype(str).str.strip()

brand_counts = brand_df['brand'].value_counts().head(5)

plt.figure()
plt.pie(
    brand_counts,
    labels=brand_counts.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Brand-wise Distribution of Laptops")
plt.tight_layout()
plt.show()


# ===== Graph 3: Step Chart - Price Range Distribution =====
price_df = df.copy()

price_df['actual price'] = price_df['actual price'].replace('[₹,]', '', regex=True)
price_df['actual price'] = pd.to_numeric(price_df['actual price'], errors='coerce')
price_df = price_df.dropna(subset=['actual price'])

bins = [0, 100000, 150000, 200000, 250000, 300000]
labels = ['0-100k', '100-150k', '150-200k', '200-250k', '250k+']

price_df['price_range'] = pd.cut(price_df['actual price'], bins=bins, labels=labels)

counts = price_df['price_range'].value_counts().sort_index()

plt.figure()
plt.step(range(len(counts)), counts.values, where='mid')

plt.xticks(range(len(counts)), counts.index, rotation=45)

plt.xlabel("Price Range")
plt.ylabel("Number of Laptops")
plt.title("Laptop Distribution by Price Slabs (Step Chart)")

plt.tight_layout()
plt.show()


# ===== Graph 4: Line Chart - Average Price by CPU =====
cpu_price_df = df.copy()

cpu_price_df['core'] = cpu_price_df['core'].astype(str).str.strip()
cpu_price_df['actual price'] = cpu_price_df['actual price'].replace('[₹,]', '', regex=True)
cpu_price_df['actual price'] = pd.to_numeric(cpu_price_df['actual price'], errors='coerce')

cpu_price_df = cpu_price_df.dropna(subset=['core', 'actual price'])

cpu_avg = cpu_price_df.groupby('core')['actual price'].mean()

top_cpus = cpu_price_df['core'].value_counts().head(8).index
cpu_avg = cpu_avg.loc[top_cpus]

cpu_avg = cpu_avg.sort_values()

plt.figure()
plt.plot(cpu_avg.index, cpu_avg.values, marker='o')

plt.xlabel("CPU Type")
plt.ylabel("Average Actual Price")
plt.title("Average Laptop Price by CPU")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ===== Graph 5: Histogram - Actual vs Discounted Price =====
hist_df = df.copy()

hist_df['actual price'] = hist_df['actual price'].replace('[₹,]', '', regex=True)
hist_df['discounted price'] = hist_df['discounted price'].replace('[₹,]', '', regex=True)

hist_df['actual price'] = pd.to_numeric(hist_df['actual price'], errors='coerce')
hist_df['discounted price'] = pd.to_numeric(hist_df['discounted price'], errors='coerce')

hist_df = hist_df.dropna(subset=['actual price', 'discounted price'])

plt.figure()
plt.hist(hist_df['actual price'], bins=20, alpha=0.5, label='Actual Price')
plt.hist(hist_df['discounted price'], bins=20, alpha=0.5, label='Discounted Price')

plt.xlabel("Price")
plt.ylabel("Number of Laptops")
plt.title("Actual vs Discounted Price Distribution")

plt.legend()
plt.tight_layout()
plt.show()


# ===== Analysis 1: Missing Values =====
print("True - Missing values in dataset:")
print(df.isnull())

print("\nTotal missing values per column:")
print(df.isnull().sum())


# ===== Analysis 2: Outlier Detection =====
def find_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return column[(column < lower_bound) | (column > upper_bound)]

for col in df.select_dtypes(include=['number']).columns:
    outliers = find_outliers(df[col])
    print(f"\nOutliers in {col}:")
    print(outliers)