import csv
import random
from datetime import datetime, timedelta


# Data lists for realistic values
RESTAURANTS = [
    "Burger Planet",
    "Sushi House",
    "Pizza Palace",
    "Taco Fiesta",
    "Pasta Paradise",
    "Curry Corner",
    "Salad Station",
    "Wok Express",
    "BBQ Barn",
    "Dessert Den"
]

MENU_ITEMS = {
    "Burger Planet": ["Cheeseburger", "Double Burger", "Chicken Burger", "Fries", "Onion Rings", "Cola", "Milkshake"],
    "Sushi House": ["Salmon Roll", "Tuna Roll", "Miso Soup", "Edamame", "Green Tea", "Sashimi Platter"],
    "Pizza Palace": ["Margherita Pizza", "Pepperoni Pizza", "Garlic Dip", "Cola", "Caesar Salad", "Breadsticks"],
    "Taco Fiesta": ["Beef Taco", "Chicken Taco", "Nachos", "Guacamole", "Salsa", "Limeade"],
    "Pasta Paradise": ["Spaghetti Carbonara", "Fettuccine Alfredo", "Garlic Bread", "Tiramisu", "Mineral Water"],
    "Curry Corner": ["Chicken Tikka", "Lamb Biryani", "Naan Bread", "Samosa", "Mango Lassi"],
    "Salad Station": ["Caesar Salad", "Greek Salad", "Quinoa Bowl", "Fresh Juice", "Fruit Cup"],
    "Wok Express": ["Kung Pao Chicken", "Fried Rice", "Spring Rolls", "Dumplings", "Green Tea"],
    "BBQ Barn": ["BBQ Ribs", "Pulled Pork", "Coleslaw", "Cornbread", "Iced Tea"],
    "Dessert Den": ["Chocolate Cake", "Ice Cream Sundae", "Cheesecake", "Coffee", "Brownie"]
}

CUSTOMER_NAMES = [
    "Ana Popescu", "Mihai Ionescu", "Ioana Marin", "Vlad Dima", "Elena Radu",
    "Andrei Stan", "Maria Popa", "Cristian Matei", "Diana Voinea", "Alexandru Dumitru",
    "Laura Constantinescu", "Stefan Iorga", "Carmen Ungureanu", "Bogdan Florea", "Ruxandra Mihail"
]

COUPON_CODES = ["WELCOME10", "SUPERFREE", "SAVE20", "FIRSTORDER", "LOYALTY5"]

STATUSES = ["completed", "cancelled", "refunded"]

# Price ranges for items (in RON)
ITEM_PRICES = {
    "Cheeseburger": 25, "Double Burger": 32, "Chicken Burger": 28, "Fries": 12, "Onion Rings": 14,
    "Cola": 8, "Milkshake": 15, "Salmon Roll": 18, "Tuna Roll": 16, "Miso Soup": 10,
    "Edamame": 12, "Green Tea": 6, "Sashimi Platter": 45, "Margherita Pizza": 35,
    "Pepperoni Pizza": 40, "Garlic Dip": 8, "Caesar Salad": 22, "Breadsticks": 10,
    "Beef Taco": 15, "Chicken Taco": 14, "Nachos": 18, "Guacamole": 12, "Salsa": 6,
    "Limeade": 7, "Spaghetti Carbonara": 38, "Fettuccine Alfredo": 36, "Garlic Bread": 12,
    "Tiramisu": 18, "Mineral Water": 5, "Chicken Tikka": 32, "Lamb Biryani": 38,
    "Naan Bread": 8, "Samosa": 10, "Mango Lassi": 12, "Greek Salad": 20, "Quinoa Bowl": 28,
    "Fresh Juice": 12, "Fruit Cup": 15, "Kung Pao Chicken": 34, "Fried Rice": 18,
    "Spring Rolls": 14, "Dumplings": 16, "Green Tea": 5, "BBQ Ribs": 55, "Pulled Pork": 42,
    "Coleslaw": 10, "Cornbread": 8, "Iced Tea": 6, "Chocolate Cake": 22, "Ice Cream Sundae": 18,
    "Cheesecake": 20, "Coffee": 8, "Brownie": 15
}


