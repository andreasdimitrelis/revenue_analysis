import os
import pandas as pd

products = pd.read_csv(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\raw\products.csv")
sales = pd.read_csv(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\raw\sales.csv")
raw_path = r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\raw" #path of "data/raw" file
processed_path = r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\proccesed" #path of "data/proccesed" file

if not os.path.exists(processed_path): #checks if there is a file "proccesed_path"
    os.makedirs(processed_path) #if it does not exist it creates it

#CSV reading from file "raw" and then coverting it into DataFrame
customers = pd.read_csv(os.path.join(raw_path, "customers.csv"))
products = pd.read_csv(os.path.join(raw_path, "products.csv"))
sales = pd.read_csv(os.path.join(raw_path, "sales.csv"))

#Adds the price for every sale
sales = sales.merge(products[['product_id', 'price']], on='product_id', how='left')
sales['total_value'] = sales['quantity'] * sales['price']

#Groups sales per customer
revenue_per_customer = sales.groupby('customer_id')['total_value'].sum().reset_index()

#Groups customer with city
revenue_per_customer = revenue_per_customer.merge(customers[['customer_id', 'city']], on='customer_id', how='left')


#Groups total value per city 
revenue_per_city = revenue_per_customer.groupby('city')['total_value'].sum().reset_index()

#Saves the result in file"proccesed
revenue_per_city.to_csv(os.path.join(processed_path, "revenue_per_city.csv"), index=False)

print(revenue_per_city.head())
print("Results were saved in procces file!")