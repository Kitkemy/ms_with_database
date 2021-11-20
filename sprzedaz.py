#python sprzedaz.py <plik><str identyfikator produktu> <int cena> <int liczba sprzedanych>
import sys
from methods import get_saldo, save_new_saldo, save_new_logs, get_store, save_new_store

file_name = sys.argv[1]
product_name = sys.argv[2]
product_price = float(sys.argv[3])
product_count = int(sys.argv[4])

saldo = get_saldo("saldo.txt")
store = get_store(file_name)

all_products = []

for products in store:
    pro_name = products.get('product_name')
    all_products.append(pro_name)

if product_name not in all_products:
    print("nie ma takiego produktu w sklepie")    

product_index = all_products.index(product_name)
count_temp = int(store[product_index].get('count'))
if count_temp < product_count:
    print("niewsystrczająca ilość towaru")

store[product_index] = {
    'product_name': product_name,
    'count': count_temp - product_count,
    'price': product_price
}

saldo += product_count * product_price

logs = []
log = f"sprzedaz: {product_name}, sztuk {product_count}, cena za sztuke {product_price}"
logs.append(log)
save_new_logs(logs)

if (store[product_index].get('count')) == 0:
    del store[product_index]

save_new_saldo(saldo)
save_new_store(store)