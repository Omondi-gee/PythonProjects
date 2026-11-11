shopping_price = float(input("Enter the store's display price: "))
def apply_discount(original_price, discount_amount):
    final_price = original_price - discount_amount
    return final_price

shopping_price = apply_discount(shopping_price, 30)
print(f"The discounted price is Ksh{shopping_price:.2f  }") #the right side runs first i.e (the code block2 inside function )then stores the returned value to the left 

