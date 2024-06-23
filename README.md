# Order Validation System for Food Delivery App

Hey there! Let me share an experience I had that led me to come up with this solution. 
I ordered a water, a pie, and some bread from a local delivery app in Thailand. Later, I discovered that the water 
was out of stock, which was a bummer because I really needed it. When the first delivery arrived, 
I found that the pie was also out of stock. When I ordered one pie, only one was delivered.

So, I decided to try something different. I placed a new order for 10 pies, which cost more than 
400 baht (enough to qualify for free delivery) and added a few bottles of water totaling 50 baht. 
This strategy worked, and I got the free delivery. This got me thinking about how such issues 
could be prevented, leading me to write a small script.

### How the Solution Works:
1. Real-time Inventory Check: When a user adds an item to their cart, the system immediately checks 
   the inventory to ensure the item is in stock.
2. Cart Validation at Checkout: Before the user can finalize their order, the system validates the 
   cart to confirm the availability of each item. If any items are out of stock, the user is prompted 
   to remove or replace them.
3. Stock Reservation: When items are added to the cart, the system reserves the stock for a limited 
   time, ensuring the items remain available during the checkout process.
4. Dynamic Free Delivery Threshold: The system ensures that only in-stock items contribute to the 
   minimum purchase amount required for free delivery.
5. Fraud Detection: The system uses algorithms to detect and prevent patterns of fraudulent behavior, 
   such as repeatedly adding out-of-stock items to meet the free delivery threshold.

### Pseudocode Explanation:
Here’s a breakdown of the pseudocode implementing these strategies:
- check_inventory(cart_items): This function checks if each item in the cart is in stock.
- reserve_stock(cart_items): This function reserves stock for each item in the cart.
- validate_cart(cart_items): This function validates the cart by checking inventory and reserving stock.
- process_order(cart): This function processes the order by validating the cart, applying free delivery 
  if eligible, and confirming the order.

# Function to check the inventory for each item in the cart
```def check_inventory(cart_items):
    for item in cart_items:
        # Check if the item is in stock
        if not item.is_in_stock():
            return False, item  # Return False and the out-of-stock item
    return True, None  # Return True if all items are in stock
```

# Function to reserve stock for items in the cart
```def reserve_stock(cart_items):
    for item in cart_items:
        # Reserve the item
        item.reserve()
```
# Function to validate the cart by checking inventory and reserving stock
```angular2html
def validate_cart(cart_items):
    is_valid, out_of_stock_item = check_inventory(cart_items)
    if not is_valid:
        # Return a message if an item is out of stock
        return f"Item {out_of_stock_item.name} is out of stock. Please remove or replace it."
    # Reserve stock for all items
    reserve_stock(cart_items)
    return "Cart is valid and items reserved."
```

# Function to process the order
```
def process_order(cart):
    # Validate the cart
    validation_message = validate_cart(cart.items)
    if validation_message != "Cart is valid and items reserved.":
        return validation_message  # Return the validation message if the cart is not valid
```
# Check if the cart total meets the free delivery threshold
```
if cart.total >= FREE_DELIVERY_THRESHOLD:
        # Apply free delivery if the threshold is met
        apply_free_delivery(cart)
    
    # Confirm the order
    confirm_order(cart)
    return "Order confirmed!"
```    

# Sample usage
```
cart = get_user_cart()  # Get the user's cart
order_status = process_order(cart)  # Process the order
print(order_status)  # Print the order status
```
