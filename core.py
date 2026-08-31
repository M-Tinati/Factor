








ProductCode = int(input("Enter Product Code :"))
ProductName = str(input("Enter Product Name :"))
ProductStoke = int(input("Enter Product Stoke :"))
ProductPrice = int(input("Enter Product Price :"))
Inventorys = []
Inventory = {
    "code" : ProductCode,
    "name" : ProductName,
    "stoke" : ProductStoke,
    "price" : ProductPrice,
}

Inventorys.append(Inventory)
print(Inventorys)
for i in Inventorys:
    print("========== PRODUCTS ==========")
    print("Product Code :" , Inventory["code"])
    print("Enter Product Name :" , Inventory["name"])
    print("Enter Product Stock :" , Inventory["stoke"])
    print("Enter Product Price :" , ProductPrice)
    print(f"inventory : {Inventory['stoke']} , \nAll price : {Inventory["stoke"]*Inventory['price']}")
    print("==============================")