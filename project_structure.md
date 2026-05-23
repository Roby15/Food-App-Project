# 🍔 Order Chaos Kitchen — Food Delivery Data Rescue Mission

## 📁 Project Structure

```
food_delivery_rescue/
│
├── data/
│   ├── sample_orders.csv          ← Small hand-crafted sample (20–30 rows, for manual testing)
│   └── generated_orders.csv       ← Auto-generated 10,000+ record dataset (created by data_generator.py)
│
├── reports/
│   └── order_quality_report.txt   ← Final output report written by reporter.py
│
├── src/
│   ├── main.py                    ← Entry point; orchestrates all modules in order
│   ├── data_generator.py          ← Generates the 10,000+ mock CSV dataset
│   ├── reader.py                  ← Reads CSV safely using csv.DictReader
│   ├── validator.py               ← Validates each field against business rules
│   ├── cleaner.py                 ← Normalizes/fixes formatting issues
│   ├── analyzer.py                ← Computes revenue, averages, popular items, etc.
│   ├── anomaly_detector.py        ← Flags suspicious records and patterns
│   └── reporter.py                ← Formats and writes the human-readable report
│
├── tests/
│   ├── test_validator.py          ← Tests for validation rules (required fields, formats)
│   ├── test_cleaner.py            ← Tests for cleaning logic (price parsing, name normalization)
│   ├── test_analyzer.py           ← Tests for revenue totals, averages, item counts
│   └── test_anomaly_detector.py   ← Tests for duplicate IDs, coupon abuse, bad delivery times
│
└── README.md                      ← Setup instructions, how to run, project overview
```

---

## 📄 File Responsibilities

| File | Owned By | What It Does |
|---|---|---|
| `main.py` | Logic Builder | Calls reader → validator → cleaner → analyzer → anomaly_detector → reporter |
| `data_generator.py` | Data Guardian | Programmatically generates 10k+ rows with controlled mess |
| `reader.py` | Logic Builder | Opens CSV, returns list of raw row dicts |
| `validator.py` | Data Guardian | Returns `valid`, `invalid`, or `suspicious` classification per record |
| `cleaner.py` | Logic Builder | Returns cleaned version of a record (no meaning changes) |
| `analyzer.py` | Logic Builder | Pure calculation functions over cleaned records |
| `anomaly_detector.py` | Data Guardian | Detects duplicates, coupon abuse, high totals, slow delivery |
| `reporter.py` | Insight Storyteller | Formats the final report for the Operations Analyst |

---

## 🗂️ Mock Data — `sample_orders.csv`

A small hand-written file covering all the important edge cases.

### CSV Header

```
order_id,customer_id,customer_name,restaurant,items,order_total,delivery_minutes,rating,coupon_code,status,order_date
```

### Edge Case Rows

| Row Purpose | Example Record |
|---|---|
| ✅ Clean completed order | `ORD-1001,CUST-501,Ana Popescu,Burger Planet,Cheeseburger\|Fries\|Cola,58.50 RON,32,5,WELCOME10,completed,2026-04-12` |
| 🧹 Fixable mess (spaces, casing, date format) | `ORD-1002,CUST-502, Mihai Ionescu ,burger planet,Chicken Burger\|fries ,44.00 ron,41,4,,completed,2026/04/12` |
| ❌ Invalid price + negative delivery + bad rating | `ORD-1003,CUST-503,Ioana Marin,Sushi House,Salmon Roll\|Miso Soup,free,-12,6,SUPERFREE,completed,2026-04-13` |
| ⚠️ Cancelled with missing optional fields | `ORD-1004,CUST-504,,Pizza Palace,Margherita Pizza\|Garlic Dip,39.90 RON,,,, cancelled,2026-04-14` |
| 🔁 Duplicate order ID | `ORD-1001,CUST-505,Vlad Dima,Burger Planet,Double Burger,62.00 RON,29,5,WELCOME10,completed,2026-04-15` |
| 💸 Refunded order | `ORD-1005,CUST-506,Elena Stan,Pizza Palace,Pepperoni Pizza,47.00 RON,55,3,,refunded,2026-04-14` |
| 🕵️ Coupon abuser (same customer, 7 rows) | `ORD-1006..1012,CUST-507,...,...,...,SAVE20,completed,...` ×7 rows |
| 💰 Suspiciously high total | `ORD-1013,CUST-508,...,...,...,890.00 RON,45,5,,completed,2026-04-15` |
| ⏱️ Very slow delivery (suspicious) | `ORD-1014,CUST-509,...,...,...,55.00 RON,145,2,,completed,2026-04-16` |
| 📅 Unparseable date | `ORD-1015,CUST-510,...,...,...,33.00 RON,30,4,,completed,not-a-date` |
| 📅 Future date | `ORD-1016,CUST-511,...,...,...,40.00 RON,28,5,,completed,2029-01-01` |
| ❓ Unknown status | `ORD-1017,CUST-512,...,...,...,38.00 RON,35,3,,lost,2026-04-16` |
| 🔡 Restaurant name variants | rows with `burger planet`, `BURGER PLANET`, ` Burger Planet ` |
| 💲 Price format variants | `RON 58.50`, `58.50 ron`, ` 58.50 `, `-10 RON`, ` ` |

---

## 🏭 Generated Data — `generated_orders.csv`

Produced by `data_generator.py`. Must contain **10,000+ rows** with this controlled distribution:

| Category | Approx % | Notes |
|---|---|---|
| Clean completed orders | ~65% | Normal happy-path records |
| Cancelled orders | ~15% | May have missing total/delivery |
| Refunded orders | ~5% | Small subset |
| Messy-but-fixable records | ~8% | Spacing, casing, date format issues |
| Invalid records | ~4% | Free price, negative delivery, bad date |
| Suspicious records | ~3% | Coupon abuse, high totals, slow delivery |

