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


def recognize_comments_v7(input_string, token_dict):
    # Definimos los estados
    S0 = 0
    S26 = 1
    S30 = 2
    S27 = 3
    S28 = 4
    S32 = 5

    state = S0
    pos = 0
    comments = []
    tokens = []
    comment_start = -1

    while pos < len(input_string):
        char = input_string[pos]

        # Estado inicial (S0)
        if state == S0:
            if char == '/':
                state = S26
                comment_start = pos
            pos += 1

        # Estado S26
        elif state == S26:
            if char == '/':
                state = S30
            elif char == '*':
                state = S27
            else:
                state = S32
            pos += 1

        # Estado S30 (comentario de línea única)
        elif state == S30:
            if char == '\n':
                state = S0
                comments.append(input_string[comment_start:pos])
                comment_start = -1
            pos += 1

        # Estado S27 (comienzo de comentario de múltiples líneas)
        elif state == S27:
            if char == '*':
                state = S28
            pos += 1

        # Estado S28
        elif state == S28:
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

        # Estado S32
        elif state == S32:
            # Buscar el identificador correspondiente en el diccionario
            token_type = [k for k, v in token_dict.items() if v == "/"][0]
            tokens.append(Token(token_type, "/"))
            state = S0
            comment_start = -1

    return comments, tokens


# Ejemplo de uso
test_string_v7 = """
int x = 10 / 5; // This is a single-line comment
a<=b!=c==d>e>=f<g!h=1
/* This is a 
multi-line comment */
int y = 20;
"""

comments, tokens = recognize_comments_v7(test_string_v7, token_dict)

# Imprimir los comentarios y tokens encontrados
print("Comentarios encontrados:")
for comment in comments:
    print(comment)

print("\nTokens encontrados:")
for token in tokens:
    print(f"Type={token.type}, Value={token.value}")
