product_count = 0
Inventorys = []
print("you should add 3 product information")

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



for i in Inventorys:
    print(f"========== PRODUCTS {len(i)} ==========")
    print("Product Code :" , i["code"])
    print("Enter Product Name :" , i["name"])
    print("Enter Product Stock :" , i["stock"])
    print("Enter Product Price :" , i["price"])
    print(f"product : {i['stock']} , \nAll price : ",)
    print("==============================")