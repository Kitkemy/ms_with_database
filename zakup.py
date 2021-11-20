#python zakup.py <plik> <str identyfikator produktu> <int cena> <int liczba zakupionych>
import sys
from methods import get_saldo, save_new_saldo, save_new_logs, get_store, save_new_store

file_name = sys.argv[1]
product_name = sys.argv[2]
product_price = float(sys.argv[3])
product_count = int(sys.argv[4])

product_total_price = product_count * product_price

saldo = get_saldo("saldo.txt")
store = get_store(file_name)
all_products = []

if product_total_price > saldo:
    print(f"Cena za towary ({product_total_price}) przekracza wartość salda ({saldo})")

else:
    saldo = saldo - product_total_price

    all_products = []

    for products in store:
        pro_name = products.get('product_name')
        all_products.append(pro_name) 
    if product_name in all_products:
        product_index = all_products.index(product_name)
        count_temp = store[product_index].get('count')
        del store[product_index]
        new_count = int(product_count) + int(count_temp)
        product_dict = {
            'product_name': product_name,
            'count': str(new_count),
            'price': product_price
        }
        store.append(product_dict)
    else:
        product_dict = {
            'product_name': product_name,
            'count': product_count,
            'price': product_price
        }
        store.append(product_dict)

    logs = []    
    log = f"zakup: {product_name}, sztuk: {product_count}, cena za sztuke: {product_price}"
    logs.append(log)
    save_new_logs(logs)
    save_new_saldo(saldo)
    save_new_store(store)