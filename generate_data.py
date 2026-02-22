import pandas as pd
import numpy as np
from datetime import datetime
np.random.seed(42)
#Customers
num_customers = 1000
customers = pd.DataFrame({
    "customer_id": range(1, num_customers + 1), #gives a random unique number for every customer
    "name": [f"Customer_{i}" for i in range(1, num_customers + 1)], #gives a name for every customer for example "Customer_1", "Customer_2", ..., etc
    "city": np.random.choice(["Athens", "Thessaloniki", "Patra", "Heraklion"], num_customers), #gives a random city from the ones in '()'
    "signup_date": np.random.choice(pd.date_range(start="2022-01-01", end="2024-12-31"), num_customers) #random date between years 2022 and 2024
    })
#Products
num_products = 100
products =pd.DataFrame({
    "product_id": range(1, num_products + 1), #gives a random unique number as an id for every product
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], num_products), #gives a random category from the ones in '()
    "price": np.round(np.random.uniform(10, 500, num_products), 2) #gives a random price between 10 and 500 euros rounded in 2 decimal places
})
#Sales
num_sales = 10000
sales = pd.DataFrame({
    "sales_id": range(1, num_sales + 1), #gives a random unique number as an id for every sale
    "product_id": np.random.choice(products["product_id"], num_sales),
    "customer_id": np.random.choice(customers["customer_id"], num_sales), #gives a random choice of a customer from variable "customer_id", connects "Sales" with "Customers"
    "quantity": np.random.randint(1, 5, num_sales), #gives quantity of the product  between 1 and 4
    "sale_date": np.random.choice(pd.date_range(start="2023-01-01", end="2024-12-31"), num_sales) #gives random date between years 2023 and 2024
    })
#Saves every DataFrame as CSV file("index=False" is used to hide the index in CSV file )
customers.to_csv(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\raw\customers.csv", index=False)
products.to_csv(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\raw\products.csv", index=False)
sales.to_csv(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\raw\sales.csv", index=False)

#CSV file succesfully made
print("Data generated succesfully")