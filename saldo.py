 #python saldo.py <str plik> <int wartosc> <str komentarz>
import sys
from methods import get_saldo, save_new_saldo, save_new_logs

file_name = sys.argv[1]
amount = float(sys.argv[2])
saldo_comment = sys.argv[3]

saldo = get_saldo(file_name)
saldo = saldo + amount
save_new_saldo(saldo)

logs = []
log = f"zmiana saldo: {amount}, komentarz /{saldo_comment}/"
logs.append(log)
save_new_logs(logs)