from Class import Product
from Class import Tienda

producto1 = Product(productName = "panales", price = 145000, category = "bebes")
producto2 = Product(productName = "toallitas humedas", price = 45000, category = "bebes")
producto3 = Product(productName = "baberos", price = 75000, category = "bebes")
producto4 = Product(productName = "huevos", price = 5000, category = "alimentos")
producto5 = Product(productName = "queso", price = 500, category = "alimentos")
producto6 = Product(productName = "pan", price = 9000, category = "alimentos")
# producto1.update_price(20, "True")

TexasStore = Tienda("Texas")
CucutaStore =  Tienda("Cucuta")

#¿?? Como envio todo el objeto para que quede como una lista. Debo colocar todos los campos?, Es necesario?
TexasStore.add_product(producto1.productName).add_product(producto2.productName).add_product(producto3.productName).show_products().load_inventory("baberos", 10).sell_product("baberos", 2).load_inventory("baberos", 4).show_inventory("baberos")



