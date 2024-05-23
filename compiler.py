from colorama import Fore, Style
from anytree import Node, RenderTree, PreOrderIter
from tabulate import tabulate

input_code = open('tests/test1.txt').read()
grammar_file_path = 'grammar/LL1Grammar.txt'
table_file_path = 'table/table.txt'
terminals_file_path = 'grammar/terminals.txt'

caracter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","*", "/", "-", "+","(",")","<",">","=",";",",",".",":","!","?","_","%","#","^","`","'"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
reserved_words = ["/t1", "/t2", "/t3", "/p", "/url", "/img","/tb","/l","/sl","/b","/i","/u"]
delimiter_operators = [ '[', ']', '{', '}', ',','(',')']
special_caracters = ['@', '&', '|', '~', '\\','\{', '\}',"/","\\"]

index = 0
errors = 0
row = 1
column = 0
output_tokens = []
tokens = []
output_errors = []
parse_errors = []

def print_presentation():
    print(Fore.RED + """
███╗   ██╗██╗████████╗███████╗██╗  ██╗
████╗  ██║██║╚══██╔══╝██╔════╝╚██╗██╔╝
██╔██╗ ██║██║   ██║   █████╗   ╚███╔╝ 
██║╚██╗██║██║   ██║   ██╔══╝   ██╔██╗ 
██║ ╚████║██║   ██║   ███████╗██╔╝ ██╗
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝""" + Style.RESET_ALL)

    print(Fore.RED + """
               _  _ ___ ___ ___  _    ___   ___  _   _ ___    _   _  _ ___  
         ___  | \| |_ _/ __/ _ \| |  | __| |   \| | | | _ \  /_\ | \| |   \ 
        |___| |  ` || | (_| (_) | |__| _|  | |) | |_| |   / / _ \| .` | |) |
              |_|\_|___\___\___/|____|___| |___/ \___/|_|_\/_/ \_\_|\_|___/ 
                                                                                                           """ + Style.RESET_ALL)
                                                                               
def read_grammar(grammar_file_path):
    grammar = {}

    with open(grammar_file_path, 'r') as file:
        production_number = 0
        for line in file:
            line = line.strip()
            if line:
                # Dividir la línea en la parte antes y después del símbolo ->
                lhs, rhs = line.split('->')
                lhs = lhs.strip()
                rhs = rhs.strip()
                # Si la parte derecha tiene punto y coma, divídela
                if ';' in rhs:
                    rhs_parts = rhs.split(';')
                else:
                    # De lo contrario, la parte derecha es un solo elemento
                    rhs_parts = [rhs]

                # Agregar la producción al diccionario principal
                grammar[production_number] = (lhs.split(), rhs_parts)
                production_number += 1

    return grammar

