n = int(input("Enter number of passengers: "))
total = 0
if n <= 0:
    print("Invalid number of passengers.")
else:
    for i in range(n):
        print("\nPassenger", i + 1)
        age = int(input("Enter age: "))
        distance = float(input("Enter distance in km: "))
        travel_class = input("Enter class (sleeper/ac): ").lower()
        cancelled = input("Ticket cancelled? (yes/no): ").lower()
        if age < 0 or distance < 0 or travel_class not in ["sleeper", "ac"]:
            print("Invalid passenger details!")
            continue
        if travel_class == "sleeper":
            rate = 1.50
        else:
            rate = 3.00
        if age < 5:
            fare = 0
            reservation = 0
        else:
            fare = distance * rate
            if age >= 60:
                fare *= 0.80
            reservation = 50
        if cancelled == "yes":
            amount = max(0, fare + reservation - 100)
            print("Cancellation Penalty: Rs. 100")
        else:
            amount = fare + reservation
        print("Passenger Fare: Rs.", round(amount, 2))
        total += amount
    print("\nTotal Railway Fare: Rs.", round(total, 2))

