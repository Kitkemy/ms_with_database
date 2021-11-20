#python magazyn.py <plik><str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
import sys
from methods import get_store
file_name = sys.argv[1]
store = get_store(file_name)

all_products = []

for products in store:
    pro_name = products.get('product_name')
    all_products.append(pro_name) 

n = len(sys.argv)

for i in range(2, n):
    product_name = sys.argv[i]
    product_index = all_products.index(product_name)
    print(f"{product_name} {store[product_index].get('count')}")