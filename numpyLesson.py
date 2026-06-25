import numpy as np

# Column headers for the sales dataset
data_structure = ["id", 2021, 2022, 2023, 2024]

# Each row: [id, 2021_sales, 2022_sales, 2023_sales, 2024_sales]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # pune
    [2, 120000, 140000, 160000, 190000],  # mumbai
    [3, 200000, 230000, 260000, 300000],  # Delhi
    [4, 180000, 210000, 240000, 270000],  # hyd
    [5, 160000, 185000, 205000, 230000],  # beng
])

city_names = ["pune", "mumbai", "Delhi", "hyd", "beng"]

print(sales_data)
print("****************Sales Analysis*************")

# Data shape
print("Data shape:", sales_data.shape)

# Data size
print("Data size:", sales_data.size)

# Print without id (slicing)
sales_without_id = sales_data[:, 1:]
print("Sales data without id:\n", sales_without_id)

# Total Sales Per year
print("Total Sales Per year:")
for year, total in zip(data_structure[1:], sales_without_id.sum(axis=0)):
    print(f"{year}: {total}")

# Total Sales per city
print("Total Sales per city:")
for city, total in zip(city_names, sales_without_id.sum(axis=1)):
    print(f"{city}: {total}")

# Cumulative sales: cumsum
print("Cumulative sales (cumsum):")
print(sales_without_id.cumsum(axis=0))

# Min Sales per year
print("Min Sales per year:")
for year, minimum in zip(data_structure[1:], sales_without_id.min(axis=0)):
    print(f"{year}: {minimum}")

# Max sales per year
print("Max Sales per year:")
for year, maximum in zip(data_structure[1:], sales_without_id.max(axis=0)):
    print(f"{year}: {maximum}")

# Avg sales per year
print("Avg Sales per year:")
for year, average in zip(data_structure[1:], sales_without_id.mean(axis=0)):
    print(f"{year}: {average}")

# Min Sales per city
print("Min Sales per city:")
for city, minimum in zip(city_names, sales_without_id.min(axis=1)):
    print(f"{city}: {minimum}")

# Max sales per city
print("Max Sales per city:")
for city, maximum in zip(city_names, sales_without_id.max(axis=1)):
    print(f"{city}: {maximum}")

# Avg sales per city
print("Avg Sales per city:")
for city, average in zip(city_names, sales_without_id.mean(axis=1)):
    print(f"{city}: {average}")
