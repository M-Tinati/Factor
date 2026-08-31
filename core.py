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
# print("============")
# print("Product Code :" , ProductCode)
# print("Enter Product Name :" , ProductName)
# print("Enter Product Stock :" , ProductStoke)
# print("Enter Product Price :" , ProductPrice)
# print(f"inventory : {ProductStoke} , \nAll price : {ProductStoke*ProductPrice}")
# print("============")