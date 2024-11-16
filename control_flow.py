def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
    

price = float(input("Enter the price: "))

discount_percent = float(input("Enter the discount percent: "))

final_price = calculate_discount(price, discount_percent)
print(final_price)

if discount_percent >= 20:
     print(f"The final price after applying the discount is ${final_price:.2f}.")
else:
    print(f"No discount was applied. The price remains ${price:.2f}.")