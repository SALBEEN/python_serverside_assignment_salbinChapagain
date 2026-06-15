import json

with open("demo/products.json", "r") as file:
    products = json.load(file)

print("------------------------------------------")
print("Product Name      | Price     | Quantity")
print("------------------------------------------")

for item in products:
    name = item["name"]
    price = item["price"]
    qty = item["quantity"]
    
    print(str(name).ljust(17) + " | $" + str(price).ljust(8) + " | " + str(qty))

print("------------------------------------------")