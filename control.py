def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to apply.

  Returns:
    The final price after applying the discount.
  """

  if discount_percent >= 20:
    return price * (1 - discount_percent / 100)
  else:
    return price


# Get the user input.
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (in %): "))

# Calculate the final price.
final_price = calculate_discount(price, discount_percent)

# Print the final price.
if discount_percent >= 20:
  print(f"The final price after applying the discount is ${final_price:.2f}.")
else:
  print("No discount was applied. The price remains ${price:.2f}.")