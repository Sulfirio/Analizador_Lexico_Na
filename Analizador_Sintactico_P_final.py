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

pos = 0
Tokens = []

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
    print(tuo)
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

    return tokens


def analizar_cadena():
    while True:
        try:
            cadena = input()
            tokens, comments = analizador_lexico(cadena)
            for token in tokens:
                print("Tokens:", token)
            #for token in comments:
            #    print("Comentarios:", token)
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
            #print("Comentarios:", comments)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Error:", str(e))

# Seccion declaration

def declaration():
    token = []
    result = funDecl()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = declaration()
        if (result2[0] == True):
            token.append(result2[1])
        return [True, ["Declaration", token]]
    else:
        result = varDecl()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
            result2 = declaration()
            if (result2[0] == True):
                token.append(result2[1])
            return [True, ["Declaration", token]]
        else:
            result = statement()
            if (result[0] == True):
                token.append(result[1])
                pos += 1
                result2 = declaration()
                if (result2[0] == True):
                    token.append(result2[1])
                return [True, ["Declaration", token]]
            else:
                return [False, []]


def funDecl():
    token = []
    if (Tokens[pos][0] == "FUN"):
        token.append(Tokens[pos][0])
        pos += 1
        result = funct()
        if (result[0] == True):
            token.append(result[1])
            return [True, ["FunDecl", token]]
        else:
            return [False, []]
    else:
        return [False, []]


