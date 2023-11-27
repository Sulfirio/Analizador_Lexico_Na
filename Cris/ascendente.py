import sys


class Token:
    def __init__(self, token_type, value, literal=None):
        self.type = token_type
        self.value = value
        self.literal = literal


token_dict = {
    "COMMA": ",",
    "DOT": ".",
    "ASTERIC": "*",
    "IDENTIFIER": "identifier",
    "SELECT": "EOF",
    "DISTINCT": "EOF",
    "FROM": "EOF"
}

keywords = [
    "AND", "ELSE", "FALSE", "FUN", "FOR", "IF", "NULL", "OR",
    "PRINT", "RETURN", "TRUE", "VAR", "WHILE", "SELECT", "DISTINCT", "FROM"]


def analizador_lexico(input_string):
    tokens = []
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    SA = -1
    S14 = 14

    state = S0
    pos = 0
    token = ""
    while pos < len(input_string):
        char = input_string[pos]
        if state == S0:
            token = ""
            if char.isspace():
                pos += 1
                continue
            elif char.isalpha():
                state = S1
            elif char == '*':
                state = S2
                token = "*"
                continue
            elif char == '.':
                state = S3
                token = "."
                continue
            elif char == ',':
                token = ","
                state = S4
                continue
            else:
                state = SA
        if state == S1:
            if char.isalpha() or char.isnumeric():
                state = S1
                token += char
            elif char == ".":
                pos += 1
                state = 14
                continue
            elif char == ",":
                state = 14
                pos += 1
                continue
            else:
                state = 14
            pos += 1

        if state == S2:
            tokens.append(("ASTERIC", token))
            state = 0
            pos += 1

        if state == S3:
            tokens.append(("DOT", token))
            state = 0
            pos += 1

        if state == S4:
            tokens.append(("COMMA", token))
            state = 0
            pos += 1

        if state == S14:
            status = 0
            for i in range(len(keywords)):
                if token == (keywords[i].lower()):
                    tokens.append([keywords[i], token])
                    status = 1
            if status == 0:
                tokens.append(["IDENTIFIER", token])
            state = S0
            pos -= 1

        if state == SA:
            print("Error.")
            return tokens

    return tokens


def analizador_ascendente(tokens):
    pila = []
    S = 0
    position = 0
    array = 0
    result = "Exito"
    
    while(array < len(tokens)):
        if tokens[array][0] == "SELECT":
            pila.append(0)
            array += 1
        
        elif(pila[position] == 0):          #SELECT
            if tokens[array][0] == "*":
                pila.append(1)
                position +=1
                array +=1
            elif tokens[array][0] == "IDENTIFIER":
                pila.append(2)
                position +=1
                array +=1
            elif tokens[array][0] == "DISTINCT":
                pila.append(5)
                position +=1
                array +=1
            
            
        elif(pila[position] == 1):          #*
            if tokens[array][0] == "FROM":
                pila.append(2)
                position +=1
                array +=1
            
        elif(pila[position] == 2):          #IDENTIFIER D
            if tokens[array][0] == "DOT":
                pila.append(12)
                position +=1
                array +=1
            elif tokens[array][0] == "COMMA":
                pila.append(11)
                position +=1
                array +=1
            elif tokens[array][0] == "FROM":
                pila.pop()
                pila.append(3)
                array +=1
            else:
                return "Error"
                
        elif(pila[position] == 3):          #FROM
            if tokens[array][0] == "IDENTIFIER":
                pila.pop()
                pila.append(4)
                array+=1
            else:
                return "Error"
                
                
        elif(pila[position] == 4):          #IDENTIFIER T
            if tokens[array][0] == "DOT":
                pila.append(22)
                position +=1
                array +=1
            elif tokens[array][0] == "COMMA":
                pila.append(21)
                position +=1
                array +=1
                if(array == len(tokens)):
                    pila.pop()
                    pila.append(100)
                    position-=1
            else:
                return "Error"
            
        elif(pila[position] == 5):          #DISTINCT
            if tokens[array][0] == "IDENTIFIER":
                pila.pop()
                pila.append(2)
            elif tokens[array][0] == "*":
                pila.pop()
                pila.append(1)            
            else:
                return "Error"
                
                
                
            
        elif(pila[position] == 11):         #COMMA D
            if tokens[array][0] == "IDENTIFIER":
                pila.pop()
                pila.pop()
                pila.append(2)
                position -= 1
                array +=1
            else:
                S = -1
            
        elif(pila[position] == 12):         #DOT D
            if tokens[array][0] == "IDENTIFIER":
                pila.pop()
                pila.pop()
                pila.append(2)
                position -= 1
                array +=1
            else:
                S = -1
                
                
                
                
                
                
             
        elif(pila[position] == 21):         #COMMA T
            if tokens[array][0] == "IDENTIFIER":
                pila.pop()
                pila.pop()
                pila.append(4)
                position -= 1
                array +=1
            else:
                S = -1
            
        elif(pila[position] == 22):         #DOT T
            if tokens[array][0] == "IDENTIFIER":
                pila.pop()
                pila.pop()
                pila.append(4)
                position -= 1
                array +=1
            else:
                S = -1
        
        else:
            return "Error"
            
            
            
            
        if S == -1:
            return "Error"
        
    if(pila[position] == 100):
        return "Exito"

    return "Error"

def analizar_cadena():
    while True:
        try:
            cadena = input()
            tokens = analizador_lexico(cadena)
            # for token in tokens:
            #    print("Tokens:", token)
            analisis = analizador_ascendente(tokens)
            print(analisis)
        except EOFError:
            # Fin de la entrada
            break
        except Exception as e:
            print("Error:", str(e))


def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
            tokens = analizador_lexico(contenido)
            analisis = analizador_ascendente(tokens)
            print(analisis)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Error:", str(e))


def main():
    if len(sys.argv) > 1:
        # Si se proporcionan argumentos, asumimos que son nombres de archivos para analizar
        for nombre_archivo in sys.argv[1:]:
            analizar_archivo(nombre_archivo)
    else:
        # Si no se proporcionan argumentos, se inicia el modo interactivo
        analizar_cadena()


if __name__ == "__main__":
    main()
