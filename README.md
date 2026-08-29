# ecommerce-data-cleaning
A data cleaning project using Python and Pandas. The dataset contains 250 e-commerce orders with inconsistent, missing, and invalid data.
Data Cleaning
The script clean_orders.py transforms the original orders_dirty.csv into orders_clean.csv.
Changes made
Dates: converts different date formats (05/12/2026, 2026-03-22, 19.06.2026) → standardized YYYY-MM-DD format.
Product names: removes extra spaces and inconsistent capitalization (sneakers, SNEAKERS, sneakers) → Sneakers.
Categories: removes extra spaces and normalizes capitalization (Accessories) → Accessories.
Payment methods: removes unnecessary spaces (Card) → Card.
Status: normalizes capitalization (completed, pending, REFUNDED) → Completed, Pending, Refunded.
Quantity: converts values to numeric → invalid values such as unknown become missing values.
Quantity: invalid negative values → missing values.
Unit price: converts comma decimal separators ("9,90") → 9.90.
Unit price: converts prices to numeric → invalid values such as N/A become missing values.
Unit price: invalid negative prices → missing values.
Discount: converts percentage values (15%, 20%, 0%) → decimal values (0.15, 0.20, 0.00).
Discount: invalid values outside the expected range → missing values.
Total: calculates the final order value using quantity, unit price, and discount → unit_price × quantity × (1 - discount).
Files
orders_dirty.csv — original dataset containing data quality problems.
clean_orders.py — Python/Pandas script used for cleaning.
orders_clean.csv — cleaned dataset produced by the script.
Tools
Python
Pandas
CSV
