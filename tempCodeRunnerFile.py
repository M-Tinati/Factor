def show_product():
    print("========== Factor ==========")
    print("Product Management System")
    print("===============================")
    
show_product()

def show_product(code , name):
    print("Product Code:", code)
    print("Product Name:" , name)
    
    
show_product("PE110X10", "Polyethylene Pipe")

def calculate_total(stock, price):
    total = stock * price 
    return total
result = calculate_total(300,50)
print(result)