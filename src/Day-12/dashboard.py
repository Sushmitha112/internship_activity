import matplotlib.pyplot as plt

# ---------------------------
# Subplot 1: Bar Chart
# ---------------------------

categories = ['Electronics', 'Clothing', 'Home']
values = [300, 450, 200]

plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.bar(categories, values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")


# ---------------------------
# Subplot 2: Line Plot
# ---------------------------

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 280, 350]

plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")


# Prevent overlapping
plt.tight_layout()

plt.show()
