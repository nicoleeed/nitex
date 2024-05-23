from colorama import Fore, Style
from tabulate import tabulate
# Lee el archivo de texto y almacena las líneas en una lista
with open("table/Hoja1.txt", "r") as file:
    lines = file.readlines()

# Inicializa una lista vacía para almacenar los elementos de la tabla
table = []

# Divide cada línea por las comas y agrega los elementos a la tabla
for line in lines:
    table.append(line.strip().split(","))

# Imprime la tabla en formato de tabla
# for row in table:
#     print("|".join(row))

print(Fore.BLUE + tabulate(table, headers="firstrow", tablefmt="fancy_grid")+ Style.RESET_ALL)
