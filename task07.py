def calculate_cart(cart: dict) -> int:
    return sum(v['price'] * v['quantity'] for v in cart.values())
cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
print(calculate_cart(cart))
