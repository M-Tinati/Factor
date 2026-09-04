product_count = 0
Inventorys = []
print("you should add 3 product information")
def check_stock(stock):
    if stock > 0:
        return "Available"
    elif stock == 0:
        return "Out of Stock"
    else:
        return "Invalid"
def input_user(code , name , stock , price):
    Inventory = {
        "code" : code,
        "name" : name,
        "stock" : stock,
        "price" : price,
        }
    Inventorys.append(Inventory)
while product_count < 3:
    ProductCode = input("Enter Product Code :")
    ProductName = input("Enter Product Name :")
    ProductStock = int(input("Enter Product Stock :"))
    ProductPrice = int(input("Enter Product Price :"))
    input_user(ProductCode,ProductName,ProductStock,ProductPrice)
    print(Inventorys)
    product_count += 1


def calculate_total(stock, price):
    total = stock * price 
    return total

for index , i in enumerate(Inventorys , start=1):
    result = calculate_total(i["stock"] , i["price"])
    stock_status = check_stock(i["stock"])
    print(f"========== PRODUCTS ==========")
    print(f"{index}.Product Code :" , i["code"])
    print("Enter Product Name :" , i["name"])
    print("Stock Status :", stock_status)
    print("Enter Product Price :" , i["price"])
    print(f"product : {i['stock']} , \nAll price : {result}",)
    print("==============================")
    
def search_product(name):
    for product in Inventorys:
        if product["name"] == name:
            return product
        
        
search = input("Search by name: ")
result = search_product(search)
print(result)


def search_code(code):
    for product in Inventorys:
        if product["code"] == code:
            return product
    
    return "Product Not Found"
        
        
search = input("Search by code: ")
result = search_code(search)
print(result)