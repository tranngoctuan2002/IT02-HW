def cart_stats(cart):
    total_value, total_quantity = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_value += c['quantity'] * c['price']

    return {
        'total_value': total_value,
        'total_quantity': total_quantity
    }