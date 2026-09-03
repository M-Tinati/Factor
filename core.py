is_Active = 0
Inventorys = []
print("you should add 3 product information")

while is_Active < 3:
    ProductCode = str(input("Enter Product Code :"))
    ProductName = str(input("Enter Product Name :"))
    ProductStock = int(input("Enter Product Stoke :"))
    ProductPrice = int(input("Enter Product Price :"))
    Inventory = {
    "code" : ProductCode,
    "name" : ProductName,
    "stock" : ProductStock,
    "price" : ProductPrice,
    }
    Inventorys.append(Inventory)
    print(Inventorys)
    is_Active += 1

for i in Inventorys:
    print("========== PRODUCTS ==========")
    print("Product Code :" , i["code"])
    print("Enter Product Name :" , i["name"])
    print("Enter Product Stock :" , i["stock"])
    print("Enter Product Price :" , i["price"])
    print(f"product : {i['stock']} , \nAll price : {i['stock'] * i['price']}")
    print("==============================")