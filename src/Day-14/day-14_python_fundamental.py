# import pandas as pd
# from sklearn.preprocessing import LabelEncoder


# data = {
#     "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
#     "Color": ["Red", "Blue", "Green", "Red"]
# }

# df = pd.DataFrame(data)

# # -------------------------
# # Label Encoding (Transmission)
# # -------------------------
# le = LabelEncoder()
# df["Transmission"] = le.fit_transform(df["Transmission"])

# # -------------------------
# # One-Hot Encoding (Color)
# # -------------------------
# df = pd.get_dummies(df, columns=["Color"], drop_first=True)
# print(df)

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler, MinMaxScaler

# # Sample Data
# data = {
#     "Age": [22, 25, 30, 35, 40, 45, 50],
#     "Salary": [30000, 35000, 60000, 65000, 70000, 80000, 90000]
# }

# df = pd.DataFrame(data)

# scaler_standard = StandardScaler()
# df_standardized = scaler_standard.fit_transform(df)

# df_standardized = pd.DataFrame(df_standardized, columns=df.columns)

# scaler_minmax = MinMaxScaler()
# df_normalized = scaler_minmax.fit_transform(df)

# df_normalized = pd.DataFrame(df_normalized, columns=df.columns)

# plt.figure(figsize=(12,4))

# # Original
# plt.subplot(1,3,1)
# plt.hist(df["Salary"])
# plt.title("Original Salary")

# # Standardized
# plt.subplot(1,3,2)
# plt.hist(df_standardized["Salary"])
# plt.title("Standardized Salary")

# # Normalized
# plt.subplot(1,3,3)
# plt.hist(df_normalized["Salary"])
# plt.title("Normalized Salary")

# plt.tight_layout()
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
# Create feature
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1,1)

# Non-linear target
y = np.array([1, 4, 9, 16, 25, 36])
model_linear = LinearRegression()
model_linear.fit(X, y)

y_pred_linear = model_linear.predict(X)

r2_linear = r2_score(y, y_pred_linear)

print("R² Score (Linear):", r2_linear)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly, y)

y_pred_poly = model_poly.predict(X_poly)

r2_poly = r2_score(y, y_pred_poly)

print("R² Score (Polynomial):", r2_poly)

