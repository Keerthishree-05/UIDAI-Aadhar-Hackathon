import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# 1. BASIC SETTINGS
# --------------------------------------------
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# --------------------------------------------
# 2. LOAD DATA (CSV FILE)
# --------------------------------------------
df = pd.read_csv("api_data_aadhar_demographic.csv")

# --------------------------------------------
# 3. COLUMN CLEANING
# --------------------------------------------
df.columns = df.columns.str.strip()

# Rename column safely (based on your dataset)
df = df.rename(columns={
    'demo_age_17_': 'demo_age_17_plus'
})

# --------------------------------------------
# 4. DATE CLEANING (INDIAN FORMAT)
# --------------------------------------------
df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)
df = df.dropna(subset=['date'])

# --------------------------------------------
# 5. FEATURE ENGINEERING
# --------------------------------------------
df['total_updates'] = df['demo_age_5_17'] + df['demo_age_17_plus']

# Avoid division by zero
df['UDR'] = np.where(
    df['total_updates'] > 0,
    df['demo_age_17_plus'] / df['total_updates'],
    0
)

# --------------------------------------------
# 6. UNIVARIATE ANALYSIS
# --------------------------------------------
age_totals = df[['demo_age_5_17', 'demo_age_17_plus']].sum()

age_totals.plot(kind='bar', color=['#4C72B0', '#DD8452'])
plt.title("Age-wise Distribution of Aadhaar Demographic Updates")
plt.ylabel("Number of Updates")
plt.show()

# --------------------------------------------
# 7. TIME-SERIES ANALYSIS
# --------------------------------------------
monthly_updates = df.groupby(df['date'].dt.to_period('M'))['total_updates'].sum()
monthly_updates.index = monthly_updates.index.to_timestamp()

plt.plot(monthly_updates, label="Monthly Updates")
plt.plot(monthly_updates.rolling(3).mean(), label="3-Month Moving Average", linewidth=3)
plt.title("Monthly Aadhaar Demographic Update Trend")
plt.xlabel("Time")
plt.ylabel("Total Updates")
plt.legend()
plt.show()

# --------------------------------------------
# 8. GROWTH RATE ANALYSIS
# --------------------------------------------
growth_rate = monthly_updates.pct_change() * 100

growth_rate.plot(kind='bar')
plt.axhline(0, color='red')
plt.title("Month-on-Month Growth Rate of Demographic Updates (%)")
plt.ylabel("Growth Rate (%)")
plt.show()

# --------------------------------------------
# 9. DISTRICT-WISE ANALYSIS
# --------------------------------------------
district_updates = df.groupby('district')['total_updates'].sum().sort_values(ascending=False)

district_updates.head(15).plot(kind='bar')
plt.title("Top Districts by Aadhaar Demographic Updates")
plt.ylabel("Total Updates")
plt.show()

# --------------------------------------------
# 10. UPDATE DOMINANCE RATIO (KEY METRIC)
# --------------------------------------------
district_udr = df.groupby('district')['UDR'].mean().sort_values(ascending=False)

district_udr.plot(kind='bar')
plt.title("Adult vs Child Update Dominance by District (UDR)")
plt.ylabel("Update Dominance Ratio")
plt.show()

# --------------------------------------------
# 11. HEATMAP – DISTRICT vs AGE GROUP
# --------------------------------------------
district_age = df.groupby('district')[['demo_age_5_17', 'demo_age_17_plus']].sum()

sns.heatmap(district_age, cmap="YlGnBu")
plt.title("District-wise Demographic Update Heatmap")
plt.show()

# --------------------------------------------
# 12. PINCODE HOTSPOT DETECTION
# --------------------------------------------
pincode_updates = df.groupby('pincode')['total_updates'].sum()

threshold = pincode_updates.quantile(0.95)
hotspots = pincode_updates[pincode_updates > threshold]

hotspots.head(15).plot(kind='bar')
plt.title("High-Intensity Aadhaar Update Hotspot Pincodes")
plt.ylabel("Total Updates")
plt.show()

# --------------------------------------------
# 13. OUTLIER ANALYSIS
# --------------------------------------------
sns.boxplot(x=df['total_updates'])
plt.title("Outlier Detection in Aadhaar Demographic Updates")
plt.show()

# --------------------------------------------
# 14. CORRELATION ANALYSIS
# --------------------------------------------
corr = df[['demo_age_5_17', 'demo_age_17_plus', 'total_updates']].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Age-wise Demographic Updates")
plt.show()

# --------------------------------------------
# 15. SUMMARY STATISTICS
# --------------------------------------------
print("Summary Statistics:")
print(df[['demo_age_5_17', 'demo_age_17_plus', 'total_updates', 'UDR']].describe())

print("\n✅ Analysis completed successfully.")
