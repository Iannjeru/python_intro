def calculate_discount(original_price, discount_percent):
    if discount_percent >= 20:
        final_price = original_price - (original_price * discount_percent / 100)
        return final_price
    else:
        return original_price

original_price= float(input("Enter original price: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount_percent)
if discount_percent >= 20:
        print(f'Final price after {discount_percent}% discount is: {final_price}')
else:
        print("No discount applied")