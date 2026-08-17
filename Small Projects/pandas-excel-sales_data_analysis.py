#Suppose you are the manager of a store and
#you have this monthly sales data.
#What you need to do:
#1) Calculate the total amount of each order
#2) Find the best-selling product: Determine which
#product has the most sales in Dollars.
#3) City sales report: Calculate the total sales for each city.
#4) Filter important customers: Find customers whose purchases are
#more than $1,000.
#5) Save to Excel


import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "Customer": ["Ali", "Sara", "Reza", "Mina", "Hassan", "Neda",
                 "Amir", "Maryam"],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Headphone",
                "Phone", "Tablet", "Laptop"],
    "Category": ["Digital", "Digital", "Digital", "Digital", "Accessory",
                 "Digital", "Digital", "Digital"],
    "Quantity": [1, 2, 1, 1, 3, 1, 2, 1],
    "Price": [1200, 800, 500, 1300, 100, 850, 550, 1250],
    "City": ["Tehran", "Shiraz", "Mashhad", "Tehran", "Tabriz",
             "Shiraz", "Tehran", "Mashhad"]
}


#1) Calculate the total amount of each order:

Quantity=data["Quantity"]
Price=data["Price"]
Total_Sales=[]
for i in range(len(Price)):
    Total_Sales.append(Quantity[i]*Price[i])
data["Total_Sales"]=Total_Sales

#or df["Total_Sales"] = df["Quantity"] * df["Price"]

df= pd.DataFrame(data)
print(df[["Order_ID","Customer","Product","Quantity","Price","City",
          "Total_Sales"]])
print("----------------------------------")




#2) Find the best-selling product: Determine which
#product has the most sales in Dollars:

product_sales =df.groupby("Product",as_index=False)["Total_Sales"].sum()
index = product_sales["Total_Sales"].idxmax()
best_product = product_sales.loc[index]
print("\nThe best-selling product is:")
print(best_product)
print("----------------------------------")



#3) City sales report: Calculate the total sales for each city:

city_sales=df.groupby("City",as_index=False)["Total_Sales"].sum()

index=city_sales["Total_Sales"].idxmax()
best_city=city_sales.loc[index]
print("\nThe best-city selling is:")
print(best_city)
print("----------------------------------")




#4) Filter important customers: Find customers whose purchases are
#more than 1,000$:

important_customers = df[df["Total_Sales"] >= 1000][
    ["Customer", "Total_Sales"]]
print("customers whose purchases are more than $1,000$ are ")
print(important_customers)




#5) Save to Excel
writer = pd.ExcelWriter('pandas-excel-sales_data_analysis.xlsx',
                        engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

best_product_df = pd.DataFrame([best_product])
best_product_df.to_excel(writer,sheet_name='Best_Product',index=False)

best_city_df = pd.DataFrame([best_city])
best_city_df.to_excel(writer,sheet_name='Best_city',index=False)

important_customers.to_excel(writer,sheet_name='Important_Customers',index=False)




writer.close()


    















