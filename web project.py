# ==========================================
# CAR SALES DATA ANALYSIS PROJECT
# ==========================================

# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# STEP 1: CREATE CAR SALES DATASET
# ------------------------------------------

data = {
    "Car_Model": [
        "Swift", "Creta", "Nexon", "City", "Baleno",
        "Venue", "Punch", "Scorpio", "Thar", "Verna",
        "Kia Seltos", "Fortuner", "Innova", "Tiago", "Altroz"
    ],

    "Brand": [
        "Maruti", "Hyundai", "Tata", "Honda", "Maruti",
        "Hyundai", "Tata", "Mahindra", "Mahindra", "Hyundai",
        "Kia", "Toyota", "Toyota", "Tata", "Tata"
    ],

    "Sales": [
        5200, 4800, 4500, 3900, 3700,
        3500, 3400, 3200, 3000, 2800,
        2700, 2500, 2300, 2200, 2100
    ]
}

# ------------------------------------------
# STEP 2: STORE DATA IN DATAFRAME
# ------------------------------------------

df = pd.DataFrame(data)

print("\n========== CAR SALES DATA ==========\n")
print(df)

# ------------------------------------------
# STEP 3: DATAFRAME DETAILS
# ------------------------------------------

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== LAST 5 ROWS ==========\n")
print(df.tail())

print("\n========== DATAFRAME INFO ==========\n")
print(df.info())

print("\n========== STATISTICS ==========\n")
print(df.describe())

# ------------------------------------------
# STEP 4: SAVE DATA TO CSV
# ------------------------------------------

df.to_csv("cars_sales.csv", index=False)

print("\n✅ cars_sales.csv file created successfully!")

# ------------------------------------------
# STEP 5: READ CSV FILE
# ------------------------------------------

cars = pd.read_csv("cars_sales.csv")

print("\n========== DATA READ FROM CSV ==========\n")
print(cars.head())

# ------------------------------------------
# STEP 6: VISUALIZATION
# ------------------------------------------

plt.figure(figsize=(12,6))

plt.bar(cars["Car_Model"][:10], cars["Sales"][:10])

plt.title("Top 10 Car Sales")
plt.xlabel("Car Models")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ------------------------------------------
# STEP 7: HIGHEST & LOWEST SALES
# ------------------------------------------

highest = cars.loc[cars["Sales"].idxmax()]
lowest = cars.loc[cars["Sales"].idxmin()]

print("\n========== HIGHEST SALES ==========")
print(highest)

print("\n========== LOWEST SALES ==========")
print(lowest)

# ------------------------------------------
# STEP 8: AVERAGE SALES
# ------------------------------------------

average_sales = cars["Sales"].mean()

print("\nAverage Sales :", average_sales)

# ------------------------------------------
# STEP 9: SORT DATA
# ------------------------------------------

sorted_data = cars.sort_values(by="Sales", ascending=False)

print("\n========== SORTED DATA ==========\n")
print(sorted_data)

# ------------------------------------------
# STEP 10: SAVE SORTED DATA
# ------------------------------------------

sorted_data.to_csv("sorted_car_sales.csv", index=False)

print("\n✅ sorted_car_sales.csv file created successfully!")

print("\n========== PROJECT COMPLETED ==========")
