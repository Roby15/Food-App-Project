## Challenge Title

**Order Chaos Kitchen: The Food Delivery Data Rescue Mission**

## Engineering Ticket

The Food Delivery Operations team has a problem: their weekly order report is giving suspicious, inconsistent, and sometimes completely ridiculous results.

Revenue looks too high. Some delivery times are negative. A few customers appear to be using coupons like they discovered a secret portal. Restaurant names are spelled five different ways. One order claims the price was `"free"`, which sounds generous but makes the finance team nervous.

The team receives food delivery order data from several systems: the mobile app, restaurant tablets, payment logs, and customer support exports. Unfortunately, those systems do not always agree on formatting.

Your end user is an **Operations Analyst** who needs a reliable tool that can clean messy order data, separate trustworthy records from problematic ones, and produce useful business insights.

They do not need a perfect enterprise dashboard. They need a Python program that helps them answer:

* Which restaurants are performing well?  
* Which orders should be reviewed?  
* Are coupons being abused?  
* What items are popular?  
* Where is delivery performance getting weird?

Your job is to turn messy delivery data into decisions. Because software is most valuable when it helps real people make better calls, not when it simply says “script completed successfully.”

## Your Mission

Build a Python 3.13 program that reads messy food delivery order data from a file, validates it, cleans what can safely be cleaned, detects suspicious records, analyzes business patterns, and generates a readable report for the Operations Analyst.

Your team must also create a mock data generator that produces a realistic dataset with **at least 10,000 records**, including both normal records and intentionally messy edge cases.

You may only use **Python builtins and the standard library**. No Pandas. No NumPy. No requests. No third-party packages. The kitchen is stocked with Python 3.13 only.

## End User

The primary end user is an **Operations Analyst at a food delivery company**.

They need to make decisions such as:

* Which restaurants generate the most completed-order revenue?  
* Which restaurants have unusually slow deliveries?  
* Which customers may be abusing coupon codes?  
* Which orders should be excluded from business reporting?  
* Which menu items are most popular?  
* Whether operational problems are isolated or part of a pattern.

This tool helps the analyst spend less time manually cleaning spreadsheets and more time understanding what is actually happening in the business.

In other words: fewer spreadsheet headaches, more useful insight.

## Team Roles

### Data Guardian

Owns the data quality side of the project.

Responsibilities:

* Defines what a valid food delivery order looks like.  
* Designs realistic messy records for the mock dataset.  
* Creates edge cases such as missing prices, invalid dates, duplicate order IDs, strange statuses, and suspicious coupon usage.  
* Helps decide which records should be cleaned, rejected, or flagged for review.  
* Makes sure test data is realistic, not just random chaos soup.

### Logic Builder

Owns the core Python implementation.

Responsibilities:

* Builds functions for reading files, parsing records, validating fields, cleaning values, and structuring cleaned orders.  
* Implements analysis logic such as revenue totals, average delivery time, popular items, and coupon usage counts.  
* Implements anomaly detection rules.  
* Keeps the code organized into small, understandable functions.  
* Makes sure bad data does not crash the program.

### Insight Storyteller

Owns the final user experience.

Responsibilities:

* Designs the report format.  
* Makes sure the output is useful to a non-technical Operations Analyst.  
* Explains what the data issues mean in plain language.  
* Connects technical findings to business value.  
* Leads the final presentation flow and demo.

These are collaboration roles, not silos. Everyone should review the code, understand the logic, participate in testing, and be able to explain the full solution. No “I only did the README” escape hatch.

## Dataset

Use a **CSV file** for this challenge.

Why CSV?

* It is beginner-friendly.  
* It is easy to inspect manually.  
* It works well with Python’s built-in `csv` module.  
* It resembles real exports from business systems.

Each record represents one food delivery order.

Suggested fields:

```
order_id,customer_id,customer_name,restaurant,items,order_total,delivery_minutes,rating,coupon_code,status,order_date
```

The `items` field can contain multiple items separated by `|`.

Example records:

```
order_id,customer_id,customer_name,restaurant,items,order_total,delivery_minutes,rating,coupon_code,status,order_date
ORD-1001,CUST-501,Ana Popescu,Burger Planet,Cheeseburger|Fries|Cola,58.50 RON,32,5,WELCOME10,completed,2026-04-12
 ORD-1002 ,CUST-502, Mihai Ionescu ,burger planet,Chicken Burger| fries , 44.00 ron , 41 ,4,, Completed ,2026/04/12
ORD-1003,CUST-503,Ioana Marin,Sushi House,Salmon Roll|Miso Soup,free,-12,6,SUPERFREE,completed,2026-04-13
ORD-1004,CUST-504,,Pizza Palace,Margherita Pizza|Garlic Dip,39.90 RON,,,"",cancelled,2026-04-14
ORD-1001,CUST-505,Vlad Dima,Burger Planet,Double Burger,62.00 RON,29,5,WELCOME10,completed,2026-04-15
```

