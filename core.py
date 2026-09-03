ProductCode = str(input("Enter Product Code :"))
ProductName = str(input("Enter Product Name :"))
ProductStock = int(input("Enter Product Stoke :"))
ProductPrice = int(input("Enter Product Price :"))
Inventorys = []
Inventory = {
    "code" : ProductCode,
    "name" : ProductName,
    "stock" : ProductStock,
    "price" : ProductPrice,
}

Inventorys.append(Inventory)
print(Inventorys)
for i in Inventorys:
    print("========== PRODUCTS ==========")
    print("Product Code :" , i["code"])
    print("Enter Product Name :" , i["name"])
    print("Enter Product Stock :" , i["stock"])
    print("Enter Product Price :" , ProductPrice)
    print(f"i : {i["stock"]} , \nAll price : {i["stock"]*i["price"]}")
    print("==============================")