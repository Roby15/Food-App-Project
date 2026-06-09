import os
from InvalidOrder import InvalidOrder
from Analyzer import analyzer

def generate_report(content):
   

    
    duplicate_order_ids = InvalidOrder.count_duplicate_order_ids
    suspicious_coupon_customers = InvalidOrder.count_suspicious_cupons
    invalid_delivery_times = InvalidOrder.count_imposible_delivery_times + InvalidOrder.count_bad_delivery_times
    orders_above_120 = InvalidOrder.count_suspicious_delivery_times
    invalid_prices = InvalidOrder.count_bad_order_totals
    suspicious_delivery_time = InvalidOrder.count_suspicious_delivery_times
    suspicious_rating = InvalidOrder.count_suspicious_ratings
    
    report_str = f"""Food Delivery Order Quality Report
==================================

Dataset Summary
---------------
Total records read: {content['all_readings']:,}
Valid cleaned records: {content['valid_records']:,}
Invalid records: {content['invalid_records']:,}
Suspicious records: {content['suspicious_records']:,}
Records requiring cleaning: {content['valid_records']:,}

Order Status Summary
--------------------
Completed orders: {content['completed_orders']:,}
Cancelled orders: {content['cancelled_orders']:,}
Refunded orders: {content['refunded_orders']:,}

Revenue Summary
---------------
Completed-order revenue: {content['completed_revenue']:,.2f} RON
Average completed order value: {content['average_order_value']:,.2f} RON
Highest revenue restaurant: {content['restaurant_highest_revenue'][0] if content['restaurant_highest_revenue'] else 'N/A'} {content['restaurant_highest_revenue'][1]:,.2f} RON

Delivery Summary
----------------
Average delivery time: {content['average_delivery_minutes']:.1f} minutes
Slowest average restaurant: {content['slowest_delivery_time'][0]} {content['slowest_delivery_time'][1]:,.2f} minutes
Orders above 120 minutes: {orders_above_120}

Average Ratings
---------------
{"\n".join(f"• {rest}: {rating:.2f} stars" for rest, rating in content["average_ratings"])}


Popular Items
-------------
1. {content["most_popular_items"][0][0]}: {content["most_popular_items"][0][1]:,} orders
2. {content["most_popular_items"][1][0]}: {content["most_popular_items"][1][1]:,} orders
3. {content["most_popular_items"][2][0]}: {content["most_popular_items"][2][1]:,} orders

Anomalies Found
---------------
Duplicate order IDs: {duplicate_order_ids}
Invalid prices: {invalid_prices}
Suspicious coupon customers: {suspicious_coupon_customers}
Invalid delivery times: {invalid_delivery_times}
Suspicious delivery time: {suspicious_delivery_time}
Suspicious ratings: {suspicious_rating}

"""

    # Print to console
    print(report_str)

    # Write to file
    os.makedirs("reports", exist_ok=True)
    with open("reports/order_quality_report.txt", "w", encoding="utf-8") as f:
        f.write(report_str)
