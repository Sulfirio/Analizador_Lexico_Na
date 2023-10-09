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


def recognize_tokens(input_string):
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

    state = S0
    pos = 0
    token = ""
    comments = []
    comment_start = -1

    while pos < len(input_string):
        char = input_string[pos]
        if state == S0:
            token = ""
            if char == '<':
                state = S1
                token += char
            if char == '>':
                state = S2
                token += char
            if char == '=':
                state = S3
                token += char
            if char == '!':
                state = S4
                token += char
            if char.isnumeric():
                state = S15
                token += char
            if char.isalpha():
                state = S13
                token += char
            if char == '/':
                state = S26
                comment_start = pos
            if char == '"':
                state = S24

            pos += 1

        if state == S1:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "<="][0]
                tokens.append(Token(token_type, "<="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "<"][0]
                tokens.append(Token(token_type, "<"))
                pos += 1
            state = S0

        if state == S2:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == ">="][0]
                tokens.append(Token(token_type, ">="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == ">"][0]
                tokens.append(Token(token_type, ">"))
                pos += 1
            state = S0

        if state == S3:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "=="][0]
                tokens.append(Token(token_type, "=="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "="][0]
                tokens.append(Token(token_type, "="))
                pos += 1
            state = S0

        if state == S4:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "!="][0]
                tokens.append(Token(token_type, "!="))
                pos += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "!"][0]
                tokens.append(Token(token_type, "!"))
                pos += 1  # Corrección: incrementar pos aquí también
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
                if token.lower == keywords[i].lower():
                    tokens.append(Token(keywords[i], token.lower, token.lower))
                    status = 1
                    i = (len(keywords))
            if status == 0:
                tokens.append(Token("IDENTIFIER", token))

        if state == S15:
            state = S22
            if char.isnumeric():
                state = S15
                token += char

            elif char == '.':
                state = S16
                token += char

            elif char == 'E':
                state = S18
                token += char
            pos += 1

        elif state == S16:
            if char.isnumeric():
                state = 17
                token += char

        elif state == S17:
            state = S23
            if char.isnumeric():
                state = S17
                token += char

            elif char == 'E':
                state = S18
                token += char

            pos += 1

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
            state = S21
            if char.isnumeric():
                state = S20
                token += char

            pos += 1
        if state == S21:
            tokens.append(Token("NUMBER", token, int(token)))
            state = 0

        if state == S22:
            tokens.append(Token("NUMBER", token, float(token)))
            state = 0

        if state == S23:
            tokens.append(Token("NUMBER", token, float(token)))
            state = 0
            
        if state == S24:
            if char == '"':
                tokens.append(Token("STRING", token, token))
                state = S0
            else:
                token += char
            pos += 1

        if state == S26:
            if char == '/':
                state = S30
            elif char == '*':
                state = S27
            else:
                state = S32
            pos += 1

        if state == S27:
            if char == '*':
                state = S28
            pos += 1

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

        if state == S30:
            if char == '\n':
                state = S0
                comments.append(input_string[comment_start:pos])
                comment_start = -1
            pos += 1

        if state == S32:
            # Buscar el identificador correspondiente en el diccionario
            token_type = [k for k, v in token_dict.items() if v == "/"][0]
            tokens.append(Token(token_type, "/"))
            state = S0
            comment_start = -1
