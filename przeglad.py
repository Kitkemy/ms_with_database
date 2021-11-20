#python przeglad.py <plik>
import sys
file_name = sys.argv[1]


file_logs = open(file_name, 'r')

logs = file_logs.read()

print(logs)