What these examples show:

* `ORD-1001` is a clean valid completed order.  
* `ORD-1002` is messy but fixable: extra spaces, inconsistent casing, different date separator, lowercase currency.  
* `ORD-1003` is invalid or suspicious: price is `"free"`, delivery time is negative, rating is outside the allowed range, and coupon usage looks strange.  
* `ORD-1004` is cancelled, has missing optional/conditional fields, and should be handled differently from completed orders.  
* The final `ORD-1001` is a duplicate order ID and should be flagged.

Your team must generate a mock dataset file with **at least 10,000 records**.

## Mock Data Generator Requirements

Create a Python script that generates your dataset using Python builtins only.

The generator should create a file such as:

```
data/generated_orders.csv
```

Your generated dataset must include realistic normal records and intentional messy records.

Include examples of:

* Clean completed orders.  
* Cancelled orders.  
* Refunded orders.  
* Duplicate order IDs.  
* Missing customer names.  
* Missing ratings.  
* Missing coupon codes.  
* Prices formatted in different ways, such as `"58.50 RON"`, `"58.50 ron"`, `" 58.50 "`, `"RON 58.50"`.  
* Invalid price values, such as `"free"`, `"-10 RON"`, or empty strings.  
* Delivery times that are missing, negative, zero, very high, or not numbers.  
* Ratings from 1 to 5, plus invalid ratings like `0`, `6`, `"five"`, or empty values.  
* Restaurant names with inconsistent formatting, such as `"Burger Planet"`, `"burger planet"`, `" Burger Planet "`, and `"BURGER PLANET"`.  
* Item names with inconsistent spacing or casing.  
* Suspiciously frequent coupon usage by the same customer.  
* Unusual order totals, such as very high completed orders.  
* Invalid or inconsistent dates, such as `"2026-04-12"`, `"2026/04/12"`, `"12-04-2026"`, `"not-a-date"`.

Do not manually write 10,000 rows. Your generator should create them programmatically.

Your generator should not create pure nonsense. Realistic data with a controlled amount of mess is more useful than digital confetti.

## Functional Requirements

Your program must:

1. Read food delivery order records from a CSV file.  
     
2. Validate each record using clear business rules.  
     
3. Clean or normalize fields where it is safe to do so.  
     
4. Separate records into at least three groups:  
     
   * valid cleaned records  
   * invalid records  
   * suspicious records that may still be usable but need review

   

5. Store cleaned data using Python structures such as lists, dictionaries, sets, and tuples.  
     
6. Detect duplicate order IDs.  
     
7. Parse and normalize order totals.  
     
8. Parse and normalize delivery times.  
     
9. Normalize restaurant names and statuses.  
     
10. Normalize item lists.  
      
11. Handle cancelled and refunded orders correctly.  
      
12. Analyze completed orders.  
      
13. Detect anomalies and interesting patterns.  
      
14. Produce a readable report for the end user.  
      
15. Avoid hard-coding final results.  
      
16. Handle bad data gracefully instead of crashing.  
      
17. Organize the solution into small functions instead of one giant script.

## Validation Rules

Define and implement validation rules for each order.

Suggested rules:

### Required Fields

The following fields are required for all records:

* `order_id`  
* `customer_id`  
* `restaurant`  
* `items`  
* `status`  
* `order_date`

The following fields are required for completed orders:

* `order_total`  
* `delivery_minutes`

### Order ID

Valid order IDs should:

* Not be empty.  
* Follow a pattern such as `ORD-1234`.  
* Be unique in the dataset.

Duplicate order IDs should be flagged.

### Customer ID

Valid customer IDs should:

* Not be empty.  
* Follow a pattern such as `CUST-501`.

### Status

Accepted statuses:

* `completed`  
* `cancelled`  
* `refunded`

Status should be normalized to lowercase.

Unknown statuses such as `"done"`, `"lost"`, `"maybe"`, or empty values should be invalid.

### Order Total

For completed orders:

* Must be present.  
* Must be convertible to a positive number.  
* Should support common messy formats like `"58.50 RON"`, `"ron 58.50"`, and `" 58.50 "`.  
* Must not be negative.  
* Must not be `"free"`.

For cancelled orders:

* Missing order total may be allowed.  
* If present, it should still be validated.

### Delivery Minutes

For completed orders:

* Must be present.  
* Must be a number.  
* Must be greater than 0\.  
* Values above 120 minutes should be considered suspicious.  
* Values above 240 minutes should be considered invalid unless your team chooses a different rule and explains it.

### Rating

Ratings are optional, but if present:

* Must be a number.  
* Must be between 1 and 5\.

Invalid values such as `0`, `6`, `"five"`, or `"excellent"` should be reported.

