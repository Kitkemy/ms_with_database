import sys
from methods import save_new_saldo, save_new_store

COMMANDS = "saldo", "zakup", "sprzedaz", "stop"

##saldo = 1000.0
file_saldo = open('saldo.txt')
saldo = float(file_saldo.readline())
file_saldo.close()

store = []


file_store = open('store.txt', 'r')
for line in file_store.readlines():
    splitted_line = line.split(';')
    product_name = splitted_line[0]
    product_count = splitted_line[1]
    product_price = splitted_line[2].replace('\n','')
    product_dict = {
        'product_name': product_name,
        'count': product_count,
        'price': product_price
    }
    store.append(product_dict)
file_store.close()
print(store)

#mode = sys.argv[1]

logs = [] #historia operacji

while True:
    action = input("podaj komendę:")    

    if action not in COMMANDS:
        print("niepoprawna komenda!")
        continue
    if action == "stop":
        save_new_saldo(saldo)
        save_new_store(store)
        break

    if action == "saldo":
        amount = float(input("kwota salda: "))
        saldo_comment = (input("komentarz: "))
        if amount < 0:
            if (amount < 0) and (saldo + amount < 0):
                print("za mało środków na koncie!")
                continue
        saldo = saldo + amount

        log = f"zmiana saldo: {amount}, komentarz /{saldo_comment}/"
        logs.append(log)

    elif action == "zakup":
        product_name = input("Nazwa produktu: ")
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("Cena za sztukę: "))
        product_total_price = product_count * product_price
        if product_total_price > saldo:
            print(f"Cena za towary ({product_total_price}) przekracza wartość salda ({saldo})")
            continue
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
            
        log = f"zakup: {product_name}, sztuk: {product_count}, cena za sztuke: {product_price}"
        logs.append(log)
        
    elif action == "sprzedaz":
        product_name = input("Nazwa produktu: ")
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("cena za sztukę: "))
        if not store.get(product_name):
            print("nie ma takiego produktu w sklepie")
            continue
        if store.get(product_name)["count"] < product_count:
            print("niewsyatrczająca ilość towaru")
            continue
        store[product_name] = {
            'count': store.get(product_name)['count'] - product_count,
            'price': product_price
        }
        saldo += product_count * product_price

        log = f"sprzedaż: {product_name}, sztuk {product_count}, cane za sztukę {product_price}"
        logs.append(log)

        if not store.get(product_name)['count']:
            del store[product_name]
'''
if mode == 'konto':
    print(f"saldo: {saldo}")
elif mode == 'przeglad':
    print (logs)


#saldo <int wartosc> <str komentarz>
elif mode == "saldo":
    amount = float(sys.argv[2])
    saldo_comment = sys.argv[3]
    if amount < 0:
        if (amount < 0) and (saldo + amount < 0):
            print("za mało środków na koncie!")
    saldo = saldo + amount

    save_new_saldo(saldo)

    log = f"zmiana saldo: {amount}, komentarz /{saldo_comment}/"
    logs.append(log)

#python accountant.py sprzedaż <str identyfikator produktu> <int cena> <int liczba sprzedanych>
elif mode == "sprzedaz":
    product_name = sys.argv[2]
    product_price = float(sys.argv[3])
    product_count = int(sys.argv[4])
    if not store.get(product_name):
        print("nie ma takiego produktu w sklepie")
    if store.get(product_name)["count"] < product_count:
        print("niewsyatrczająca ilość towaru")
    store[product_name] = {
        'count': store.get(product_name)['count'] - product_count,
        'price': product_price
    }
    saldo += product_count * product_price

    log = f"sprzedaż: {product_name}, sztuk {product_count}, cane za sztukę {product_price}"
    logs.append(log)

    if not store.get(product_name)['count']:
        del store[product_name]

#python accountant.py zakup <str identyfikator produktu> <int cena> <int liczba zakupionych>
elif mode == "zakup":
    product_name = sys.argv[2]
    product_price = float(sys.argv[3])
    product_count = int(sys.argv[4])
    product_total_price = product_count * product_price
    if product_total_price > saldo:
        print(f"Cena za towary ({product_total_price}) przekracza wartość salda ({saldo})")
    else:
        saldo = saldo - product_total_price
        if not store.get(product_name):
            store[product_name] = {"count": product_count, "price": product_price}
        else:
            store_product_count = store[product_name]["count"]
            store[product_name] = {
                "count": store_product_count + product_count,
                "price": product_price}

    log = f"zakup: {product_name}, sztuk: {product_count}, cena za sztuke: {product_price}"
    logs.append(log)   

# python accountant.py magazyn <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
elif mode == "magazyn":
    n = len(sys.argv)
  
    for i in range(2, n):
        product_name = sys.argv[i]
        print(f"{product_name} {store.get(product_name)['count']}")
'''