### Generator Internal Pools

| Pool | Values |
|---|---|
| **Restaurants** | `Burger Planet`, `Sushi House`, `Pizza Palace`, `Taco Town`, `Pasta Prima` + casing variants |
| **Items (Burger Planet)** | `Cheeseburger`, `Fries`, `Cola`, `Double Burger`, `Milkshake` |
| **Items (Sushi House)** | `Salmon Roll`, `Miso Soup`, `Tuna Nigiri`, `Edamame`, `Green Tea` |
| **Items (Pizza Palace)** | `Margherita Pizza`, `Pepperoni Pizza`, `Garlic Dip`, `Tiramisu`, `Sparkling Water` |
| **Items (Taco Town)** | `Beef Taco`, `Chicken Burrito`, `Nachos`, `Guacamole`, `Horchata` |
| **Items (Pasta Prima)** | `Spaghetti Bolognese`, `Penne Arrabbiata`, `Bruschetta`, `Cannoli`, `Espresso` |
| **Customer IDs** | `CUST-501` through `CUST-700` (200 customers) |
| **Order IDs** | `ORD-1001` through `ORD-11000+` with ~150 intentional duplicates |
| **Coupon Codes** | `WELCOME10`, `SAVE20`, `FREESHIP`, `LOYALTY5`, `SUMMER15` + empty for most rows |
| **Coupon Abusers** | ~10 customer IDs using a coupon in >70% of their orders |
| **Dates** | Random dates in `2026-01-01` to `2026-04-30`, plus a few in wrong format or future |

### Intentional Mess Injected by Generator

- Price as `"free"`, `"-10 RON"`, `"RON 58.50"`, `"58.50 ron"`, `" 58.50 "`
- Delivery time as `"-5"`, `"0"`, `"245"`, `"fast"`, or empty
- Rating as `"0"`, `"6"`, `"five"`, `"excellent"`, or empty
- Date as `"12-04-2026"`, `"2026/04/12"`, `"not-a-date"`, or a 2029 future date
- Status as `"done"`, `"lost"`, `"maybe"`, or empty
- Restaurant names with extra spaces or all-caps/all-lowercase

---

## 📊 Report Output — `order_quality_report.txt`

```
Food Delivery Order Quality Report
===================================

1. Dataset Summary
------------------
Total records read:          10,250
Valid cleaned records:        9,612
Invalid records:                421
Suspicious records:             217
Records requiring cleaning:   2,384

2. Order Status Summary
------------------------
Completed orders:   8,950
Cancelled orders:     982
Refunded orders:      101

3. Revenue Summary
-------------------
Completed-order revenue:       487,230.50 RON
Average completed order value:      54.44 RON
Highest revenue restaurant:    Burger Planet

4. Delivery Summary
--------------------
Average delivery time:         38.6 minutes
Slowest average restaurant:    Sushi House
Orders above 120 minutes:      47

5. Popular Items
-----------------
1. Fries             — 2,104 orders
2. Cheeseburger      — 1,843 orders
3. Cola              — 1,420 orders
4. Salmon Roll       — 1,310 orders
5. Margherita Pizza  — 1,198 orders

6. Restaurant Breakdown
------------------------
[Per restaurant: revenue, avg delivery, avg rating, cancellation rate]

7. Coupon Analysis
-------------------
Total coupon orders:           1,834
Revenue with coupons:        89,200.00 RON
Revenue without coupons:    398,030.50 RON
Suspicious coupon customers:   12

8. Anomalies Found
-------------------
Duplicate order IDs:       18
Invalid prices:            53
Suspicious coupon usage:   12
Invalid delivery times:    31
High-value orders:          9
Invalid ratings:           27
Suspicious restaurants:     3

9. Recommended Follow-Up
-------------------------
- Review customers with unusually frequent coupon usage.
- Check restaurants with high cancellation rates.
- Investigate records with invalid prices before using in finance reports.
- Audit high-value orders above 300 RON.
- Re-examine orders with delivery times above 120 minutes.
```

---

## 🧪 Test Coverage — `tests/`

| Test File | What It Proves |
|---|---|
| `test_validator.py` | Clean order passes; missing required field fails; unknown status fails; future date flagged |
| `test_cleaner.py` | `"58.50 RON"` → `58.50`; `"burger planet"` → `"Burger Planet"`; `"SAVE20 "` → `"SAVE20"` |
| `test_analyzer.py` | Revenue total correct on 5-row sample; average delivery time correct; popular items ranked correctly |
| `test_anomaly_detector.py` | Duplicate IDs detected; coupon abuse flagged at threshold; delivery > 120 flagged; total > 300 flagged |

---

## 👥 Team Role Map

| Module / File | Data Guardian | Logic Builder | Insight Storyteller |
|---|:---:|:---:|:---:|
| `data_generator.py` | ✅ Lead | 👀 Review | — |
| `reader.py` | — | ✅ Lead | — |
| `validator.py` | ✅ Lead | 👀 Review | — |
| `cleaner.py` | 👀 Review | ✅ Lead | — |
| `analyzer.py` | — | ✅ Lead | 👀 Review |
| `anomaly_detector.py` | ✅ Lead | 👀 Review | — |
| `reporter.py` | — | 👀 Review | ✅ Lead |
| `main.py` | 👀 Review | ✅ Lead | 👀 Review |
| `tests/` | ✅ Cases | ✅ Code | — |
| `README.md` | — | — | ✅ Lead |

> ✅ Lead = primary owner · 👀 Review = must understand and can contribute
