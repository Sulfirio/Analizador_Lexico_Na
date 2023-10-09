# Revisando y corrigiendo el código
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.literal = None


# Diccionario de tokens
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


def recognize_relational_operators_v8(input_string):
    # Definir los estados
    S0 = 0  # Estado inicial
    S1 = 1  # <
    S2 = 2  # >
    S3 = 3  # =
    S4 = 4  # !

    state = S0  # Estado actual
    pos = 0  # Posición actual en la cadena de entrada
    tokens = []  # Lista de tokens reconocidos

    while pos < len(input_string):
        char = input_string[pos]

        # Estado inicial (S0)
        if state == S0:
            if char == '<':
                state = S1
            elif char == '>':
                state = S2
            elif char == '=':
                state = S3
            elif char == '!':
                state = S4
            pos += 1

        # Estado S1 (< leído)
        elif state == S1:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "<="][0]
                tokens.append(Token(token_type, "<="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "<"][0]
                tokens.append(Token(token_type, "<"))
                pos += 1  # Corrección: incrementar pos aquí también
            state = S0

        # Estado S2 (> leído)
        elif state == S2:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == ">="][0]
                tokens.append(Token(token_type, ">="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == ">"][0]
                tokens.append(Token(token_type, ">"))
                pos += 1  # Corrección: incrementar pos aquí también
            state = S0

        # Estado S3 (= leído)
        elif state == S3:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "=="][0]
                tokens.append(Token(token_type, "=="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "="][0]
                tokens.append(Token(token_type, "="))
                pos += 1  # Corrección: incrementar pos aquí también
            state = S0

        # Estado S4 (! leído)
        elif state == S4:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "!="][0]
                tokens.append(Token(token_type, "!="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "!"][0]
                tokens.append(Token(token_type, "!"))
                pos += 1  # Corrección: incrementar pos aquí también
            state = S0

    return tokens


# Ejecutando el código con la cadena de prueba y verificando los tokens reconocidos
test_string = """
*a<=b!= c==d >e>=f<g!h=1
! > =
"""
tokens = recognize_relational_operators_v8(test_string)


def print_tokens_v2(tokens):
    print("Tokens reconocidos:")
    print(f"{'Token Type':<15} {'Value':<10}")
    print("-" * 25)
    for token in tokens:
        print(f"{token.type:<15} {token.value:<10}")


print_tokens_v2(tokens)
