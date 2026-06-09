def analyzer(content):
    count_all_readings=0
    count_valid_records=0
    count_invalid_records=0
    count_suspicious_records=0
    count_completed_orders=0
    count_cancelled_orders=0
    count_refunded_orders=0
    total_completed_revenue=0
    total_delivery_time=0
    
    restaurant_analysis={}
    count_items={}
    for row in content:
        count_all_readings+=1
        if row["flagged"]==False:
            count_valid_records+=1
            items_list=row["items"].split(sep="|")
            for item in items_list:
                if count_items.get(item,0):
                    count_items[item]+=1
                else:
                    count_items[item]=1
            if row["status"] == "completed":
                count_completed_orders+=1
                total_completed_revenue+=row["order_total"]
                total_delivery_time+=row["delivery_minutes"]
                if restaurant_analysis.get(row["restaurant"],0):
                    restaurant_analysis[row["restaurant"]][0]+=1
                    restaurant_analysis[row["restaurant"]][1]+=row["order_total"]
                    restaurant_analysis[row["restaurant"]][2]+=row["delivery_minutes"]
                    try:
                        int(row["rating"])
                        if len(restaurant_analysis[row["restaurant"]])==3:
                            restaurant_analysis[row["restaurant"]].append(row["rating"])
                            restaurant_analysis[row["restaurant"]].append(1)
                        else:
                            restaurant_analysis[row["restaurant"]][3]+=row["rating"]
                            restaurant_analysis[row["restaurant"]][4]+=1
                    except:
                        pass
                else:
                    try:
                        int(row["rating"])
                        restaurant_analysis[row["restaurant"]]=[1,row["order_total"],row["delivery_minutes"],row["rating"],1]
                    except:
                        restaurant_analysis[row["restaurant"]]=[1,row["order_total"],row["delivery_minutes"]]
            elif row["status"] == "cancelled":
                count_cancelled_orders+=1
            elif row["status"] == "refunded":
                count_refunded_orders+=1
        else:
            count_invalid_records+=1
        if row["suspicious"] == True:
            count_suspicious_records+=1
        
    average_completed_order_value = total_completed_revenue / count_completed_orders if count_completed_orders > 0 else 0.0

    average_delivery_minutes = total_delivery_time / count_completed_orders if count_completed_orders > 0 else 0.0

    rest_names = [k for k in restaurant_analysis.keys()]

    maximum_orders=max(rest_names, key=lambda r: restaurant_analysis[r][0])

    restaurant_with_most_amount_orders=(maximum_orders,restaurant_analysis[maximum_orders][0])

    highest_revenue_restaurant=max(rest_names,key=lambda r:restaurant_analysis[r][1])

    restaurant_with_highest_revenue=(highest_revenue_restaurant,restaurant_analysis[highest_revenue_restaurant][1])

    slowest_delivery_time=max(rest_names,key=lambda r:restaurant_analysis[r][2]/restaurant_analysis[r][0])
    slowest_delivery_time_tuple=(slowest_delivery_time,
                               restaurant_analysis[slowest_delivery_time][2]/restaurant_analysis[slowest_delivery_time][0])
    most_popular_items=[]
    for item, qty in sorted(count_items.items(), key=lambda x: x[1], reverse=True)[:3]:
        most_popular_items.append((item,qty))

    average_rating_per_restaurant=[]
    sort_on_rating=sorted(rest_names,key=lambda r: restaurant_analysis[r][3]/restaurant_analysis[r][4],reverse=True)
    for rest in sort_on_rating:
        average_rating_per_restaurant.append((rest,restaurant_analysis[rest][3]/restaurant_analysis[rest][4]))

    return {
        "all_readings": count_all_readings,
        "valid_records": count_valid_records,
        "invalid_records": count_invalid_records,
        "suspicious_records": count_suspicious_records,
        "completed_orders": count_completed_orders,
        "cancelled_orders": count_cancelled_orders,
        "refunded_orders": count_refunded_orders,
        "completed_revenue": total_completed_revenue,
        "average_order_value": average_completed_order_value,
        "average_delivery_minutes": average_delivery_minutes,
        "restaurant_most_orders": restaurant_with_most_amount_orders,
        "restaurant_highest_revenue": restaurant_with_highest_revenue,
        "most_popular_items": most_popular_items,
        "slowest_delivery_time": slowest_delivery_time_tuple,
        "average_ratings" : average_rating_per_restaurant
        
    }


