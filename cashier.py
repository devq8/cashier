def get_invoice_items(items):
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, price: 0.2 },
    #   {'name': 'Orange', 'quantity': 4, price: 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    invoice_items = []
    
    
    for item in items:
        invoice_items.append(f"{item['quantity']} {item['name']} {'{0:.3f}'.format(item['price']*item['quantity'])} KD")

    
    return invoice_items


def get_total(items):
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    total = 0

    for item in items:
        total += (item['quantity']*item['price'])
    return total

def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    print("-----------------------")
    print("        Receipt")
    print("-----------------------")

    for item in invoice_items:
        print(item)
    
    print("-----------------------")
    print(f"Total Price: {'{0:.3f}'.format(total)} KD")

def main():
    # Write your main logic here
    print("\nKindly enter the items bought : ")
    items = []
    
    item = {
                "name": input("\nItem (enter \"done\" when finished): "),
                "price": float(input("Price: ")),
                "quantity": int(input("Quantity: "))
            }
    
    items.append(item)

    while item["name"] != "done" :
        
        name = input("\nItem (enter \"done\" when finished): ")

        if name == "done":
            break
        else:
            item = {
                "name": name,
                "price": float(input("Price: ")),
                "quantity": int(input("Quantity: "))
            }
            items.append(item)

    
    print_receipt( get_invoice_items(items), get_total(items) )


if __name__ == "__main__":
    main()
