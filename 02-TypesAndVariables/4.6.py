price = float(input('Enter price: '))
discount_pct = float(input('Enter discount %: '))
discounted = price * (1 - discount_pct/100)
reduction = price - discounted

print(f'Price with discount: {discounted:.2f}')
print(f'Reduction: {reduction:.2f}')