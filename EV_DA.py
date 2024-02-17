import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("/Users/sameerkallurkar/python/DS/EVP/ElectricCarData_Norm.csv")

# Data cleaning
# Dropping duplicates
df.drop_duplicates(inplace=True)
# Stripping Units and renaming columns
df['TopSpeed'] = df['TopSpeed'].str.strip(' km/h')
df.rename(columns={'TopSpeed': 'TopSpeed_km/h'}, inplace=True)
df['FastCharge'] = df['FastCharge'].str.strip(' km/h')
df.rename(columns={'FastCharge': 'FastCharge_km/h'}, inplace=True)
df['Range'] = df['Range'].str.strip(' km')
df.rename(columns={'Range': 'Range_km'}, inplace=True)
df['Efficiency'] = df['Efficiency'].str.strip(' Wh/km')
df.rename(columns={'Efficiency': 'Efficiency_Wh/km'}, inplace=True)
df['Accel'] = df['Accel'].str.strip(' sec')
df.rename(columns={'Accel': 'Accel_sec'}, inplace=True)
# Replacing the values
df['RapidCharge'] = df['RapidCharge'].str.replace("Rapid charging possible", 'Yes')
df['RapidCharge'] = df['RapidCharge'].str.replace("Rapid charging not possible", 'No')
df['PowerTrain'] = df['PowerTrain'].str.replace('All Wheel Drive', 'AWD')
df['PowerTrain'] = df['PowerTrain'].str.replace('Rear Wheel Drive', 'RWD')
df['PowerTrain'] = df['PowerTrain'].str.replace('Front Wheel Drive', 'FWD')

# Converting dtypes
df['Accel_sec'] = pd.to_numeric(df['Accel_sec'], errors='coerce')
df['TopSpeed_km/h'] = df['TopSpeed_km/h'].astype(int)
df['Range_km'] = df['Range_km'].astype(int)
df['Efficiency_Wh/km'] = df['Efficiency_Wh/km'].astype(int)
df['FastCharge_km/h'] = df['FastCharge_km/h'].str.replace('-', '')
df['FastCharge_km/h'] = pd.to_numeric(df['FastCharge_km/h'], errors='coerce')
df['FastCharge_km/h'].fillna(df['FastCharge_km/h'].mean(), inplace=True)
df['FastCharge_km/h'] = df['FastCharge_km/h'].round().astype(int)

# Plotting multiple graphs in a single figure
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(20, 18))


# Top 10 Brands with the Most Number of Electric Cars
brand_counts = df['Brand'].value_counts().head(10)
brand_counts.plot(kind='bar', ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Top 10 Brands with the Most Number of Electric Cars')
axes[0, 0].set_xlabel('Brand')
axes[0, 0].set_ylabel('Number of Electric Cars')

# Top 5 Fastest Electric Cars
fastest_cars = df.sort_values(by='TopSpeed_km/h').head(5)
fastest_cars['Brand_Model'] = fastest_cars['Brand'] + ' ' + fastest_cars['Model']
fastest_cars.plot(kind='barh', x='Brand_Model', y='TopSpeed_km/h', ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('Top 5 Fastest Electric Cars')
axes[0, 1].set_xlabel('Speed (Km/h)')
axes[0, 1].set_ylabel('Car Model')

# Top 5 Efficient Electric Cars
efficient_car = df.sort_values(by='Efficiency_Wh/km').head(5)
efficient_car['Brand_Model'] = efficient_car['Brand'] + ' ' + efficient_car['Model']
efficient_car.plot(kind='barh', x='Brand_Model', y='Efficiency_Wh/km', ax=axes[1, 0], color='lightcoral')
axes[1, 0].set_title('Top 5 Efficient Electric Cars')
axes[1, 0].set_xlabel('Efficiency (Wh/km)')
axes[1, 0].set_ylabel('Car Model')

# Scatter plot for acceleration vs. top speed
axes[1, 1].scatter(df['Accel_sec'], df['TopSpeed_km/h'], color='skyblue', alpha=0.3)
axes[1, 1].set_title('Acceleration vs. Top Speed of Electric Vehicles')
axes[1, 1].set_xlabel('Acceleration (seconds)')
axes[1, 1].set_ylabel('Top Speed (km/h)')
axes[1, 1].grid(True)

# Rotate x-axis labels for better readability in histogram
axes[2, 0].tick_params(axis='x', rotation=45)

# Histogram for acceleration with custom bins and labels
accel_bins = np.arange(df['Accel_sec'].min(), df['Accel_sec'].max() + 1, 0.5)
axes[2, 0].hist(df['Accel_sec'], bins=accel_bins, color='skyblue', edgecolor='black')
axes[2, 0].set_title('Distribution of Acceleration of Electric Vehicles')
axes[2, 0].set_xlabel('Acceleration (seconds)')
axes[2, 0].set_ylabel('Frequency')
axes[2, 0].grid(True)

# Adjust layout to prevent overlapping labels
plt.tight_layout(pad=3.0)

# Histogram for top speed
axes[2, 1].hist(df['TopSpeed_km/h'], bins=20, color='skyblue', edgecolor='black')
axes[2, 1].set_title('Distribution of Top Speed of Electric Vehicles')
axes[2, 1].set_xlabel('Top Speed (km/h)')
axes[2, 1].set_ylabel('Frequency')
axes[2, 1].grid(True)

plt.tight_layout()
plt.show()
