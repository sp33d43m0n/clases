class Tienda:
    def __init__(self, name = "undefined"):
        self.name = name,
        self.products = []
        
    def add_product (self, new_product): 
        self.catalog.append(new_product)
        return self
    #toma un producto y lo agrega a la tienda
    
    def __str__(self):
        return f"La tienda {self.name} tiene el catalogo {self.catalog}"
    
TiendaTexas = Tienda("Texas")


class Product:
    def __init__(self, productName, price, category):
        self.productName = productName
        self.price = price
        self.category = category
        
        
    def update_price(self, percent_change, is_increased):
    # Si is_increased es True, el precio debería aumentar en el porcentaje S
    # i es False, el precio debe disminuir en el cambio porcentual proporcionado.
        print(f"los precios de los productos eran {self.price}")
        if is_increased == "True":
            self.price *= (1+(percent_change/100))
        else:
            self.price -= (1+(percent_change/100))
        print(f"los precios de los productos son {self.price}")
        return self
         
    def print_info (self):
        print(f"Nombre del producto {self.productName}, precio {self.price}, categoria {self.category}")
        return self  
    # def print_info (self):
    # #imprime el nombre del producto, su categoría y su precio.
    #     for i in range (0, len(self.productName)):
    #         print(f"Nombre del producto {self.productName[i]}, precio {self.price[i]}, categoria {self.category[i]}")
    
producto1 = Product(productName = "pañales", price = 145000, category = "bebes")
producto2 = Product(productName = "toallitas humedas", price = 45000, category = "bebes")
producto3 = Product(productName = "baberos", price = 75000, category = "bebes")
producto4 = Product(productName = "huevos", price = 5000, category = "alimentos")
producto5 = Product(productName = "queso", price = 500, category = "alimentos")
producto6 = Product(productName = "pan", price = 9000, category = "alimentos")
producto1.update_price(20, "True")
TiendaTexas.add_product(producto1)


