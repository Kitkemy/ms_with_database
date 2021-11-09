def save_new_saldo(saldo):
    new_saldo = str(saldo)
    file_saldo = open('saldo.txt', 'w')
    file_saldo.write(new_saldo)
    file_saldo.close()