class Tienda:
    def __init__(self, name, products = [], stock = []):
        self.name = name,
        self.products = products
        self.stock = stock
    
    def __str__(self):
        return self.name
            
    #toma un producto y lo agrega a la tienda
    def add_product(self, new_product): 
        self.products.append(new_product)
        self.stock.append(0)
        return self
    
    def load_inventory(self, products, quantity):
        pos = self.products.index(products)
        self.stock[pos] += quantity
        return self
    
    def show_products(self):
        print(self.products)
        return self
    
    def show_inventory(self, products):
        pos = self.products.index(products)
        print(f"el producto {self.products[pos]}, tiene en inventario {self.stock[pos]}")
    
    def sell_product(self, products, quantity):
        pos = self.products.index(products)
        self.stock[pos] -= quantity
        return self
    
        
        
         
        
        
        

