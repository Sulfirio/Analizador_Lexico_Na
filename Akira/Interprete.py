import sys

token_dict = {
    "LEFT_PAREN": "(",
    "RIGHT_PAREN": ")",
    "LEFT_BRACE": "{",
    "RIGHT_BRACE": "}",
    "COMMA": ",",
    "DOT": ".",
    "MINUS": "-",
    "PLUS": "+",
    "SEMICOLON": ";",
    "SLASH": "/",
    "STAR": "*",
    "BANG": "!",
    "BANG_EQUAL": "!=",
    "EQUAL": "=",
    "EQUAL_EQUAL": "==",
    "GREATER": ">",
    "GREATER_EQUAL": ">=",
    "LESS": "<",
    "LESS_EQUAL": "<=",
    "IDENTIFIER": "identifier",
    "STRING": "string",
    "NUMBER": "number",
    "AND": "and",
    "ELSE": "else",
    "FALSE": "false",
    "FUN": "fun",
    "FOR": "for",
    "IF": "if",
    "NULL": "null",
    "OR": "or",
    "PRINT": "print",
    "RETURN": "return",
    "TRUE": "true",
    "VAR": "var",
    "WHILE": "while",
    "EOF": "EOF"
}

keywords = [
    "AND", "ELSE", "FALSE", "FUN", "FOR", "IF", "NULL", "OR",
    "PRINT", "RETURN", "TRUE", "VAR", "WHILE"]


def analizador_lexico(input_string):
    tokens = []
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
    S11 = 11
    S12 = 12
    S13 = 13
    S14 = 14
    S15 = 15
    S16 = 16
    S17 = 17
    S18 = 18
    S19 = 19
    S20 = 20
    S21 = 21
    S22 = 22
    S23 = 23
    S24 = 24
    S25 = 25
    S26 = 26
    S27 = 27
    S28 = 28
    S29 = 29
    S30 = 30
    S31 = 31
    S32 = 32
    S34 = 34

    state = S0
    pos = 0
    token = ""
    comments = []
    comment_start = -1
    char_to_token = {v: k for k, v in token_dict.items()}
    tuo = len(input_string)
    #print(tuo)
    while pos < len(input_string):
        char = input_string[pos]
        if state == S0:
            token = ""
            if char == '<':
                state = S1
                pos += 1
            elif char == '>':
                state = S2
                pos += 1
            elif char == '=':
                state = S3
                pos += 1
            elif char == '!':
                state = S4
                pos += 1
            elif char.isspace():
                pos += 1
                continue
            elif char.isnumeric():
                state = S15
            elif char.isalpha():
                state = S13
            elif char == '/':
                state = S26
                comment_start = pos
                pos += 1
                continue
            elif char == '"':
                state = S24
                pos += 1
                continue
            else:
                state = S25

        elif state == S1:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "<="][0]
                tokens.append([token_type, "<="])
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "<"][0]
                tokens.append([token_type, "<"])

            state = S0

        elif state == S2:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == ">="][0]
                tokens.append([token_type, ">="])
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == ">"][0]
                tokens.append([token_type, ">"])

            state = S0

        elif state == S3:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "=="][0]
                tokens.append([token_type, "=="])
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "="][0]
                tokens.append([token_type, "="])

            state = S0

        elif state == S4:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "!="][0]
                tokens.append([token_type, "!="])
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "!"][0]
                tokens.append([token_type, "!"])
                # Corrección: incrementar pos aquí también
            state = S0

        if state == S13:
            if char.isalpha() or char.isnumeric():
                state = S13
                token += char
            else:
                state = 14
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

        if state == S15:
            if char.isnumeric():
                state = S15
                token += char
                pos += 1

            elif char == '.':
                state = S16
                token += char
                pos += 1

            elif char == 'E':
                state = S18
                token += char
                pos += 1
            else:
                state = S22

        elif state == S16:
            if char.isnumeric():
                state = 17

        elif state == S17:
            if char.isnumeric():
                state = S17
                token += char
                pos += 1

            elif char == 'E':
                state = S18
                token += char
                pos += 1
            else:
                state = S23

        elif state == S18:
            if char == '+' or char == '-':
                state = S19
                token += char

            if char.isnumeric():
                state = S20
                token += char

            pos += 1

        elif state == S19:
            if char.isnumeric():
                state = S20
                token += char

            pos += 1

        elif state == S20:
            if char.isnumeric():
                state = S20
                token += char
                pos += 1
            else:
                state = S21
        if state == S21:
            tokens.append(["NUMBER", token, float(token)])
            state = 0

        if state == S22:
            tokens.append(["NUMBER", token, float(token)])
            state = 0

        if state == S23:
            tokens.append(["NUMBER", token, float(token)])
            state = 0

        elif state == S24:
            if char == '"':
                tokens.append(["STRING", token, token])
                state = S0
            elif char == '\n':  # Detectar salto de línea
                print("Error: se detectó un salto de línea dentro de una cadena")
                break
            else:
                token += char
            pos += 1

        if state == S25:
            if char in char_to_token:
                tokens.append([char_to_token[char], char])
                state = S0
            pos += 1

        elif state == S26:
            if char == '/':
                state = S30
            elif char == '*':
                state = S27
            else:
                state = S32
                continue
            pos += 1
            continue

        if state == S27:
            if char == '*':
                state = S28
            pos += 1
            continue

        if state == S28:
            if char == '/':
                state = S0
                comments.append(input_string[comment_start:pos + 1])
                comment_start = -1
            elif char == '*':
                # Nos mantenemos en S28
                pass
            else:
                state = S27
            pos += 1
            continue

        elif state == S30:
            if char == '\n' or pos == len(input_string) - 1:
                state = S0
                if char != '\n':  # Si el comentario no termina con un salto de línea, incluir el último caracter
                    pos += 1
                comments.append(input_string[comment_start:pos])
                comment_start = -1
            pos += 1
            continue
        if state == S32:
            # Buscar el identificador correspondiente en el diccionario
            token_type = [k for k, v in token_dict.items() if v == "/"][0]
            tokens.append([token_type, "/"])
            state = S0
            comment_start = -1
            continue
    # Manejo del último token, si es que hay uno en construcción
    if token:
        if state == S15 or state == S17 or state == S20:
            tokens.append(["NUMBER", token, float(token)])
        elif state == S13:
            tokens.append(["IDENTIFIER", token])
        else:
            raise ValueError(f"Token incompleto al final de la cadena: {token}")

    return tokens, comments


def analizar_cadena():
    while True:
        try:
            cadena = input()
            tokens, comments = analizador_lexico(cadena)
            for token in tokens:
                print("Tokens:", token)
            for token in comments:
                print("Comentarios:", token)
        except EOFError:
            # Fin de la entrada
            break
        except Exception as e:
            print("Error:", str(e))


def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
            tokens, comments = analizador_lexico(contenido)
            print("Tokens:", tokens)
            print("Comentarios:", comments)
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
