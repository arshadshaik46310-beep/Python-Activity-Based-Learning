n = int(input("Enter number of products: "))
for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    actual = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum stock level: "))
    expected = opening + incoming - dispatched
    discrepancy = actual - expected
    replenishment = max(0, minimum - actual)
    print("\n--- Inventory Report ---")
    print("Product Name:", name)
    print("Expected Closing Stock:", expected)
    print("Actual Closing Stock:", actual)
    if discrepancy == 0:
        print("Stock Status: No Discrepancy")
    else:
        print("Stock Discrepancy:", discrepancy)
    print("Replenishment Required:", replenishment)

