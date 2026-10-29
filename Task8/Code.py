orders = []
n = int(input("Enter number of orders: "))
for i in range(n):
    print("\nOrder", i + 1)
    name = input("Enter product name: ")
    stock = int(input("Enter available stock: "))
    quantity = int(input("Enter order quantity: "))
    priority = input("Enter priority (High/Medium/Low): ").title()
    orders.append({
        "name": name,
        "stock": stock,
        "quantity": quantity,
        "priority": priority
    })
priority_order = {"High": 1, "Medium": 2, "Low": 3}
orders.sort(key=lambda x: priority_order.get(x["priority"], 4))
stock_data = {}
for order in orders:
    name = order["name"]
    if name not in stock_data:
        stock_data[name] = order["stock"]
    available = stock_data[name]
    fulfilled = min(available, order["quantity"])
    outstanding = order["quantity"] - fulfilled
    stock_data[name] -= fulfilled
    if outstanding == 0:
        status = "Fulfilled"
    elif fulfilled > 0:
        status = "Partially Fulfilled"
    else:
        status = "Not Fulfilled"
    print("\nProduct:", name)
    print("Priority:", order["priority"])
    print("Fulfilled Quantity:", fulfilled)
    print("Outstanding Quantity:", outstanding)
    print("Status:", status)

