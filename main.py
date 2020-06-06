import csv

def calculate_average_monthly_change_housing_price(years_to_check):
    vancouver_values, victoria_values = [], []
    vancouver_average, victoria_average = 0, 0

    with open("housing_price_percentage_change_montly\\18100205.csv", "rt") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "Vancouver, British Columbia" in row["GEO"] and any(year in row["ï»¿\"REF_DATE\""] for year in years_to_check) and row["New housing price indexes"] == "Total (house and land)":
                vancouver_values.append(float(row["VALUE"]))

            elif "Victoria, British Columbia" in row["GEO"] and any(year in row["ï»¿\"REF_DATE\""] for year in years_to_check) and row["New housing price indexes"] == "Total (house and land)":
                victoria_values.append(float(row["VALUE"]))

    for i in range(len(vancouver_values) - 1):
        vancouver_average += vancouver_values[i + 1] - vancouver_values[i]

    vancouver_average /= len(vancouver_values) - 1

    for i in range(len(vancouver_values) - 1):
        victoria_average += victoria_values[i + 1] - victoria_values[i]

    victoria_average /= len(victoria_values) - 1

    return vancouver_average, victoria_average

def calculate_average_rent_price_change(years_to_check):
    vancouver_values, victoria_values = [], []

    unit_types = ["Bachelor units", "One bedroom units"]
    with open("average_rent_price_monthly\\34100133.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "Vancouver, British Columbia" in row["GEO"] and any(year in row["ï»¿\"REF_DATE\""] for year in years_to_check) and row["Type of unit"] in unit_types:
                if row["VALUE"]:
                    vancouver_values.append(float(row["VALUE"]))

            elif "Victoria, British Columbia" in row["GEO"] and any(year in row["ï»¿\"REF_DATE\""] for year in years_to_check) and row["Type of unit"] in unit_types:
                if row["VALUE"]:
                    victoria_values.append(float(row["VALUE"]))

    vancouver_change, victoria_change = 0, 0

    for i in range(len(vancouver_values) - 1):
        vancouver_change += vancouver_values[i + 1] - vancouver_values[i]

    for i in range(len(victoria_values) - 1):
        victoria_change += victoria_values[i + 1] - victoria_values[i]

    vancouver_change /= len(vancouver_values)
    victoria_change /= len(victoria_values)

    return vancouver_change, victoria_change

def calculate_average_rent_price(years_to_check=["2019"]):
    vancouver_values, victoria_values = [], []

    unit_types = ["Bachelor units", "One bedroom units"]
    with open("average_rent_price_monthly\\34100133.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if "Vancouver, British Columbia" in row["GEO"] and any(year in row["ï»¿\"REF_DATE\""] for year in years_to_check) and row["Type of unit"] in unit_types:
                if row["VALUE"]:
                    vancouver_values.append(float(row["VALUE"]))

            elif "Victoria, British Columbia" in row["GEO"] and any(year in row["ï»¿\"REF_DATE\""] for year in years_to_check) and row["Type of unit"] in unit_types:
                if row["VALUE"]:
                    victoria_values.append(float(row["VALUE"]))
    
    vancouver_average = sum(vancouver_values) / len(vancouver_values)
    victoria_average = sum(victoria_values) / len(victoria_values)

    return vancouver_average, victoria_average

years_to_check = ["20" + str(tens) + str(ones) for tens in range(2) for ones in range(10)]

print(calculate_average_monthly_change_housing_price(years_to_check))
print(calculate_average_rent_price_change(years_to_check))
print(calculate_average_rent_price())