#python konto.py <plik>

import sys
from methods import get_saldo

file_name = sys.argv[1]
saldo = get_saldo(file_name)
print(f"saldo: {saldo}")