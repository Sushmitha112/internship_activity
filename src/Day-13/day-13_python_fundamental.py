import pandas as pd


df = pd.read_csv("dataset.csv")

df.head()
df.tail()
df.shape
df.info()
df.describe()
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df['Age'], kde=True)
plt.show()

sns.boxplot(x=df['salary'])
plt.show()

df['Gender'].value_counts()

sns.scatterplot(x='Age', y='salary', data=df)
plt.show()

sns.boxplot(x='Gender', y='salary', data=df)
plt.show()
Convert Gender to numeric
df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})

# Convert City to numeric
df["City"] = df["City"].astype("category").cat.codes
df["Join_Date"] = pd.to_datetime(
    df["Join_Date"],
    format="%d-%m-%Y"
)
corr = df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

sns.boxplot(x=df['salary'])
plt.show()

plt.figure(figsize=(6,4))

sns.histplot(df["Purchase_Amount"], kde=False)

plt.title("Histogram of Price with KDE")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

print("Skewness:", df["Purchase_Amount"].skew())
print("Kurtosis:", df["Purchase_Amount"].kurt())

corr_matrix = df.corr(numeric_only=True)

print(corr_matrix)
plt.figure(figsize=(8,6))

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Matrix Heatmap")
plt.show()
plt.figure(figsize=(6,4))

sns.boxplot(y=df["Purchase_Amount"])

plt.title("Boxplot of Purchase Amount")
plt.ylabel("Purchase Amount")

plt.show()

