import sys
import re

print()
print("Analizador Lexico")
print()

#Declaramos el archivo para abrir
file = open("Prueba1.txt")


#Diccionarios
identificadores = {'a' : 'id','b' : 'id','c' : 'id','d' : 'id','e' : 'id','f' : 'id','g' : 'id','h' : 'id','i' : 'id','j' : 'id','k' : 'id','l' : 'id','m' : 'id','n' : 'id',
                   'o' : 'id','p' : 'id','q' : 'id','r' : 'id','s' : 'id','t' : 'id','u' : 'id','v' : 'id','w' : 'id','x' : 'id','y' : 'id','z' : 'id',
                   'A' : 'id','B' : 'id','C' : 'id','D' : 'id','E' : 'id','F' : 'id','G' : 'id','H' : 'id','I' : 'id','J' : 'id','K' : 'id','L' : 'id','M' : 'id','N' : 'id',
                   'O' : 'id','P' : 'id','Q' : 'id','R' : 'id','S' : 'id','T' : 'id','U' : 'id','V' : 'id','W' : 'id','X' : 'id','Y' : 'id','Z' : 'id'}
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


    # Expresión regular para dividir la línea en tokens
    token_pattern = re.compile(r'(".*?"|\b\w+\b|[<>=!]=?|[-+*/{}(),.;])')
    tokens = token_pattern.findall(line)
    print("Los Lexemas son:", tokens)

    print("Linea #", count, "Token: \n")
    for token in tokens:
        #Tokens de un caracter
        if token in simbolos1C_key:
            print(simbolos1C[token])
        #Tokens de uno o dos caracteres
        if token in simbolos2C_key:
            print(simbolos2C[token])
        #Literales
        if token in identificadores_key:
            print(identificadores[token])
        if token.startswith('"') and token.endswith('"'):
        # Token es una cadena encerrada en comillas
            cadena_sin_comillas = token[1:-1]  # Elimina las comillas del principio y el final
            cadenas[token] = cadena_sin_comillas
            print("Cadena:", cadena_sin_comillas)
         #Palabras Clave   
        if token in palabras_reservadas_key:
            print(palabras_reservadas[token])

    print("................................................")
        


