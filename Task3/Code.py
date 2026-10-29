budget = float(input("Enter your budget: "))
n = int(input("Enter number of products: "))
products = []
for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    products.append([name, price, quantity])
def calculate_total():
    total = sum(p[1] * p[2] for p in products)
    discount = total * 0.10 if total >= 1000 else 0
    return total - discount, discount
total, discount = calculate_total()
while total > budget:
    reduced = False
    for p in products:
        if p[2] > 0:
            p[2] -= 1
            reduced = True
            total, discount = calculate_total()
            if total <= budget:
                break
    if not reduced:
        break
print("\n--- Final Shopping Bill ---")
for p in products:
    print(p[0], "- Quantity:", p[2],
          "Cost: Rs.", round(p[1] * p[2], 2))
subtotal = sum(p[1] * p[2] for p in products)
print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Total: Rs.", round(total, 2))
print("Remaining Budget: Rs.", round(budget - total, 2))