### Coupon Code

Coupon codes are optional.

If present, they should:

* Be trimmed.  
* Be normalized to uppercase.  
* Contain only reasonable characters such as letters, numbers, and hyphens.

Very frequent use of coupons by the same customer should be flagged as suspicious.

### Order Date

Order dates should be parsed using Python builtins such as `datetime`.

Accepted formats may include:

* `YYYY-MM-DD`  
* `YYYY/MM/DD`

Dates that cannot be parsed should be invalid.

Future dates should be suspicious or invalid depending on your team’s rule.

## Cleaning Rules

Clean and normalize values where it is safe and reasonable.

Examples of safe cleaning:

* Trim extra spaces from all string fields.  
* Normalize status values to lowercase.  
* Normalize coupon codes to uppercase.  
* Normalize restaurant names to title case.  
* Convert `"burger planet"`, `" Burger Planet "`, and `"BURGER PLANET"` into `"Burger Planet"`.  
* Convert price strings like `"58.50 RON"` or `"ron 58.50"` into a numeric value such as `58.50`.  
* Convert delivery minutes from strings into integers.  
* Convert rating strings like `"5"` into integer `5`.  
* Split items on `|`.  
* Trim each item name.  
* Normalize item names to title case.  
* Parse accepted date formats into a consistent `YYYY-MM-DD` format.

Do **not** silently fix values that could change business meaning.

Do not silently fix:

* Negative prices.  
* `"free"` prices.  
* Negative delivery times.  
* Duplicate order IDs.  
* Invalid statuses.  
* Invalid dates.  
* Ratings outside 1 to 5\.  
* Missing required fields.  
* Suspiciously high delivery times.  
* Suspiciously high order totals.

Those should be reported as invalid or suspicious.

A good rule of thumb: clean formatting problems, but report meaning problems.

## Analysis Tasks

Your program should produce useful insights from the cleaned data.

Beginner-friendly analysis tasks:

* Count total records read.  
* Count valid records.  
* Count invalid records.  
* Count suspicious records.  
* Count completed, cancelled, and refunded orders.  
* Calculate total completed-order revenue.  
* Calculate average completed-order value.  
* Calculate average delivery time for completed orders.  
* Find the restaurant with the highest completed-order revenue.  
* Find the restaurant with the most completed orders.  
* Find the most popular items.

Slightly more advanced analysis tasks:

* Calculate average rating by restaurant.  
* Find restaurants with high cancellation or refund rates.  
* Find customers with unusually frequent coupon usage.  
* Compare revenue with and without coupon orders.  
* Find days with unusually high order volume.  
* Identify the top 5 customers by completed-order count.  
* Identify restaurants with slow average delivery times.  
* Track how many records required cleaning.

## Anomaly Detection

Your program must detect suspicious patterns.

Implement at least **five** anomaly rules.

Suggested anomaly rules:

1. **Duplicate Order ID**  
     
   * Same `order_id` appears more than once.

   

2. **Suspicious Delivery Time**  
     
   * Completed order has delivery time above 120 minutes.

   

3. **Impossible Delivery Time**  
     
   * Completed order has delivery time less than or equal to 0\.

   

4. **Suspicious Coupon Usage**  
     
   * Same customer uses coupons more than a chosen threshold, such as 5 times in the dataset or more than 70% of their completed orders.

   

5. **Unusually High Order Total**  
     
   * Completed order total is above a chosen threshold, such as `300 RON`.

   

6. **Invalid Rating**  
     
   * Rating exists but is outside the range 1 to 5\.

   

7. **Suspicious Restaurant Pattern**  
     
   * A restaurant has a cancellation rate above a chosen threshold, such as 40%.

   

8. **Odd Date Pattern**  
     
   * Order date is in the future or cannot be parsed.

Keep your rules explainable. The Operations Analyst should understand why an order was flagged.

Avoid mysterious “AI magic score says suspicious.” This is Python Essentials, not a black-box dragon.

## Report Output

Your program should print a readable report to the terminal and/or write it to a text file such as:

```
reports/order_quality_report.txt
```

The exact format is up to your team, but it should be understandable to a non-technical user.

Example structure:

```
Food Delivery Order Quality Report
==================================

Dataset Summary
---------------
Total records read: 10,250
Valid cleaned records: 9,612
Invalid records: 421
Suspicious records: 217
Records requiring cleaning: 2,384

Order Status Summary
--------------------
Completed orders: 8,950
Cancelled orders: 982
Refunded orders: 101

Revenue Summary
---------------
Completed-order revenue: 487,230.50 RON
Average completed order value: 54.44 RON
Highest revenue restaurant: Burger Planet

Delivery Summary
----------------
Average delivery time: 38.6 minutes
Slowest average restaurant: Sushi House
Orders above 120 minutes: 47

Popular Items
-------------
1. Fries: 2,104 orders
2. Cheeseburger: 1,843 orders
3. Cola: 1,420 orders

Anomalies Found
---------------
Duplicate order IDs: 18
Invalid prices: 53
Suspicious coupon customers: 12
Invalid delivery times: 31
High-value orders: 9

Recommended Follow-Up
---------------------
- Review customers with unusually frequent coupon usage.
- Check restaurants with high cancellation rates.
- Investigate records with invalid prices before using them in finance reports.
```

