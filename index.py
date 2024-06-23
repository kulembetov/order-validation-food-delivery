def check_inventory(cart_items):
    for item in cart_items:
        if not item.is_in_stock():
            return False, item
        return True, None

def reserve_stock(cart_items):
    for item in cart_items:
        item.reserve()

def validate_cart(cart_items):
    is_valid, out_of_stock_item, = check_inventory(cart_items)
    if not is_valid:
        return f"Item {out_of_stock_item.name} is out of stock. Please remove or replace it."
    reserve_stock(cart_items)
    return "Cart is valid and items reserved."

def process_order(cart):
    validation_message = validate_cart(cart.items)
    if validation_message != "Cart is valid and items reserved.":
        return validation_message

    if cart.total >= FREE_DELIVERY_THRESHOLD:
        apply_free_delivery(cart)

    confirm_order(cart)
    return "Order confirmed!"

cart = get_user_cart()
order_status = process_order(cart)
print(order_status)