def get_random_items(restaurant):
    """Get 1-3 random items for a restaurant."""
    items = MENU_ITEMS[restaurant]
    num_items = random.randint(1, 3)
    return random.sample(items, num_items)


def calculate_order_total(items):
    """Calculate total price based on items."""
    return sum(ITEM_PRICES[item] for item in items)


def format_price_variations(price, messy=False):
    """Format price with various messy styles."""
    if messy:
        variation = random.choice([
            f"{price} RON",
            f"{price} ron",
            f" {price} ",
            f"RON {price}",
            f"{price:.2f}RON",
            f"  {price}  "
        ])
        return variation
    return f"{price} RON"


def format_restaurant_name_variations(name, messy=False):
    """Format restaurant name with various messy styles."""
    if messy:
        variation = random.choice([
            name.lower(),
            name.upper(),
            f" {name} ",
            f"  {name.lower()}  ",
            f"{name.upper()} "
        ])
        return variation
    return name


def format_item_variations(items, messy=False):
    """Format items with various messy styles."""
    if messy:
        messy_items = []
        for item in items:
            variation = random.choice([
                item.lower(),
                f" {item}",
                f"{item} ",
                f"  {item}  ",
                item
            ])
            messy_items.append(variation)
        return "|".join(messy_items)
    return "|".join(items)


def generate_date_variations(messy=False):
    """Generate order date with various formats. Returns (date_string, format_identifier)."""
    base_date = datetime(2026, 4, 1) + timedelta(days=random.randint(0, 30))
    
    if messy:
        variation = random.choice([
            (base_date.strftime("%Y-%m-%d"), "YYYY-MM-DD"),
            (base_date.strftime("%Y/%m/%d"), "YYYY/MM/DD"),
            (base_date.strftime("%d-%m-%Y"), "DD-MM-YYYY"),
            (base_date.strftime("%m/%d/%Y"), "MM/DD/YYYY"),
            ("not-a-date", "invalid"),
            ("2026-13-45", "invalid"),  # Invalid date
            ("", "missing")
        ])
        return variation
    return (base_date.strftime("%Y-%m-%d"), "YYYY-MM-DD")


