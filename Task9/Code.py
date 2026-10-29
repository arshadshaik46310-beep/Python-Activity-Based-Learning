n = int(input("Enter number of branches: "))
branches = []
for i in range(n):
    print("\nBranch", i + 1)
    name = input("Enter branch name: ")
    stock = int(input("Enter current stock: "))
    target = int(input("Enter target stock: "))
    branches.append({
        "name": name,
        "stock": stock,
        "target": target,
        "surplus": max(0, stock - target),
        "shortage": max(0, target - stock)
    })
limit = int(input("\nEnter maximum transfer quantity: "))
print("\n--- Inventory Transfers ---")
for source in branches:
    for dest in branches:
        if source["surplus"] > 0 and dest["shortage"] > 0:
            qty = min(source["surplus"], dest["shortage"], limit)
            print(source["name"], "->", dest["name"], ":", qty, "units")
            source["surplus"] -= qty
            dest["shortage"] -= qty
print("\n--- Final Inventory Status ---")
for branch in branches:
    print(branch["name"])
    print("Remaining Surplus:", branch["surplus"])
    print("Remaining Shortage:", branch["shortage"])

