order_list = [
    [
        ["Laptop", True, False],  # fragile, tax-exempt
        ["Phone", False, False],
        ["Dairy", 2.0, True]  # 2 kg, perishable
    ],
    [
        ["Sofa", True],  # large
        ["Fruits", 3.0, False],  # 3 kg, not perishable
        ["Table", False]  # not large
    ],
    [
        ["Tablet", True, True],  # fragile, tax-exempt
        ["Phone", False, True],  # not fragile, tax-exempt
        ["Vegetables", 5.0, False]  # 5 kg, not perishable
    ],
    [
        ["TV", "large", False]  # invalid item
    ]
]

for order in order_list:
    total_proce = 0.0
    for item in order:
        item[0] = item[0].lower()
        match item:
            case "laptop" | "phone" | "tablet" as electronics, fragile, tax_exempt:
                if electronics == "laptop":
                    base_price = 499.99
                elif electronics == "phone":
                    base_price = 299.99
                else:
                    base_price = 199.99

                total_proce += base_price

                if fragile:
                    total_proce += 20.00

                if not tax_exempt:
                    total_proce += base_price * 0.08

                print(f"Electronics: {electronics}", "Fragile" if fragile else "", "tax exempt" if tax_exempt else "")

            case "fruits" | "vegetables" | " dairy" as grocery, weight, perishable:
                if perishable:
                    total_proce += 5.00

                if grocery == "fruits":
                    price_per_kg = 3.99
                elif grocery == "vegetables":
                    price_per_kg = 2.99
                else:
                    price_per_kg = 4.99

                total_proce += weight * price_per_kg

                print(f"Grocery: {grocery}, weight: {weight:.2f}kg", "perishable" if perishable else "")

            case "table" | "Chair" | "Sofa" as furnitures, large:
                if large:
                    total_proce += 50.00

                if furnitures == "table":
                    total_proce += 150.00
                elif furnitures == "Chair":
                    total_proce += 80.00
                else:
                    total_proce += 250.00
                    
                print(f"Furnitures:{furnitures}", "Large" if large else "")

            case _:
                print("invalid item")

    if len(order) >= 3:
        total_proce *= 0.90 

    print(f"order total : {total_proce:.2f}")
