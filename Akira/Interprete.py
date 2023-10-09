import sys


class Token:
    def __init__(self, token_type, value, literal=None):
        self.type = token_type
        self.value = value
        self.literal = literal


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


def analizador_lexico(cadena):
    # Implementación del analizador léxico aquí
    tokens = []
    # ...
    return tokens


def analizar_cadena():
    while True:
        try:
            cadena = input()
            tokens = analizador_lexico(cadena)
            print("Tokens:", tokens)
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
            print("Tokens:", tokens)
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
