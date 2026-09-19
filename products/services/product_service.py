import requests

from ..models import Product

def get_products():
    response = requests.get("https://fakestoreapi.com/products")
    if response.status_code != 200:
        print(f"Error al obtener los productos:{response.status_code}")
        return[]
    
    return response.json()

def load_products():
    if Product.objects.count():
        return f"ya existen {Product.objects.count()}productos"
    products = get_products()
    for product in products:
        del product["category"]
        del product["rating"]
        Product.objects.create(**product)
        # Product.objects.create(
        #     title=product["title"],
        #     description=product["description"],
        # )
        
    return f"Se cargaron {Product.objects.count()} productos"