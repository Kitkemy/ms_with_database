def save_new_saldo(saldo):
    new_saldo = str(saldo)
    file_saldo = open('saldo.txt', 'w')
    file_saldo.write(new_saldo)
    file_saldo.close()

def save_new_store(store):
    file_store = open('store.txt', 'w')
    for id in store:
        product_name = id.get('product_name')
        count =  str(id.get('count'))
        price =  str(id.get('price'))
        file_store.write(product_name + ";" + count + ";" + price + "\n")
    file_store.close()

def save_new_logs(logs):
    new_logs = str(logs)
    file_logs = open('logs.txt', 'a')
    file_logs.write(new_logs)
    file_logs.close()

def get_saldo(file_name):
    file_saldo = open(file_name)
    saldo = float(file_saldo.readline())
    file_saldo.close()
    return saldo