Your report should not just dump raw data. It should summarize what matters.

## Unit Testing Requirements

Unit tests are mandatory.

Use Python’s built-in `unittest` module.

Your tests should focus on business logic, not just whether files exist. Unit tests are not only for grades. They are a way to track edge cases, prevent regressions, and build confidence when your data gets weird.

Test ideas:

1. A clean completed order passes validation.  
2. A price like `"58.50 RON"` is cleaned into `58.50`.  
3. A price like `"free"` is rejected.  
4. A completed order with missing delivery time is invalid.  
5. Restaurant names like `" burger planet "` and `"BURGER PLANET"` normalize to the same value.  
6. Duplicate order IDs are detected.  
7. A rating of `6` is rejected or flagged.  
8. A customer using coupons too many times is detected as suspicious.

You should also test summary calculations, such as total revenue and average delivery time, using a small controlled dataset.

Good tests are tiny safety helmets for your code. Wear them.

## Suggested Project Structure

```
project/
  data/
    sample_orders.csv
    generated_orders.csv
  reports/
    order_quality_report.txt
  src/
    main.py
    data_generator.py
    reader.py
    validator.py
    cleaner.py
    analyzer.py
    anomaly_detector.py
    reporter.py
  tests/
    test_validator.py
    test_cleaner.py
    test_analyzer.py
    test_anomaly_detector.py
  README.md
```

Suggested responsibilities:

* `data_generator.py`: creates the 10,000+ record mock dataset.  
* `reader.py`: reads CSV records safely.  
* `validator.py`: checks whether records follow the rules.  
* `cleaner.py`: normalizes fixable messy values.  
* `analyzer.py`: calculates summaries and insights.  
* `anomaly_detector.py`: detects suspicious patterns.  
* `reporter.py`: formats the final report.  
* `main.py`: connects everything together.

## How to Use AI Like a Modern Engineer

You are encouraged to use tools like ChatGPT, Cursor, Windsurf, or VS Code Copilot.

But AI should help you think, not replace your thinking.

Use AI as a pair programmer, not as a homework machine.

Helpful ways to use AI:

* Ask AI to explain concepts you do not understand.  
* Ask AI to review your code for bugs or readability.  
* Ask AI to generate edge case ideas.  
* Ask AI to help write unit test scenarios.  
* Ask AI to compare two possible data structures.  
* Ask AI to explain an error message.  
* Ask AI to suggest how to break a big function into smaller functions.

Important rules:

* Do not blindly paste AI-generated code.  
* You must be able to explain every function in your project.  
* You are responsible for checking whether AI suggestions are correct.  
* AI can suggest tests, but your team must understand what each test proves.  
* AI can help with debugging, but you should still read the error message yourself.  
* AI is great at confidence. It is not always great at correctness. Politely fact-check the robot.

Example prompts you can ask an AI assistant:

1. “Here is my validation function. Can you review it for edge cases I missed?”  
2. “Can you explain how Python’s built-in `csv.DictReader` works with missing columns?”  
3. “What are good unit test cases for cleaning messy price strings?”  
4. “I have a list of cleaned orders as dictionaries. What is a beginner-friendly way to calculate revenue by restaurant?”  
5. “Can you help me compare using a list of dictionaries versus a dictionary keyed by order ID?”  
6. “Here is my error message. Explain what it means and suggest where I should look first.”  
7. “Can you suggest anomaly detection rules for food delivery orders that are easy to implement with Python builtins?”  
8. “Can you help me refactor this long function into smaller functions without changing the behavior?”

## Final Presentation

At the end, your team must present the project.

Your presentation should include:

1. The actual challenge you solved.  
2. Who the end user is.  
3. What problem the end user has.  
4. Why this problem matters.  
5. A short demo of your program.  
6. What data issues you found.  
7. What technical challenges you had during implementation.  
8. How you tested the business logic.  
9. What insights or anomalies your solution discovered.  
10. An estimate of how much value the solution could bring to the end user.

Think empathetically.

Do not only say:

“Our script works.”

Explain why it matters:

“Our tool helps an Operations Analyst avoid using broken order data in revenue reports, quickly identify suspicious coupon patterns, and find restaurants that may need operational support.”

Your final demo should show the journey from messy records to useful decisions.

The best projects will feel like small professional tools, not just Python exercises wearing a fake mustache.  
