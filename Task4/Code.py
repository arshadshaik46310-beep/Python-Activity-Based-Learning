weight = float(input("Enter parcel weight in kg: "))
length = float(input("Enter length in cm: "))
width = float(input("Enter width in cm: "))
height = float(input("Enter height in cm: "))
zone = input("Enter distance zone (Local/National): ").lower()
urgency = input("Enter urgency (Normal/Express): ").lower()
restricted = input("Is the parcel restricted? (yes/no): ").lower()
volume = length * width * height
services = {
    "Basic Courier": {"rate": 40, "max_weight": 10,
                      "max_volume": 50000, "restricted": False},
    "Fast Courier": {"rate": 70, "max_weight": 20,
                     "max_volume": 100000, "restricted": False},
    "Premium Courier": {"rate": 100, "max_weight": 50,
                        "max_volume": 200000, "restricted": True}
}
zone_charge = 20 if zone == "local" else 60
urgency_charge = 50 if urgency == "express" else 0
eligible = []
for name, service in services.items():
    if (weight <= service["max_weight"]
            and volume <= service["max_volume"]
            and (restricted == "no" or service["restricted"]))
        charge = service["rate"] * weight
        charge += zone_charge + urgency_charge
        eligible.append((name, charge))
if eligible:
    print("\nEligible Courier Services:")
    for name, charge in eligible:
        print(name, "- Rs.", round(charge, 2))
    best = min(eligible, key=lambda x: x[1])
    print("\nCheapest Service:", best[0])
    print("Total Courier Charge: Rs.", round(best[1], 2))
else:
    print("\nNo eligible courier service available.")

