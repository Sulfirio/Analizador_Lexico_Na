import sys


print()
print("Analizador Lexico")
print()

# Verificamos si se proporcionó un argumento en la línea de comandos
if len(sys.argv) != 2:
    sys.exit(1)

archivo_entrada = sys.argv[1]

# Abrir el archivo 
with open(archivo_entrada, 'r') as file:


#Diccionarios
    identificadores = {'a' : 'id','b' : 'id','c' : 'id','d' : 'id','e' : 'id','f' : 'id','g' : 'id','h' : 'id','i' : 'id','j' : 'id','k' : 'id','l' : 'id','m' : 'id','n' : 'id',
                    'o' : 'id','p' : 'id','q' : 'id','r' : 'id','s' : 'id','t' : 'id','u' : 'id','v' : 'id','w' : 'id','x' : 'id','y' : 'id','z' : 'id',
                    'A' : 'id','B' : 'id','C' : 'id','D' : 'id','E' : 'id','F' : 'id','G' : 'id','H' : 'id','I' : 'id','J' : 'id','K' : 'id','L' : 'id','M' : 'id','N' : 'id',
                    'O' : 'id','P' : 'id','Q' : 'id','R' : 'id','S' : 'id','T' : 'id','U' : 'id','V' : 'id','W' : 'id','X' : 'id','Y' : 'id','Z' : 'id'}
    
    id = []
    
    identificadores_key = identificadores.keys()

    palabras_reservadas = {'and' : 'AND', 'else' : 'ELSE', 'false' : 'FALSE', 'for' : 'FOR',
                        'fun' : 'FUN', 'if' : 'IF', 'null' : 'NULL',
                        'or' : 'OR', 'print' : 'PRINT', 'return' : 'RETURN',
                        'true' : 'TRUE', 'var' : 'VAR', 'while': 'WHILE'}
    palabras_reservadas_key = palabras_reservadas.keys()

    cadenas = {}
    cadenas_key = cadenas.keys()

    simbolos1C = {
                '+' : 'PLUS', '-' : 'MINUS','*' : 'STAR', '/' : 'SLASH', '{' : 'LEFT_BRACE', '}' : 'RIGHT_BRACE',
                '(' : 'LEFT_PAREN', ')' : 'RIGHT_PARENT', ',' : 'COMMA', '.' : 'DOT', ';' : 'SEMICOLON' }
    simbolos1C_key = simbolos1C.keys()

    simbolos2C = {'!' : 'BANG','!=' : 'BANG_EQUAL', '=' : 'EQUAL','==' : 'EQUAL_EQUAL','>' : 'GREATER','>=' : 'GREATER_EQUAL',
                '<' : 'LESS ','<=' : 'LESS_EQUAL'}
    simbolos2C_key = simbolos2C.keys()

    #Leemos el archivo
    a = file.read()
    count = 0


    #Dividimos el archivo.
    program = a.split("\n")
    for line in program:
        count = count + 1
        print("Linea #",count ,'\n',line)

        if not line.strip():
            continue  #Ignoramos lineas vacias
    # Verificamos si la línea comienza con '//'
        if line.strip().startswith('//'):
            continue  # Ignoramos la línea y pasamos a la siguiente
        if line.strip().startswith('/*'):
            continue  #Ignoramos el inicio de comentario
        if line.strip().endswith('*/'):
            continue  #Ignoramos el fin de comentario


        def tokenize(line):
            tokens = []
            current_token = ""
            state = "inicio"

            for char in line:
                if state == "inicio":
                    if char == '"':
                        current_token += char
                        state = "entre_comillas"
                    elif char.isalpha():
                        current_token += char
                        state = "palabra"
                    elif char in "<>=!":
                        current_token += char
                        state = "operador"
                    elif char.isalpha:
                        current_token += char
                        state = "ID"
                    else:
                        tokens.append(char)
                        
                        
                elif state == "ID":
                    if char.isalpha() or char.isnumeric():                
                        state = "ID"
                        current_token += char
                        
                    else:
                        tokens.append(current_token)
                        id.append(current_token)
                        current_token = ""
                        state = "inicio"
                        print("Estado de token es:",current_token)
                        
                        
                elif state == "entre_comillas":
                    current_token += char
                    if char == '"':
                        tokens.append(current_token)
                        current_token = ""
                        state = "inicio"
                elif state == "palabra":
                    if char.isalnum():
                        current_token += char
                    else:
                        tokens.append(current_token)
                        identificadores['id'] = current_token
                        current_token = ""
                        state = "inicio"
                        if char == '"':
                            current_token += char
                            state = "entre_comillas"
                        elif char in "<>=!":
                            current_token += char
                            state = "operador"
                        else:
                            tokens.append(char)
                elif state == "operador":
                    if char in "=!":
                        current_token += char
                    else:
                        tokens.append(current_token)
                        current_token = ""
                        state = "inicio"
                        if char in "<>=":
                            current_token += char
                        else:
                            tokens.append(char)

            if current_token:
                tokens.append(current_token)

            return tokens

        tokens = tokenize(line)
        print("Los Lexemas son:", tokens)

        print("Linea #", count, "Token: \n")
        for token in tokens:
            #Tokens de un caracter
            if token in simbolos1C_key:
                print(simbolos1C[token])
            #Tokens de uno o dos caracteres
            elif token in simbolos2C_key:
                print(simbolos2C[token])
            #Literales
            elif token in identificadores_key:
                print(identificadores[token])
            elif token.startswith('"') and token.endswith('"'):
            # Token es una cadena encerrada en comillas
                cadena_sin_comillas = token[1:-1]  # Elimina las comillas del principio y el final
                cadenas[token] = cadena_sin_comillas
                print("Cadena:", cadena_sin_comillas)
            #Palabras Clave   
            elif token in palabras_reservadas_key:
                print(palabras_reservadas[token])
            elif token == " ":
                a = 1
            elif token in id:
                print(id[token])
            else:
            # Token desconocido
                print(f"Error: Token desconocido '{token}'")
                print(identificadores)
                sys.exit(1)

        print("................................................")
