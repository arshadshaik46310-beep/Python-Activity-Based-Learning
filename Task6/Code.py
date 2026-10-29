appliances = ["Fan", "AC", "Refrigerator"]
days = 7
limit = float(input("Enter daily consumption limit in kWh: "))
readings = []
for appliance in appliances:
    print("\nEnter 7-day readings for", appliance)
    values = []
    for day in range(days):
        value = float(input("Day " + str(day + 1) + ": "))
        values.append(value)
    readings.append(values)
print("\n--- Appliance-wise Total ---")
for i in range(len(appliances)):
    print(appliances[i], ":", sum(readings[i]), "kWh")
print("\n--- Daily Consumption ---")
for day in range(days):
    total = sum(readings[i][day] for i in range(len(appliances)))
    print("Day", day + 1, ":", total, "kWh")
    if total > limit:
        print("Warning: Consumption exceeds limit!")