def read_grammar_table(table_file_path):
    grammar_table = {}

    with open(table_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Dividir la línea en la parte antes y después de la flecha (->)
                lhs, rhs = line.split('->')
                lhs = lhs.strip()
                rhs = rhs.strip()

                # Almacenar en el diccionario utilizando una tupla como clave
                grammar_table[lhs] = int(rhs)  
    return grammar_table

def read_terminals(terminals_file_path):
    terminal_symbols_ = []

    with open(terminals_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):  # Ignorar líneas vacías y comentarios
                # Dividir la línea por espacios en blanco y tomar el primer elemento
                symbol = line.split()[0]
                if symbol not in terminal_symbols_:
                    terminal_symbols_.append(symbol)

    return terminal_symbols_

def print_table():
    with open("table/Hoja1.txt", "r") as file:
        lines = file.readlines()

    # Inicializa una lista vacía para almacenar los elementos de la tabla
    table = []

    # Divide cada línea por las comas y agrega los elementos a la tabla
    for line in lines:
        table.append(line.strip().split(";"))

    print(Fore.GREEN + tabulate(table, headers="firstrow", tablefmt="fancy_grid")+ Style.RESET_ALL)

def print_grammar():
    print(Fore.BLUE +"""
╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
╠═╝╠╦╝║ ║ ║║║ ║║   ║ ║║ ║║║║╚═╗
╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝""" + Style.RESET_ALL)
    for clave, valor in grammar_productions.items():
        clave_str = str(clave) if clave >= 10 else f"{clave} " # Agrega un espacio si la clave es menor que 10
        print(Fore.RED + clave_str + Style.RESET_ALL, " ".join(valor[0]),Fore.YELLOW + "->"+ Style.RESET_ALL, " ".join(valor[1]))
    
    print(Fore.BLUE +"""
╔═╗╔═╗╦═╗╔═╗╦╔╗╔╔═╗  ╔╦╗╔═╗╔╗ ╦  ╔═╗
╠═╝╠═╣╠╦╝╚═╗║║║║║ ╦   ║ ╠═╣╠╩╗║  ║╣ 
╩  ╩ ╩╩╚═╚═╝╩╝╚╝╚═╝   ╩ ╩ ╩╚═╝╩═╝╚═╝"""+ Style.RESET_ALL)
    print_table()
        
    print(Fore.BLUE +"""
╔╦╗╔═╗╦═╗╔╦╗╦╔╗╔╔═╗╦  ╔═╗
 ║ ║╣ ╠╦╝║║║║║║║╠═╣║  ╚═╗
 ╩ ╚═╝╩╚═╩ ╩╩╝╚╝╩ ╩╩═╝╚═╝"""+ Style.RESET_ALL)
    for terminal in terminal_symbols:
        print(terminal)
  
def peek_char():
    global index
    if index >= len(input_code):
        return ''
    elif (index < len(input_code)-3 and input_code[index]+input_code[index+1]+input_code[index+2]) == '/c{':
        index += 3
        while (input_code[index]) != '}':
            index += 1
        index += 3
        return peek_char()
    #error de cerrar comentario 
    return input_code[index]

def get_char():
    global index
    global column
    char = peek_char()
    column += 1
    index += 1
    return char

def get_tokens():
    global row
    global column
    global index
    global tokens
    global errors
    global output_tokens
    global output_errors
    
    while (True):
        current_char = get_char()
        char_aux_new_line = peek_char()
        if current_char == '$':
            tokens.append('$')
            break
        elif current_char+char_aux_new_line == "/n":
            row += 1
            column = 0
            index += 1
            output_tokens.append(f"NL \"{current_char}\" found at ({row}:{column})")
            tokens.append("/n")
            
        elif current_char in delimiter_operators:
            if current_char == "{":
                output_tokens.append(f"BLCO \"{current_char}\" found at ({row}:{column})")
                tokens.append("{")
            elif current_char == "}":
                output_tokens.append(f"BLCC \"{current_char}\" found at ({row}:{column})")
                tokens.append("}")
            elif current_char == ",":
                output_tokens.append(f"SPC \"{current_char}\" found at ({row}:{column})")
                tokens.append(",")
            elif current_char == "[":
                output_tokens.append(f"BTO \"{current_char}\" found at ({row}:{column})")
                tokens.append("[")
            elif current_char == "]":
                output_tokens.append(f"BTC \"{current_char}\" found at ({row}:{column})")
                tokens.append("]")
            elif current_char == "(":
                output_tokens.append(f"PO \"{current_char}\" found at ({row}:{column})")
                tokens.append("(")
            elif current_char == ")":
                output_tokens.append(f"PC \"{current_char}\" found at ({row}:{column})")
                tokens.append(")")

        
        elif current_char in numbers:
            index_origin = index
            output_tokens.append(f"INT \" {current_char} \" found at ({row}:{column})")
            #print("tok val " +current_char)
            tokens.append("INT")
            if int(current_char+input_code[index_origin:index].replace(" ", "").replace("/n", "")) > 9:
                errors += 1
                output_errors.append(
                    "int max size exceeded at line: "+str(row)+", column: "+str(column))
        elif current_char in caracter:
            index_origin = index
            char_aux = peek_char()
            while (char_aux in caracter or char_aux in numbers or char_aux in special_caracters or char_aux == " " ) and char_aux != "/":
                if char_aux in special_caracters:
                    output_errors.append(
                        "special caracter at line: "+str(row)+", column: "+str(column))
                    errors += 1                    
                index += 1
                column += 1
                char_aux = peek_char()
            word = (
                current_char+input_code[index_origin:index]).replace("/n", "")
            if word in reserved_words:
                output_tokens.append(f"RESERVED_WORD \"{word}\" found at ({row}:{column})")
                tokens.append(word)
            else:
                output_tokens.append(f"PLAIN_TEXT \"{word}\" found at ({row}:{column})")
                tokens.append("PLAIN_TEXT")
    return tokens
     
def scan():
    get_tokens()
    
    print(Fore.GREEN + "============================================================================" )
    print(Fore.BLUE +"""
╔═╗╔═╗╔═╗╔╗╔╔╗╔╔═╗╦═╗
╚═╗║  ╠═╣║║║║║║║╣ ╠╦╝
╚═╝╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═"""+ Style.RESET_ALL)
    print(Fore.GREEN + "INFO SCAN - Start scanning" )
    print(Fore.GREEN + "============================================================================" )
    for i in output_tokens:
        print(Fore.GREEN + "DEBUG SCAN - " + Fore.BLUE +i+ Style.RESET_ALL)
    print(Fore.GREEN + "============================================================================" )
    
    print(Fore.GREEN + "INFO SCAN - Completed with" )
    
    print(Fore.CYAN + "Error(s): ", errors)
    if errors > 0:
        print(Fore.CYAN + "============================================================================" )
        for i in output_errors:
            print(Fore.CYAN + i+ Style.RESET_ALL)
        print(Fore.CYAN + "============================================================================" )
    
    print(Fore.BLUE +"""
╔╦╗╔═╗╦╔═╔═╗╔╗╔╔═╗
 ║ ║ ║╠╩╗║╣ ║║║╚═╗
 ╩ ╚═╝╩ ╩╚═╝╝╚╝╚═╝"""+ Style.RESET_ALL)
    print(Fore.BLUE + "============================================================================" + Style.RESET_ALL)
    for i in tokens:
        print(i)
    print(Fore.BLUE + "============================================================================" + Style.RESET_ALL)

def find_closest_node(node, target_name):
    # Buscar entre los hermanos del nodo actual
    for sibling in node.siblings:
        if sibling.name == target_name:
            if target_name == "BLCC" and node.children:
                continue
            return sibling
    
    # Buscar entre los ancestros del nodo actual
    parent = node.parent
    while parent:
        for sibling in parent.siblings:
            if sibling.name == target_name:
                if target_name == "BLCC" and node.children:
                    continue
                return sibling
        parent = parent.parent
    
    return None

def find_leaf_node(root, target_name):
    last_found_node = None
    for node in PreOrderIter(root):
        if node.name == target_name:
            if target_name == "BLCC" and node.children:
                continue
            last_found_node = node
    return last_found_node
    
def print_preOrder_tree(root):
    for node in PreOrderIter(root):
        if node.name.startswith(("PLAIN_TEXT", "INT")):
            print(node.name)
        elif node.name in terminal_symbols:
            print(node.name)
def preOrder_tree(root):
    for node in PreOrderIter(root):
        print(node.name)
def print_tree(tree_root):
    for pre, _, node in RenderTree(tree_root):
        if node.name.startswith(("PLAIN_TEXT", "INT")):
            # Imprimir el nombre del nodo en rojo, excluyendo "PLAIN_TEXT" o "INIT" y ": "
            name_without_prefix = node.name.split(": ")[1]
            print("%s%s" % (pre, Fore.RED + name_without_prefix + Fore.RESET))
        elif node.name in terminal_symbols:
            print("%s%s" % (pre, Fore.RED + node.name + Fore.RESET))
        else:
            print("%s%s" % (pre, Fore.BLUE + node.name + Fore.RESET))

def parsing(scaned_tokens):
    stack = ["$","$", "G"]  
    current_token = 0 
    tree_root = Node("G")
    current_node = tree_root
    while True:
        print(Fore.GREEN +"Stack -> "+ Style.RESET_ALL, stack)
        #print(Fore.GREEN +"Parse Tree -> "+ Style.RESET_ALL)
        #print_tree(tree_root)
        
        top_of_stack = stack[-1]  # Elemento en la cima de la pila      
        #print(Fore.GREEN +"Current Token -> "+ Style.RESET_ALL, scaned_tokens[current_token])
        if top_of_stack == "$" and current_token == len(scaned_tokens) and len(parse_errors) == 0:
            print(Fore.RED +"""
╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔═╗  ┬
╚═╗║ ║║  ║  ║╣ ╚═╗╚═╗  │
╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝  o Input successfully parsed!""" + Style.RESET_ALL)
            break
        if top_of_stack == "$" and current_token == len(scaned_tokens) and len(parse_errors) > 0:
            print(Fore.RED +"""
╔═╗╔═╗╦╦  ┬
╠╣ ╠═╣║║  │
╚  ╩ ╩╩╩═╝o  The Input could not be parsed!""" + Style.RESET_ALL)
            break
        if top_of_stack == "ε":
            stack.pop()
            current_node = current_node.parent
            top_of_stack = stack[-1]
                
        elif top_of_stack in terminal_symbols:
            if top_of_stack == scaned_tokens[current_token]:
                stack.pop()  
                current_token += 1  
                if current_node.name == top_of_stack:
                    current_node = current_node.parent
            else:
                #print(Fore.CYAN + "Error: Unexpected input. Expecting:", top_of_stack + Style.RESET_ALL)
                if top_of_stack != "$" and  current_token == len(scaned_tokens) -1:
                    print(Fore.RED +"""
╔═╗╔═╗╦╦  ┬
╠╣ ╠═╣║║  │
╚  ╩ ╩╩╩═╝o  The Input could not be parsed!""" + Style.RESET_ALL)
                    break
                token_info = output_tokens[current_token].split("found at")[1]
                row_column = token_info.split(":")
                row = row_column[0]
                column = row_column[1]
                parse_errors.append(
                    "Unexpected input. Expecting: "+ top_of_stack + " at line: "+str(row)+", column: "+str(column))
                
                current_token += 1
                continue
        else:
            # Construir la cadena de búsqueda     
            search_key = f'({top_of_stack},{scaned_tokens[current_token]})'
            #print(search_key, "-",parse_table[search_key])
            
            if (search_key) in parse_table:
                # Buscar en la tabla utilizando la cadena de búsqueda
                production = parse_table[search_key] # Obtiene la producción de la tabla
                stack.pop()  
                
                production_key = grammar_productions[production]
                
                # Empuja los símbolos de la producción en orden inverso a la pila
                for symbol in reversed(production_key[1]):
                    stack.append(symbol)
                    
                primer_simbolo = True
                for symbol in production_key[1]:
                    if primer_simbolo:
                        parent_node = find_closest_node(current_node, top_of_stack)
                        if not parent_node :
                            parent_node = find_leaf_node(tree_root, top_of_stack)
                        # Verificar si el padre tiene hijos
                        if not parent_node.children:
                            if symbol == "PLAIN_TEXT" or symbol == "INT":
                                parts = output_tokens[current_token].split('"')
                                # Si hay al menos dos partes (inicio y fin de las comillas), agrega la segunda parte a la lista
                                if len(parts) >= 2:
                                    symbol =symbol + " : " + parts[1]
                                    
                            current_node = Node(symbol, parent=parent_node)
                        else:
                            # Obtener el primer hijo del padre
                            first_child = parent_node.children[0]
                            # Agregar el nuevo nodo como el segundo hijo
                            if symbol == "PLAIN_TEXT" or symbol == "INT":
                                parts = output_tokens[current_token].split('"')
                                # Si hay al menos dos partes (inicio y fin de las comillas), agrega la segunda parte a la lista
                                if len(parts) >= 2:
                                    symbol =symbol + " : " + parts[1]
                                    
                            current_node = Node(symbol, parent=parent_node)
                            # Insertar el nuevo nodo después del primer hijo
                            current_node.parent = None  
                            current_node.parent = parent_node  
                            first_child.parent = None  
                            first_child.parent = parent_node
                        primer_simbolo = False
                    else:
                        # Si no es el primer símbolo, crea un nuevo nodo con el símbolo actual
                        current_node = Node(symbol, parent=parent_node)
            else:
                #print(Fore.CYAN + "Error: No valid production found for:", top_of_stack, "and", scaned_tokens[current_token]+ Style.RESET_ALL)
                if top_of_stack != "$" and  current_token == len(scaned_tokens) -1:
                    print(Fore.RED +"""
╔═╗╔═╗╦╦  ┬
╠╣ ╠═╣║║  │
╚  ╩ ╩╩╩═╝o  The Input could not be parsed!""" + Style.RESET_ALL)
                    break
                token_info = output_tokens[current_token].split("found at")[1]
                row_column = token_info.split(":")
                row = row_column[0]
                column = row_column[1]
                parse_errors.append(
                    "Error: No valid production found for: " + top_of_stack+ " and "+ scaned_tokens[current_token]+ " at line: "+str(row)+", column: "+str(column))
                #imprimir tambien las producciones que se pueden hacer con el top of stack
                parse_errors.append("Maybe you meant:")
                for key in parse_table:
                    # Verifica si la clave comienza con el valor de top_of_stack
                    if key.startswith(f'({top_of_stack},'):
                        # Si coincide, agrega la segunda parte del key a la lista
                        parse_errors.append(key.split(',')[1][:-1])
                current_token += 1
                continue
    return tree_root
      

print_presentation()

grammar_productions=read_grammar(grammar_file_path)
parse_table=read_grammar_table(table_file_path)
terminal_symbols = read_terminals(terminals_file_path)

print_grammar()

scan()

print(Fore.GREEN +"""
╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗
╠═╝╠═╣╠╦╝╚═╗║╣ ╠╦╝
╩  ╩ ╩╩╚═╚═╝╚═╝╩╚═"""+ Style.RESET_ALL)

print(Fore.GREEN + "============================================================================" + Style.RESET_ALL)

tree_root = parsing(tokens)

if len(parse_errors) > 0:
    print(Fore.CYAN + "Parse Error(s): ", len(parse_errors))
    print(Fore.CYAN + "============================================================================" )
    for i in parse_errors:
        print(Fore.CYAN + i+ Style.RESET_ALL)

print(Fore.GREEN + "============================================================================" + Style.RESET_ALL)

if len(parse_errors) == 0:
    print(Fore.GREEN +"""
╔═╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╦═╗╔═╗╔═╗
╠═╝╠═╣╠╦╝╚═╗║╣    ║ ╠╦╝║╣ ║╣ 
╩  ╩ ╩╩╚═╚═╝╚═╝   ╩ ╩╚═╚═╝╚═╝"""+ Style.RESET_ALL)

    print(Fore.GREEN + "============================================================================" + Style.RESET_ALL)

    print_tree(tree_root)

    print(Fore.GREEN + "============================================================================" + Style.RESET_ALL)
    
    print_preOrder_tree(tree_root)