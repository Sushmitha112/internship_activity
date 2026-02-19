import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.hist(data["value"], bins=10)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Values")
plt.show()

print("Mean:", data["value"].mean())
print("Median:", data["value"].median())

import numpy as np

mean = data["value"].mean()
std = data["value"].std()

data["z_score"] = (data["value"] - mean) / std
print(data.head())

means = []

for _ in range(1000):
    sample = np.random.choice(data["value"], size=30) #taking the random sample from entire population
    means.append(sample.mean()) #taking the average of the samples to convert it into normal disribution
plt.figure()
plt.hist(means, bins=30)
plt.title("Distribution of Sample Means")
plt.show()


#Tak-1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)
data = pd.DataFrame({
    "value": np.random.exponential(scale=50, size=500)
})

Plot Histogram + KDE (ONE graph)
plt.figure(figsize=(6,4))
sns.histplot(data["value"], kde=True)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Values")
plt.show()

#Compare Mean & Median
mean = data["value"].mean()
median = data["value"].median()

print("Mean:", mean)
print("Median:", median)

#Task-2
import numpy as np
import pandas as pd
df = pd.read_csv("data.csv")
data=pd.DataFrame(df)
print(data.dtypes)
mean=data["value"].mean()
std=data["value"].std()
print("means is:",mean)
print("standard deviation is:",std)
data["z_score"] = (data["value"] - mean) / std
print("outliers",data["z_score"].head(5))
outliers = data[np.abs(data["z_score"]) > 3]
print("Outliers:")
print(outliers)

#Task-3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)

# Heavily skewed dataset
data = pd.DataFrame({
    "income": np.random.exponential(scale=50, size=1000)
})
sample_mean =[]
for i in range(1000):
    sample = np.random.choice(data["income"], size=30)
    sample_mean.append(sample.mean())
sns.histplot(sample,kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
    
    



                 
