# # STEP 1 — Import pandas
import pandas as pd

# # STEP 2 — Create messy dataset (added Date + messy City + duplicate row)
# data = {
#     "CustomerID": [101,102,103,104,105,106,107,107,108,109],
#     "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
#     "Age": [25,None,30,22,None,28,35,35,None,26],
#     "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
#     "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
#     "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
#     "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
#              "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
# }

# df = pd.DataFrame(data)

# # STEP 3 — Inspect dataset
# print("First rows:\n", df.head())
# print("\nDataset info:")
# print(df.info())

# # STEP 4 — Check missing values
# print("\nMissing values per column:")
# print(df.isna().sum())

# # STEP 5 — Fill missing values (statistical approach)
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
# df["City"] = df["City"].fillna(df["City"].mode()[0])
# df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
# df["Name"] = df["Name"].fillna("Unknown")

# # STEP 6 — Check data types before conversion
# print("\nData types BEFORE conversion:")
# print(df.dtypes)

# # STEP 7 — Convert data types
# df["Age"] = df["Age"].astype(int)
# df["Date"] = pd.to_datetime(df["Date"])

# print("\nData types AFTER conversion:")
# print(df.dtypes)

# # -------------------------------------------------
# # NEW PART — STRING CLEANING
# # -------------------------------------------------

# # Strip extra spaces from City names
# df["City"] = df["City"].str.strip()

# # Convert City names to lowercase
# df["City"] = df["City"].str.lower()

# print("\nCity column after cleaning:")
# print(df["City"])

# # -------------------------------------------------
# # NEW PART — DUPLICATE HANDLING
# # -------------------------------------------------

# # Check duplicate rows
# print("\nNumber of duplicate rows:")
# print(df.duplicated().sum())

# # Remove duplicates
# df = df.drop_duplicates()

# print("\nShape after removing duplicates:", df.shape)

# # FINAL CLEAN DATASET
# print("\nFinal cleaned dataset:")
# print(df.head())

# df.to_pickle("cleaned_data.pkl")


#data=pd.read_csv("customer_orders.csv")
#print("frist row:\n",data.head())
#print(data.isna().sum())
#data["order_id"] = data["order_id"].fillna(data["order_id"].median())
#print("duplicate count:",data.duplicated().sum())
#data_cleaned=data.drop_duplicates()
#print("shape of data set before cleaning:",data.shape)
#print("shape of data set after cleanning:",data_cleaned.shape)

# print(len(data_cleaned))
# data_cleaned = data.drop_duplicates().copy()
# data_cleaned["product_name"] = data_cleaned["product_name"].str.strip()
#Task-2
#Task-2
import pandas as pd
df = pd.read_csv("sample_price_data.csv")
print("Before cleaning:")
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print("\nAfter cleaning:")
print(df.dtypes)
print("\nAverage Price:", df["Price"].mean())

