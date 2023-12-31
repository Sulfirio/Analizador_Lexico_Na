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
    size = len(input_string)
    while pos < len(input_string):
        char = input_string[pos]
        print("Se analiza el character: ", char)
        print("Estamos en estado:", state)
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
            if (pos + 1) >= size:
                tokens.append(["IDENTIFIER", token])
                return tokens
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


def analizador_descendente(tokens):
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S5 = 5
    S6 = 6
    S7 = 7
    S8 = 8
    S9 = 9
    S10 = 10

    SA = -1

    S = 0


    result = "Exito"
    for token in tokens:
        #print("Estamos en estado:", S)
        #print("Estamos analizando:", token[0])
        if S == S0:
            if token[0] == "SELECT":
                S = S1
            else:
                S = SA
        elif S == S1:
            if token[0] == "ASTERIC":
                S = S2
            elif token[0] == "DISTINCT":
                S = S3
            elif token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA


        elif S == S2:
            if token[0] == "FROM":
                S = S5
            else:
                S = SA


        elif S == S3:
            if token[0] == "*":
                S = S2
            elif token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA


        elif S == S4:
            if token[0] == "COMMA":
                S = S6
            elif token[0] == "DOT":
                S = S7
            elif token[0] == "FROM":
                S = S5
            else:
                S = SA


        elif S == S5:
            if token[0] == "IDENTIFIER":
                S = S8
            else:
                S = SA


        elif S == S6:
            if token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA


        elif S == S7:
            if token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA


        elif S == S8:
            if token[0] == "COMMA":
                S = S9
            elif token[0] == "DOT":
                S = S10
            else:
                S = SA


        elif S == S9:
            if token[0] == "IDENTIFIER":
                S = S8
            else:
                S = SA


        elif S == S10:
            if token[0] == "IDENTIFIER":
                S = S8
            else:
                S = SA

        if S == SA:
            return "Error"

    return result


def analizar_cadena():
    while True:
        try:
            cadena = input()
            tokens = analizador_lexico(cadena)
            # for token in tokens:
            #    print("Tokens:", token)
            analisis = analizador_descendente(tokens)
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
            analisis = analizador_descendente(tokens)
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
