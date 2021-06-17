class Store:

    def __init__(self, name, productList = []):
        self.name = name
        self.productList = []
        for producto in productList:
            self.productList.append(Product(producto, 0, "Primeras Adiciones"))

    def add_product(self, new_product, price, category):
        self.productList.append(Product(new_product, price, category))
        print(f"Usted acaba de agregar al producto {new_product}")
        return self

    def sell_product(self, id):
        print(f"Usted a vendido el producto llamado {self.productList[id].name}")
        self.productList.pop(id)
        return self

    def inflation(self, percent_increase):
        print(f"El precio de todos los productos aumentara un {percent_increase}%")
        for i in self.productList:
            self.productList[i].price * (1+percent_increase/100)
        return self

class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            print(f"El producto {self.name} aumentara un {percent_change}%")
            self.price = (1+percent_change/100) * self.price
            print(f"El nuevo precio es {self.price}")
        else:
            print(f"El producto {self.name} bajara un {percent_change}%")
            self.price = (1-percent_change/100) * self.price
            print(f"El nuevo precio es {self.price}")
        return self

    def print_info(self):
        print(f"El producto {self.name} posee un valor de {self.price} y pertenece a la categoria {self.category}")
        return self

productos = ["pan", "arroz", "margarina"]
store = Store("Alegria", productos)

store.add_product("queso", 100, "alimento").sell_product(0)