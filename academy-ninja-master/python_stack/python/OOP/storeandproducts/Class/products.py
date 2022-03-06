class Product:
    def __init__(self, productName, price, category):
        self.productName = productName
        self.price = price
        self.category = category
    
    def __str__(self):
        return self.productName   
        
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
    




