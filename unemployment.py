# Unemployment Analysis in india 

#STEP_1 import required libararies
import pandas as pd   #   pandas is use fir data handling.
import matplotlib.pyplot as plt # matplotlib is used for data visualization



# STEP_2 dataset ko load karege 
# CSV file ko DataFrame me load karna hai

df= pd.read_csv("ML_Project/unemployment_pediction/unemployment in india_Datasets.csv")

#dataset ko first look dege 
print("first 5 rows of dataset:")
print(df.head())


# STEP 3: clean column names .........
    # column names ke extra space ko remove karna.

df.columns = df.columns.str.strip()

print("\nColumns Names:")
print(df.columns)

#....... STEPS__4 CHECKING MISSING VALUES .....
print("\nMissing values before cleaning:")
print(df.isnull().sum())


#.......STEP__5....: REMOVE MISSING VALUES......
#jahan data missing hai wo rows ko hata dena 

df.dropna(inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

#.......STEP__6:.. CONVERT DATE COLUMN TO DATETIME.............
# date ko datetime format mai change karna .

df['Date']= pd.to_datetime(df['Date'])

print("\nData types after Date conversion:")
print(df.dtypes)


#.......STEP 7: ....STATISTICAL SUMMARY.....
print("\nStatistical Summary:")
print(df.describe())

#......STEP 8 :....... OVERALL UMEMPLOYMENT TREND...
plt.figure(figsize=(10,5))

plt.plot(
    df['Date'],
    df['Estimated Unemployment Rate (%)'],
    color='red',
    linestyle='--',
    linewidth=2,
    marker='o'
)

plt.title("Unemployment Rate Trend in India", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()

#....STEP 9.... covid-19 impact analysis...
#2019 ke baad ka data covid period
covid_df = df[df['Date'].dt.year >= 2019]

plt.figure()
plt.plot(
        covid_df['Date'], 
        covid_df['Estimated Unemployment Rate (%)'],
        color='yellow',
        linestyle='--',
        linewidth=2,
        marker='o'
    )

plt.title("covid-19 impact on Unemployment Rate")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#....STEP 10.... Region-wise Average Unemployment.....

region_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nRegion-wise Average Unemployment Rate:")
print(region_avg)

#....STEP 11 ..... Region-wise Bar Chart.......
plt.figure()
region_avg.plot(kind='bar')

plt.title("Average unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()
plt.show()