def varDecl():
    token = []
    if (Tokens[pos][0] == "VAR"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "IDENTIFIER"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result = varInit()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
        else:
            return [False, []]
        return [True, ["VarDecl", token]]

    else:
        return [False, []]


def varInit():
    token = []
    if (Tokens[pos][0] == "EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == 1):
            token.append(result[1])
            return [True, ["VarInit", token]]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion statement

def statement():
    result = exprStm()
    if (result[0] == True):
        return [True, ["Statement", result[1]]]
    else:
        result = forStm()
        if (result[0] == True):
            return [True, ["Statement", result[1]]]
        else:
            result = ifStm()
            if (result[0] == True):
                return [True, ["Statement", result[1]]]
            else:
                result = printStm()
                if (result[0] == True):
                    return [True, ["Statement", result[1]]]
                else:
                    result = returnStm()
                    if (result[0] == True):
                        return [True, ["Statement", result[1]]]
                    else:
                        result = whileStm()
                        if (result[0] == True):
                            return [True, ["Statement", result[1]]]
                        else:
                            result = block()
                            if (result[0] == True):
                                return [True, ["Statement", result[1]]]
                            else:
                                return [False, []]


def exprStm():
    token = []
    result = Expression()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
            return [True, ["exprStm", token]]
        else:
            return [False, []]

    else:
        return [False, []]


# Seccion For

def forStm():
    token = []
    if (Tokens[pos][0] == "FOR"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "LEFT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result = forStm1()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]

        result2 = forStm2()
        if (result2[0] == True):
            token.append(result2[1])
            pos += 1
        else:
            return [False, []]

        result3 = forStm3()
        if (result3[0] == True):
            token.append(result3[1])
            pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result4 = statement()
        if (result4[0] == True):
            token.append(result4[1])
        else:
            return [False, []]
        return [True, ["ForStm", token]]
    else:
        return [False, []]


def forStm1():
    token = []
    result = varDecl()
    result2 = exprStm()
    if (result[0] == True):
        token.append(result[1])
        return [True, ["ForStm1", token]]
    elif (result2[0] == True):
        token.append(result2[1])
        return [True, ["ForStm1", token]]
    elif (Tokens[pos][0] == "SEMICOLON"):
        token.append(Tokens[pos][0])
        return [True, ["ForStm1", token]]
    else:
        return [False, []]


def forStm2():
    token = []
    result = Expression()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
        else:
            return [False, []]
        return [True, ["ForStm2", token]]
    elif (Tokens[pos][0] == "SEMICOLON"):
        return [True, ["ForStm2", Tokens[pos][0]]]
    else:
        return [False, []]


def forStm3():
    result = Expression()
    if (result[0] == True):
        return [True, ["ForStm3"], result[1]]


# Seccion While

def whileStm():
    token = []
    if (Tokens[pos][0] == "WHILE"):
        token.append(token[pos][0])
        pos += 1
        if (Tokens[pos][0] == "LEFT_PAREN"):
            token.append(token[pos][0])
            pos += 1
            result = Expression()
            if (result[0] == True):
                token.append(result[1])
                pos += 1
            result2 = whileStm()
            if (result2[0] == True):
                token.append(result2[1])
                pos += 1
            return [True, ["WhileStm", token]]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion if

def ifStm():
    token = []
    if (Tokens[pos][0] == "IF"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "LEFT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result2 = statement()
        if (result2[0] == True):
            token.append(result2[1])
            pos += 1
        else:
            return [False, []]
        result3 = elseStm()
        if (result3 == True):
            token.append(result3[1])
        return [True, ["ForStm", token]]

    else:
        return [False, []]


def elseStm():
    token = []
    if (Tokens[pos][0] == "ELSE"):
        token.append(Tokens[pos][0])
        pos += 1
        result = statement()
        if (result[0] == True):
            token.append(result[1])
            return [True, ["ElseStm", token]]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion Print

def printStm():
    token = []
    if (Tokens[pos][0] == "PRINT"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
            return [True, ["ElseStm", token]]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion Return

def returnStm():
    token = []
    if (Tokens[pos][0] == "RETURN"):
        token.append(Tokens[pos][0])
        pos += 1
        result = returnOpc()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
            return [True, ["ReturnStm", token]]
        else:
            return [False, []]
    else:
        return [False, []]


def returnOpc():
    result = Expression()
    if (result[0] == True):
        return [True, ["ReturnOpc", result[1]]]
    return [False, []]


# Seccion Expression

def Expression():
    result = assignment()
    if (result[0] == True):
        return [True, ["Expresion", result[1]]]
    else:
        return [False, []]


# Seccion Assignment

def assignment():
    token = []
    result = exprOr()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = assignmentOpc()
        if (result2[0] == True):
            token.append(result2[1])
        return [True, ["Assignment", result[1]]]
    else:
        return [False, []]


def assignmentOpc():
    token = []
    if (Tokens[pos][0] == "EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
        else:
            return [False, []]
        return [True, ["AssigmentOpc", token]]
    else:
        return [False, []]


# Seccion logica or

def exprOr():
    token = []
    result = exprAnd()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = exprOr2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprOr", token]]
        else:
            return [True, ["ExprOr", token]]
    else:
        return [False, []]


def exprOr2():
    token = []
    if (Tokens[pos][0] == "OR"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprAnd()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        result2 = exprOr2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprOr2", token]]
        else:
            return [True, ["ExprOr2", token]]
    else:
        return [False, []]


# Seccion Logica and

def exprAnd():
    token = []
    result = exprEquality()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = exprAnd2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprAnd", token]]
        else:
            return [True, ["ExprAnd", token]]
    else:
        return [False, []]


def exprAnd2():
    token = []
    if (Tokens[pos][0] == "AND"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprEquality()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        result2 = exprAnd2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprAnd2", token]]
        else:
            return [True, ["ExprAnd2", token]]
    else:
        return [False, []]


# Seccion EQUALITY
def exprEquality():
    token = []
    result = exprComp()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = exprEquality2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprEquality", token]]
        else:
            return [True, ["ExprEquality", token]]
    else:
        return [False, []]


def exprEquality2():
    token = []
    if (Tokens[pos][0] == "BANG_EQUAL" | Tokens[pos][0] == "EQUAL_EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprComp()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        result2 = exprEquality2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprEquality2", token]]
        else:
            return [True, ["ExprEquality2", token]]
    else:
        return [False, []]


# Seccion COMPARSION
def exprComp():
    token = []
    result = exprTerm()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = exprComp2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprComp", token]]
        else:
            return [True, ["ExprComp", token]]
    else:
        return [False, []]


def exprComp2():
    token = []
    if (Tokens[pos][0] == "GREATER" | Tokens[pos][0] == "GREATER_EQUAL" | Tokens[pos][0] == "LESS" | Tokens[pos][
        0] == "LESS_EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprTerm()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        result2 = exprComp2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprComp2", token]]
        else:
            return [True, ["ExprComp2", token]]
    else:
        return [False, []]


# Seccion Term
def exprTerm():
    token = []
    result = factor()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = term2()
        if (result2[0] == True):
            token.append(result2[1])
        return [True, ["ExprTerm", token]]
    else:
        return [False, []]


def term2():
    token = []
    if (Tokens[pos][0] == "MINUS" | Tokens[pos][0] == "PLUS"):
        token.append(Tokens[pos][0])
        pos += 1
        result = factor()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        result2 = term2()
        if (result2[0] == True):
            token.append(result2[1])
        return [True, ["Term2", token]]
    else:
        return [False, []]


def factor():
    token = []
    result = exprUnary()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = factor2()
        if (result2[0] == True):
            token.append(result2[1])
        return [True, ["Factor", token]]
    else:
        return [False, []]


def factor2():
    token = []
    if (Tokens[pos][0] == "STAR" | Tokens[pos][0] == "SLASH"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprUnary()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        else:
            return [False, []]
        result2 = factor2()
        if (result2[0] == True):
            token.append(result2[1])
        return [True, ["Factor2", token]]
    else:
        return [False, []]


# Seccion Unary

def exprUnary():
    token = []
    if (Tokens[pos][0] == "BANG" | Tokens[pos][0] == "MINUS"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprUnary()
        if (result[0] == True):
            token.append(result[1])
            return [True, ["ExprUnary", token]]
        else:
            return [False, []]
    elif (Tokens[pos][0] == "TRUE" | Tokens[pos][0] == "FALSE" | Tokens[pos][0] == "NULL" | Tokens[pos][0] == "NUMBER" |
          Tokens[pos][0] == "STRING" | Tokens[pos][0] == "IDENTIFIER" | Tokens[pos][0] == "LEFT_PAREN"):
        result = exprCall()
        token.append(result[1])
        if (result[0] == True):
            return [True, ["ExprUnary", token]]
    else:
        return [False, []]
    return [False, []]


def exprCall():
    token = []
    if (Tokens[pos][0] == "TRUE" | Tokens[pos][0] == "FALSE" | Tokens[pos][0] == "NULL" | Tokens[pos][0] == "NUMBER" |
            Tokens[pos][0] == "STRING" | Tokens[pos][0] == "IDENTIFIER" | Tokens[pos][0] == "LEFT_PAREN"):
        result = exprPrimary()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
            result2 = exprCall2()
            if (result2[0] == True):
                token.append(result2[1])
                return [True, ["ExprCall", token]]
            else:
                return [True, ["ExprCall", token]]
        else:
            return [False, []]
    else:
        return [False, []]

    return [False, []]


def exprCall2():
    token = []
    if (Tokens[pos][0] == "LEFT_PAREN"):
        token.append(Tokens[pos][0])
        pos += 1
        result = argOpc()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result2 = exprCall2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ExprCall2", token]]
        else:
            return [True, ["ExprCall2", token]]
    return [False, []]


def exprPrimary():
    token = []
    if (Tokens[pos][0] == "TRUE" | Tokens[pos][0] == "FALSE" | Tokens[pos][0] == "NULL" | Tokens[pos][0] == "NUMBER" |
            Tokens[pos][0] == "STRING" | Tokens[pos][0] == "IDENTIFIER"):
        return [True, ["ExprPrimary", Tokens[pos][0]]]
    elif (Tokens[pos][0] == "LEFT_PAREN"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
            if (Tokens[pos][0] == "RIGHT_PAREN"):
                Tokens.append(Tokens[pos][0])
                return [True, ["ExprPrimary", token]]
            else:
                return [False, []]
    return [False, []]


# Seccion Argumentos

def argOpc():
    token = []
    result = Expression()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = arguments()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, ["ArgOpc", token]]
        else:
            return [True, ["ArgOpc", token]]
    else:
        return [False, []]
    return [False, []]


def arguments():
    token = []
    if (Tokens[pos][0] == "COMMA"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        result2 = Expression()
        if (result2[0] == True):
            token.append(result2[1])
            pos += 1
        return [True, ["Arguments", token]]
    else:
        return [False, []]


# Seccion Functions

def funct():
    token = []
    if (Tokens[pos][0] == "IDENTIFIER"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "LEFT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result = paramOpc()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result2 = block()
        if (result2[0] == True):
            token.append(result2[1])
            pos += 1
            return [True, ["Function", token]]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion parameters

def paramOpc():
    token = []
    if (Tokens[pos][0] == "IDENTIFIER"):
        result = parameters()
        if (result[0] == True):
            token.append(result[1])
        return [True, ["ParametersOpc", token]]
    else:
        return [False, []]


def parameters():
    token = []
    if (Tokens[pos][0] == "IDENTIFIER"):
        token.append(Tokens[pos][0])
        pos += 1
        result = parameters2()
        if (result[0] == True):
            token.append(result[1])
        else:
            return [False, []]
        return [True, ["Parameters", token]]
    else:
        return [False, []]


def parameters2():
    token = []
    if (Tokens[pos][0] == "COMMA"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "IDENTIFIER"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result = parameters2
        if (result[0] == True):
            token.append(result[1])
        else:
            return [False, []]
        return [True, ["Parameters_2", token]]
    else:
        return [True, [""]]
    return [False, []]


# Seccion block

def block():
    token = []
    if (Tokens[pos][0] == "LEFT_BRACE"):
        token.append(Tokens[pos][0])
        pos += 1
        result = declaration()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
        if (Tokens[pos][0] == "LEFT_BRACE"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
    else:
        return [False, []]



def main():
    program = declaration()
    if (program == True):
        print("Compilado")
    else:
        print("Error en el codigo")

    if len(sys.argv) > 1:
        # Si se proporcionan argumentos, asumimos que son nombres de archivos para analizar
        for nombre_archivo in sys.argv[1:]:
            analizar_archivo(nombre_archivo)
    else:
        # Si no se proporcionan argumentos, se inicia el modo interactivo
        analizar_cadena()

    return 0

if __name__ == "__main__":
    main()