def generate_order_record(order_num, used_order_ids, coupon_usage_by_customer):
    """Generate a single order record with potential messiness."""
    order_id = f"ORD-{1000 + order_num}"
    
    # 5% chance of duplicate order ID
    if random.random() < 0.05 and used_order_ids:
        order_id = random.choice(list(used_order_ids))
    
    used_order_ids.add(order_id)
    
    customer_id = f"CUST-{500 + random.randint(1, 50)}"
    customer_name = random.choice(CUSTOMER_NAMES)
    
    # 3% chance of missing customer name
    if random.random() < 0.03:
        customer_name = ""
    
    restaurant = random.choice(RESTAURANTS)
    items = get_random_items(restaurant)
    
    # Decide if this record should be messy (15% chance)
    is_messy = random.random() < 0.15
    
    # Format restaurant and items with potential messiness
    formatted_restaurant = format_restaurant_name_variations(restaurant, is_messy)
    formatted_items = format_item_variations(items, is_messy)
    
    # Calculate base price
    base_price = calculate_order_total(items)
    
    # Status selection (mostly completed)
    status_weights = [0.85, 0.10, 0.05]  # completed, cancelled, refunded
    status = random.choices(STATUSES, weights=status_weights)[0]
    
    # Format status with potential messiness
    if is_messy and random.random() < 0.3:
        formatted_status = random.choice([
            status.upper(),
            f" {status}",
            f"{status} ",
            "done",  # Invalid status
            "lost",  # Invalid status
            ""  # Missing status
        ])
    else:
        formatted_status = status
    
    # Order total handling
    if status == "completed":
        # 8% chance of invalid price
        if random.random() < 0.08:
            order_total = random.choice(["free", "-10 RON", "", "N/A", f"{-base_price} RON"])
        else:
            order_total = format_price_variations(base_price, is_messy)
    else:
        # Cancelled/refunded might have missing or invalid price
        if random.random() < 0.4:
            order_total = ""
        else:
            order_total = format_price_variations(base_price, is_messy)
    
    # Delivery minutes
    if status == "completed":
        # 10% chance of invalid delivery time
        if random.random() < 0.10:
            delivery_minutes = random.choice(["-12", "0", "fast", "", "300", "not-a-number"])
        else:
            # Mostly normal (20-60), some suspicious (61-120), some very high (121-240+)
            if random.random() < 0.05:
                delivery_minutes = random.randint(121, 300)  # Suspicious/invalid
            else:
                delivery_minutes = random.randint(20, 60)
    else:
        # Cancelled/refunded might have missing delivery time
        delivery_minutes = "" if random.random() < 0.5 else random.randint(20, 60)
    
    # Rating (optional)
    if status == "completed":
        if random.random() < 0.2:  # 20% chance of missing rating
            rating = ""
        elif random.random() < 0.05:  # 5% chance of invalid rating
            rating = random.choice(["0", "6", "five", "excellent", "-1"])
        else:
            rating = str(random.randint(1, 5))
    else:
        rating = ""
    
    # Coupon code
    if random.random() < 0.3:  # 30% chance of having a coupon
        coupon_code = random.choice(COUPON_CODES)
        
        # Track coupon usage by customer
        if customer_id not in coupon_usage_by_customer:
            coupon_usage_by_customer[customer_id] = 0
        coupon_usage_by_customer[customer_id] += 1
        
        # Some customers use coupons suspiciously often
        if customer_id in coupon_usage_by_customer and coupon_usage_by_customer[customer_id] > 5:
            # Make this customer use coupons even more
            if random.random() < 0.7:
                coupon_code = random.choice(COUPON_CODES)
                coupon_usage_by_customer[customer_id] += 1
    else:
        coupon_code = ""
    
    # Format coupon with potential messiness
    if coupon_code and is_messy:
        coupon_code = random.choice([
            coupon_code.lower(),
            f" {coupon_code}",
            f"{coupon_code} "
        ])
    
    # Order date
    order_date, date_format = generate_date_variations(is_messy)
    
    return {
        "order_id": order_id,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "restaurant": formatted_restaurant,
        "items": formatted_items,
        "order_total": order_total,
        "delivery_minutes": delivery_minutes,
        "rating": rating,
        "coupon_code": coupon_code,
        "status": formatted_status,
        "order_date": order_date,
        "date_format": date_format
    }


def generate_dataset(num_records=10000, output_file="data/generated_orders.csv"):
    """Generate the complete dataset with messy and clean records."""
    used_order_ids = set()
    coupon_usage_by_customer = {}
    records = []
    
    print(f"Generating {num_records} records...")
    
    for i in range(1, num_records + 1):
        record = generate_order_record(i, used_order_ids, coupon_usage_by_customer)
        records.append(record)
        
        if i % 1000 == 0:
            print(f"Generated {i} records...")
    
    # Write to CSV
    print(f"Writing to {output_file}...")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "order_id", "customer_id", "customer_name", "restaurant", "items",
            "order_total", "delivery_minutes", "rating", "coupon_code", "status", "order_date", "date_format"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(records)
    
    print(f"Successfully generated {num_records} records to {output_file}")
    print(f"Duplicate order IDs created: {len(records) - len(used_order_ids)}")
    print(f"Customers with suspicious coupon usage: {sum(1 for c in coupon_usage_by_customer.values() if c > 5)}")


if __name__ == "__main__":
    generate_dataset(num_records=10000)
