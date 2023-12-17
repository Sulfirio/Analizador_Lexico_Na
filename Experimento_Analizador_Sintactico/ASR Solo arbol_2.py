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
    position = 0
    token = ""
    comments = []
    comment_start = -1
    char_to_token = {v: k for k, v in token_dict.items()}
    tuo = len(input_string)
    #print(tuo)
    while position < len(input_string):
        char = input_string[position]
        if state == S0:
            token = ""
            if char == '<':
                state = S1
                position += 1
            elif char == '>':
                state = S2
                position += 1
            elif char == '=':
                state = S3
                position += 1
            elif char == '!':
                state = S4
                position += 1
            elif char.isspace():
                position += 1
                continue
            elif char.isnumeric():
                state = S15
            elif char.isalpha():
                state = S13
            elif char == '/':
                state = S26
                comment_start = position
                position += 1
                continue
            elif char == '"':
                state = S24
                position += 1
                continue
            else:
                state = S25

        elif state == S1:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "<="][0]
                tokens.append([token_type, "<="])
                position += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "<"][0]
                tokens.append([token_type, "<"])

            state = S0

        elif state == S2:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == ">="][0]
                tokens.append([token_type, ">="])
                position += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == ">"][0]
                tokens.append([token_type, ">"])

            state = S0

        elif state == S3:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "=="][0]
                tokens.append([token_type, "=="])
                position += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "="][0]
                tokens.append([token_type, "="])

            state = S0

        elif state == S4:
            if char == '=':
                token_type = [k for k, v in token_dict.items() if v == "!="][0]
                tokens.append([token_type, "!="])
                position += 1
            else:
                token_type = [k for k, v in token_dict.items() if v == "!"][0]
                tokens.append([token_type, "!"])
                # Corrección: incrementar position aquí también
            state = S0

        if state == S13:
            if char.isalpha() or char.isnumeric():
                state = S13
                token += char
            else:
                state = 14
            position += 1

        if state == S14:
            status = 0
            for i in range(len(keywords)):
                if token == (keywords[i].lower()):
                    tokens.append([keywords[i], token])
                    status = 1
            if status == 0:
                tokens.append(["IDENTIFIER", token])
            state = S0
            position -= 1

        if state == S15:
            if char.isnumeric():
                state = S15
                token += char
                position += 1

            elif char == '.':
                state = S16
                token += char
                position += 1

            elif char == 'E':
                state = S18
                token += char
                position += 1
            else:
                state = S22

        elif state == S16:
            if char.isnumeric():
                state = 17

        elif state == S17:
            if char.isnumeric():
                state = S17
                token += char
                position += 1

            elif char == 'E':
                state = S18
                token += char
                position += 1
            else:
                state = S23

        elif state == S18:
            if char == '+' or char == '-':
                state = S19
                token += char

            if char.isnumeric():
                state = S20
                token += char

            position += 1

        elif state == S19:
            if char.isnumeric():
                state = S20
                token += char

            position += 1

        elif state == S20:
            if char.isnumeric():
                state = S20
                token += char
                position += 1
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
            position += 1

        if state == S25:
            if char in char_to_token:
                tokens.append([char_to_token[char], char])
                state = S0
            position += 1

        elif state == S26:
            if char == '/':
                state = S30
            elif char == '*':
                state = S27
            else:
                state = S32
                continue
            position += 1
            continue

        if state == S27:
            if char == '*':
                state = S28
            position += 1
            continue

        if state == S28:
            if char == '/':
                state = S0
                comments.append(input_string[comment_start:position + 1])
                comment_start = -1
            elif char == '*':
                # Nos mantenemos en S28
                pass
            else:
                state = S27
            position += 1
            continue

        elif state == S30:
            if char == '\n' or position == len(input_string) - 1:
                state = S0
                if char != '\n':  # Si el comentario no termina con un salto de línea, incluir el último caracter
                    position += 1
                comments.append(input_string[comment_start:position])
                comment_start = -1
            position += 1
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

def print_ast(node, path=''):
    if isinstance(node, list):
        if len(node) == 1:
            # Si hay un solo elemento hijo, continuamos con la misma línea
            print_ast(node[0], path)
        else:
            for sub_node in node:
                # Si hay varios elementos hijos, iniciamos una nueva línea para cada uno
                print_ast(sub_node, path + ' -> ')
    else:
        # Imprimir la rama completa cuando llegamos a una hoja
        print(path + str(node))

def analizar_cadena():
    global pos
    global Tokens
    while True:
        try:
            cadena = input()
            tokens = analizador_lexico(cadena)
            """for token in tokens:
                print("Tokens:", token)
                """
            # for token in comments:
            #    print("Comentarios:", token)
            Tokens = tokens
            pos= 0
            program = declaration()
            print_ast(program[1])
            if (program[0] == True):
                print("Compilado")
            else:
                print("Error en el codigo")
        except EOFError:
            # Fin de la entrada
            break
        #except Exception as e:
        #    print("Error:", str(e))


def analizar_archivo(nombre_archivo):
    global pos
    global Tokens
    try:
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
            tokens = analizador_lexico(contenido)
            aux=0
            """for token in tokens:
                print("Tokens:", token, " Posicion:",aux)
                aux+=1
            """
            Tokens = tokens
            pos=0
            program = declaration()
            print_ast(program[1])
            if (program[0] == True):
                print("Compilado")
            else:
                print("Error en el codigo")
            # print("Comentarios:", comments)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    #except Exception as e:
    #    print("Error:", str(e))


# Seccion declaration

def declaration():
    global pos
    global Tokens
    if(pos>=len(Tokens)):
        return [False, []]
    if (Tokens[pos][0] == "SEMICOLON" or Tokens[pos][0] == "RIGHT_BRACE"):
        return [False, []]
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en declaration")
    if (pos > 0):
        if(Tokens[pos-1][0] == "PRINT" or Tokens[pos-1][0] == "IF" or Tokens[pos-1][0] == "FUN" or Tokens[pos-1][0] == "VAR" or Tokens[pos-1][0] == "FOR" or Tokens[pos-1][0] == "RETURN" or Tokens[pos-1][0] == "WHILE"):
            pos -= 1
    token = []
    result = varDecl()
    if (result[0] == True):
        token.append(result[1])
        if (pos + 1 < len(Tokens)):
            pos += 1
        #print("\n\n\naqui1\n\n\n")
        #print([True, ["Declaration", token]])
        result2 = declaration()
        if (result2[0] == True):
            token.append(result2[1])
        #print([True, ["Declaration", token]])
        if(pos+1<len(Tokens)):
            pos+=1
        #print(["Variable Declaration", token],"\n")
        return [True,  token]
    else:
        result = statement()
        if (result[0] == True):
            token.append(result[1])
            if (pos + 1 < len(Tokens)):
                pos += 1
            result2 = declaration()
            if (result2[0] == True):
                token.append(result2[1])
            return [True,  token]
        else:
            result = funDecl()
            if (result[0] == True):
                token.append(result[1])
                #if(pos+1<len(Tokens)):
                    #pos += 1
                    #print("\ntenemos",Tokens[pos][0],"\n")
                result2 = declaration()
                if (result2[0] == True):
                    token.append(result2[1])
                #print(["Function Declaration", token],"\n")
                return [True, ["Function Declaration", token]]
            else:
                return [False, []]


def funDecl():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en funDecl")
    token = []
    if (Tokens[pos][0] == "FUN"):
        token.append(Tokens[pos][0])
        pos += 1
        result = funct()
        if (result[0] == True):
            token.append(result[1])
            return [True,token]
        else:
            return [False, []]
    else:
        return [False, []]


def varDecl():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en varDecl")
    token = []
    if (Tokens[pos][0] == "VAR"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "IDENTIFIER"):
            token.append(Tokens[pos])
            pos += 1
        else:
            return [False, []]
        result = varInit()
        if (result[0] == True):
            token.append(result[1])
            #print("\nEstamos en",pos, "que tiene el valor:", Tokens[pos])
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
        else:
            return [False, []]
        return [True, ["Variable Declaration",token]]

    else:
        return [False, []]


def varInit():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en varInit")
    token = []
    if (Tokens[pos][0] == "EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        #print("\nllegamos\n")
        result = Expression()
        if (result[0] == 1):
            token.append(result[1])
            #print([True, ["Varinit", token]])
            return [True,  token]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion statement

def statement():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en statement")
    result = exprStm()
    if (result[0] == True):
        print(["Expression Statement", result[1]],"\n")
        return [True, ["Expression Statement", result[1]]]
    else:
        result = forStm()
        if (result[0] == True):
            #print(["Loop Statement", result[1]],"\n")
            return [True, ["Loop Statement", result[1]]]
        else:
            result = ifStm()
            if (result[0] == True):
                #print(["Conditional Statement", result[1]],"\n")
                return [True, ["Conditional Statement", result[1]]]
            else:
                result = printStm()
                if (result[0] == True):
                    #print(["Print Statement", result[1]],"\n")
                    return [True, ["Print Statement", result[1]]]
                else:
                    result = returnStm()
                    if (result[0] == True):
                        #print(["Return Statement", result[1]],"\n")
                        return [True, ["Return Statement", result[1]]]
                    else:
                        result = whileStm()
                        if (result[0] == True):
                            #print(["Loop Statement", result[1]],"\n")
                            return [True, ["Loop Statement", result[1]]]
                        else:
                            result = block()
                            if (result[0] == True):
                                #print(["Block", result[1]],"\n")
                                return [True, result[1]]
                            else:
                                return [False, []]


def exprStm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprStm")
    token = []
    result = Expression()
    if (result[0] == True):
        token.append(result[1])
        if(pos+1<len(Tokens)):
            if(Tokens[pos+1][0]=="SEMICOLON"):
                pos += 1
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
            return [True,  token]
        else:
            return [False, []]

    else:
        return [False, []]


# Seccion For

def forStm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en forStm")
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
            #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
            pos += 1
        else:
            return [False, []]

        result2 = forStm2()

        if (result2[0] == True):
            #print("aqui")
            token.append(result2[1])
            pos -= 1
        else:
            return [False, []]

        result3 = forStm3()

        if (result3[0] == True):

            token.append(result3[1])
        else:
            pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            #print("TESTING")
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result4 = statement()
        if (result4[0] == True):
            token.append(result4[1])
            pos += 1

        else:
            return [False, []]
        return [True,token]
    else:
        return [False, []]


def forStm1():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en forStm1")
    token = []
    result = varDecl()
    result2 = exprStm()
    if (result[0] == True):
        token.append(result[1])
        #print("aqui2")
        return [True, token]
    elif (result2[0] == True):
        token.append(result2[1])
        #print("aqui2")
        return [True, token]
    elif (Tokens[pos][0] == "SEMICOLON"):
        token.append(Tokens[pos][0])
        #print("aqui2")
        return [True, token]
    else:
        return [False, []]


def forStm2():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en forStm2")
    token = []
    if (Tokens[pos][0] == "SEMICOLON"):
        pos+=1
        return [True, Tokens[pos][0]]
    result = Expression()

    if (result[0] == True):
        token.append(result[1])
        pos += 2
        """if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
        else:
            return [False, []]"""
        return [True, token]

    else:
        return [False, []]


def forStm3():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en forStm3")
    result = Expression()
    if (result[0] == True):
        return [True, result[1]]

    return [False, []]


# Seccion While

def whileStm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en whileStm")
    token = []
    if (Tokens[pos][0] == "WHILE"):
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "LEFT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
            result = Expression()
            if (result[0] == True):
                token.append(result[1])
                pos += 1
            result2 = block()
            if (result2[0] == True):
                token.append(result2[1])
                pos += 1
            return [True, token]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion if

def ifStm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos ifStm")
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
            #pos += 1
            #print("Prueba18\n")
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result2 = block()
        #print(result2)
        if (result2[0] == True):
            token.append(result2[1])
            pos += 1
            if(Tokens[pos][0]=="PRINT"):
                #print("PRUEBAAAAA\n")
                pos-=1
        else:
            return [False, []]
        result3 = elseStm()
        if (result3[0] == True):
            token.append(result3[1])
        return [True, token]

    else:
        return [False, []]


def elseStm():
    global pos
    global Tokens
    if(pos>=len(Tokens)):
        return [False, []]
    #print("\nEstamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos elseStm\n")
    token = []
    if (Tokens[pos][0] == "ELSE"):
        token.append(Tokens[pos][0])
        pos += 1
        result = block()
        if (result[0] == True):
            token.append(result[1])
            return [True,  token]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion Print

def printStm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos printStm")
    token = []
    if (Tokens[pos][0] == "PRINT"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
            #pos += 1
        else:
            return [False, []]
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
            return [True, token]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion Return

def returnStm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos returnStm")
    token = []
    if (Tokens[pos][0] == "RETURN"):
        token.append(Tokens[pos][0])
        pos += 1
        result = returnOpc()
        if (result[0] == True):
            token.append(result[1])
            #pos += 1
        if (Tokens[pos][0] == "SEMICOLON"):
            token.append(Tokens[pos][0])
            return [True, token]
        else:
            return [False, []]
    else:
        return [False, []]


def returnOpc():
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos returnOpc")
    result = Expression()
    if (result[0] == True):
        return [True, result[1]]
    return [False, []]


# Seccion Expression

def Expression():
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos Expression")
    result = assignment()
    if (result[0] == True):
        #print([True, ["Expresion", result[1]]])
        return [True, result[1]]
    else:
        return [False, []]


# Seccion Assignment

def assignment():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en assignment")
    token = []
    result = exprOr()
    if (result[0] == True):
        token.append(result[1])
        if(Tokens[pos][0] == "SEMICOLON" or Tokens[pos][0]== "RIGHT_PAREN" or Tokens[pos][0]== "RIGHT_BRACE"):
            return [True, token]
        pos += 1
        result2 = assignmentOpc()
        if (result2[0] == True):
            token.append(result2[1])
            #print (["Assignment", token],"\n")
            return [True, ["Expression Binary", token]]
        return [True,token]
    else:
        return [False, []]


def assignmentOpc():
    global pos
    global Tokens
    if(pos+1 >= len(Tokens)):
        return [False,[]]
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en assignmentOpc")
    token = []
    if(pos>=len(Tokens)):
        pos-=1
        return [False, []]
    if(pos+1>=len(Tokens)):
        return [False, []]
    if (Tokens[pos+1][0] == "EQUAL"):
        pos += 1
    if (Tokens[pos][0] == "EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
        else:
            #print("falso")
            return [False, []]
        return [True, token]
    else:
        #print("falso")
        return [False, []]


# Seccion logica or

def exprOr():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprOr")
    token = []
    result = exprAnd()
    if (result[0] == True):
        token.append(result[1])
        #pos += 1
        result2 = exprOr2()
        if (result2[0] == True):
            token.append(result2[1])
            #print(["Expression Logic", token],"\n")
            return [True, ["Expression Logic", token]]
        else:
            return [True,  token]
    else:
        return [False, []]


def exprOr2():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en  exprOr2")
    if(pos+1 >= len(Tokens)):
        return [False,[]]
    token = []
    if (Tokens[pos+1][0] == "OR"):
        pos+=1
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
            return [True, token]
        else:
            return [True, token]
    else:
        return [False, []]


# Seccion Logica and

def exprAnd():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprAnd")
    token = []
    result = exprEquality()
    if (result[0] == True):
        token.append(result[1])
        #pos += 1
        result2 = exprAnd2()
        if (result2[0] == True):
            token.append(result2[1])
            #print(["Expression Logic", token],"\n")
            return [True, ["Expression Logic", token]]
        else:
            return [True, token]
    else:
        return [False, []]


def exprAnd2():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprAnd2")
    if(pos+1 >= len(Tokens)):
        return [False,[]]
    token = []
    if (Tokens[pos+1][0] == "AND"):
        pos+=1
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
            return [True, token]
        else:
            return [True, token]
    else:
        return [False, []]


# Seccion EQUALITY
def exprEquality():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprEquality")
    token = []
    result = exprComp()
    if (result[0] == True):
        token.append(result[1])
        #pos += 1
        result2 = exprEquality2()
        if (result2[0] == True):
            token.append(result2[1])
            #print(["Expression Binary", token], "\n")
            return [True, ["Expression Binary", token]]
        else:
            return [True, token]
    else:
        return [False, []]


def exprEquality2():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en  exprEquality2")

    if(pos+1 >= len(Tokens)):
        return [False,[]]
    token = []
    if (Tokens[pos+1][0] == "BANG_EQUAL" or Tokens[pos+1][0] == "EQUAL_EQUAL"):
        pos+=1
    if (Tokens[pos][0] == "BANG_EQUAL" or Tokens[pos][0] == "EQUAL_EQUAL"):
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
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprComp")
    token = []
    result = exprTerm()
    if (result[0] == True):
        token.append(result[1])
        #print("Estamos", pos)
        #pos += 1
        result2 = exprComp2()
        if (result2[0] == True):
            token.append(result2[1])
            #print(["Expression Binary", token], "\n")
            return [True, token]
        else:
            return [True, token]
    else:
        return [False, []]


def exprComp2():
    global pos
    global Tokens
    if(pos>=len(Tokens)):
        pos-=1
    if(Tokens[pos][0] == "SEMICOLON" or Tokens[pos][0]== "RIGHT_PAREN" or Tokens[pos][0]== "RIGHT_BRACE"):
        return [False, []]
    if(pos+1 >= len(Tokens)):
        return [False,[]]
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en  exprComp2")
    token = []
    if (Tokens[pos+1][0] == "GREATER" or Tokens[pos+1][0] == "GREATER_EQUAL" or Tokens[pos+1][0] == "LESS" or Tokens[pos+1][0] == "LESS_EQUAL"):
        pos+=1
    if (Tokens[pos][0] == "GREATER" or Tokens[pos][0] == "GREATER_EQUAL" or Tokens[pos][0] == "LESS" or Tokens[pos][0] == "LESS_EQUAL"):
        token.append(Tokens[pos][0])
        pos += 1
        result = exprTerm()
        if (result[0] == True):
            token.append(result[1])
            #pos += 1
        else:
            return [False, []]
        result2 = exprComp2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, token]
        else:
            return [True, token]
    else:
        return [False, []]


# Seccion Term
def exprTerm():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprTerm")
    token = []
    result = factor()
    if (result[0] == True):
        token.append(result[1])
        #pos += 1
        result2 = term2()
        if (result2[0] == True):
            token.append(result2[1])
            #print(["Expression Binary", token], "\n")
            return [True,["Expression Binary", token]]
        else:
            return [True, token]
    else:
        return [False, []]


def term2():
    global pos
    global Tokens
    if(pos>=len(Tokens)):
        pos-=1
    if(Tokens[pos][0] == "SEMICOLON" or Tokens[pos][0]== "RIGHT_PAREN" or Tokens[pos][0]== "RIGHT_BRACE"):
        if(Tokens[pos][0]== "RIGHT_PAREN" or Tokens[pos][0]== "RIGHT_BRACE" or Tokens[pos][0]== "SEMICOLON"):
            pos-=1
        return [False, []]
    if(pos+1 >= len(Tokens)):
        return [False,[]]
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en  term2")
    token = []
    if (Tokens[pos+1][0] == "MINUS" or Tokens[pos+1][0] == "PLUS"):
        pos+=1
    if (Tokens[pos][0] == "MINUS" or Tokens[pos][0] == "PLUS"):
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
            if(pos+1<len(Tokens)):
                if(Tokens[pos+1][0] == "SEMICOLON"):
                    pos+=1
        return [True, token]
    else:
        return [False, []]


def factor():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en factor")
    token = []
    result = exprUnary()
    if (result[0] == True):
        token.append(result[1])
        result2 = factor2()
        if (result2[0] == True):
            token.append(result2[1])
            #print(["Expression Binary", token], "\n")
            return [True, ["Expression Bynary", token]]
        else:
            return [True,token]
    else:
        return [False, []]


def factor2():
    global pos
    global Tokens
    if(Tokens[pos-1][0]== "SEMICOLON"):
        #pos-=1
        return [False, []]

    if(pos+1 >= len(Tokens)):
        return [False,[]]
    if(Tokens[pos][0] == "SEMICOLON" or Tokens[pos][0]== "RIGHT_PAREN" or Tokens[pos][0]== "RIGHT_BRACE"):
        #print("test2")
        return [False, []]

    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en  factor2")
    token = []
    if (Tokens[pos+1][0] == "STAR" or Tokens[pos+1][0] == "SLASH"):
        pos+=1
    if (Tokens[pos][0] == "STAR" or Tokens[pos][0] == "SLASH"):
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
        return [True, token]
    else:
        return [False, []]


# Seccion Unary

def exprUnary():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprUnary")
    token = []
    if (Tokens[pos][0] == "BANG" or Tokens[pos][0] == "MINUS"):
        cadena = "[Expression Unary, ["
        cadena += Tokens[pos][0]
        cadena += ",["
        token.append(Tokens[pos][0])
        pos += 1
        result = exprUnary()
        if (result[0] == True):
            token.append(result[1])
            #print([True, ["ExprUnary", token]])
            cadena+= result[1][1][0][0]
            cadena+= ", ["
            cadena+= result[1][1][0][1][0]
            cadena+= ", "
            cadena+= result[1][1][0][1][1]
            cadena+= "]]]"
            
            #print(cadena,"\n")
            return [True,["Expression Unary",token]]
        else:
            return [False, []]
    elif (Tokens[pos][0] == "TRUE" or Tokens[pos][0] == "FALSE" or Tokens[pos][0] == "NULL" or Tokens[pos][0] == "NUMBER" or
          Tokens[pos][0] == "STRING" or Tokens[pos][0] == "IDENTIFIER" or Tokens[pos][0] == "LEFT_PAREN"):
        result = exprCall()
        if (result[0] == True):
            token.append(result[1])
            #print([True, ["ExprUnary", token]])
            #print("posicion",pos)
            #print(["Expression Unary",token],"\n")
            return [True,["Expression Unary",token]]
    else:
        return [False, []]
    return [False, []]


def exprCall():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprCall")
    token = []
    if (Tokens[pos][0] == "TRUE" or Tokens[pos][0] == "FALSE" or Tokens[pos][0] == "NULL" or Tokens[pos][0] == "NUMBER" or
            Tokens[pos][0] == "STRING" or Tokens[pos][0] == "IDENTIFIER" or Tokens[pos][0] == "LEFT_PAREN"):
        result = exprPrimary()
        if (result[0] == True):
            token.append(result[1])
            #if(Tokens[pos+1][0] != "EQUAL" or Tokens[pos+1][0] != "SLASH" or Tokens[pos+1][0] != "STAR" or Tokens[pos+1][0] != "MINUS" or Tokens[pos+1][0] != "PLUS" or Tokens[pos+1][0] != "BANG" or Tokens[pos+1][0] != "BANG_EQUAL" or Tokens[pos+1][0] != "EQUAL_EQUAL" or Tokens[pos+1][0] != "GREATER" or Tokens[pos+1][0] != "GREATER_EQUAL" or Tokens[pos+1][0] != "LESS" or Tokens[pos+1][0] !=  "LESS_EQUAL"):
            #    pos += 1
            result2 = exprCall2()
            if (result2[0] == True):
                token.append(result2[1])
                #print(["Expression Call Function", token],"\n")
                return [True, ["Expression Call Function", token]]
            else:
                return [True,result[1]]
        else:
            return [False, []]
    else:
        return [False, []]

    return [False, []]


def exprCall2():
    global pos
    global Tokens
    if(pos>=len(Tokens)):
        return [False,[]]
    if(Tokens[pos][0] == "SEMICOLON"):
        return [False,[]]
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprCall2")
    token = []
    if(pos+1 >= len(Tokens)):
        return [False,[]]
    if (Tokens[pos+1][0] == "LEFT_PAREN"):
        pos += 1
        token.append(Tokens[pos][0])
        pos += 1
        result = argOpc()
        if (result[0] == True):
            token.append(result[1])
            if(Tokens[pos][0] == "RIGHT_PAREN"):
                pos-=1
            pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result2 = exprCall2()
        if (result2[0] == True):
            token.append(result2[1])
            return [True, token]
        else:
            return [True, token]
    return [False, []]


def exprPrimary():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en exprPrimary")
    token = []
    if (Tokens[pos][0] == "TRUE" or Tokens[pos][0] == "FALSE" or Tokens[pos][0] == "NULL" or Tokens[pos][0] == "NUMBER" or
            Tokens[pos][0] == "STRING" or Tokens[pos][0] == "IDENTIFIER"):
        #pos+=1
        if(Tokens[pos][0] == "TRUE" or Tokens[pos][0] == "FALSE" or Tokens[pos][0] == "NULL"):
            #print(["Expression Literal", Tokens[pos]],"\n")
            return [True, ["Expression Literal", Tokens[pos]]]
        if(Tokens[pos][0] == "NUMBER" or Tokens[pos][0] == "STRING"):
            #print(["Expression Literal", Tokens[pos]],"\n")
            return [True, ["Expression Literal", [Tokens[pos][0],Tokens[pos][1]]]]
        """
        if(Tokens[pos+1][0] == "LEFT_PAREN"):
            token.append(Tokens[pos])
            token.append(Tokens[pos+1])
            pos+=2
            result = paramOpc()
            if (result[0] == True):
                token.append(result[1])
                #pos += 1
            if (Tokens[pos][0] == "RIGHT_PAREN"):
                #print("prueba5")
                token.append(Tokens[pos])
                pos += 1
            else:
                return [False, []]
            if(Tokens[pos][0] == "SEMICOLON"):
                pos+=1
            else:
                return [False, []]
            print(["Function call", token])
            return [True, ["Function call", token]]
        """
        if(Tokens[pos][0] == "IDENTIFIER"):
            #print(["Expression Variable", Tokens[pos]],"\n")
            return [True, ["Expression Variable", Tokens[pos]]]
    elif (Tokens[pos][0] == "LEFT_PAREN"):
        #print("Entramos al elif")
        token.append(Tokens[pos][0])
        pos += 1
        result = Expression()
        if (result[0] == True):
            token.append(result[1])
            pos += 1
            if (Tokens[pos][0] == "RIGHT_PAREN"):
                Tokens.append(Tokens[pos][0])
                #print(["Expression Grouping", token],"\n")
                return [True, ["Expression Grouping", token]]
            else:
                return [False, []]
    return [False, []]


# Seccion Argumentos

def argOpc():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en argOpc")
    token = []
    result = Expression()
    if (result[0] == True):
        token.append(result[1])
        pos += 1
        result2 = arguments()
        if (result2[0] == True):
            token.append(result2[1])
            if(Tokens[pos-1][0]  =="RIGHT_PAREN"):
                pos-=1
            return [True, ["Arguments", token]]
        else:
            return [True, ["Arguments", token]]
    else:
        return [False, []]
    return [False, []]


def arguments():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en arguments")
    token = []
    if(Tokens[pos-1][0] == "COMMA"):
        pos-=1
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
        return [True,token]
    else:
        return [False, []]


# Seccion Functions

def funct():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en funct")
    token = []
    if (Tokens[pos][0] == "IDENTIFIER"):
        token.append(Tokens[pos])
        pos += 1

        if (Tokens[pos][0] == "LEFT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]

        result = paramOpc()

        if (result[0] == True):
            token.append(result[1])
            #pos += 1
        if (Tokens[pos][0] == "RIGHT_PAREN"):
            token.append(Tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        result2 = block()
        if (result2[0] == True):
            token.append(result2[1])
            pos += 1
            return [True,token]
        else:
            return [False, []]
    else:
        return [False, []]


# Seccion parameters

def paramOpc():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en paramOpc")
    token = []
    result = parameters()
    if (result[0] == True):
        token.append(result[1])
        return [True,  token]
    else:
        return [False, []]


def parameters():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en parameters")
    token = []
    if (Tokens[pos][0] == "IDENTIFIER" or Tokens[pos][0] == "NUMBER"):
        token.append(Tokens[pos])
        pos += 1
        result = parameters2()
        if (result[0] == True):
            token.append(result[1])
        #else:
        #    return [False, []]
        #print("\nprueba3")
        return [True, ["Parameters", token]]
    else:
        return [False, []]


def parameters2():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en parameters2")
    token = []
    if (Tokens[pos][0] == "COMMA"):
        #print("test")
        token.append(Tokens[pos][0])
        pos += 1
        if (Tokens[pos][0] == "IDENTIFIER" or Tokens[pos][0] == "NUMBER"):
            token.append(Tokens[pos])
            pos += 1
        else:
            #print("\nprueba")
            return [False, []]
        result = parameters2()
        if (result[0] == True):
            token.append(result[1])
        #else:
            #print("\nprueba")
            #return [False, []]
        return [True,  token]

    else:
        #print("\nprueba2")
        return [False, []]
    return [False, []]


# Seccion block

def block():
    global pos
    global Tokens
    #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
    #print("Estamos en block")
    token = []
    if (Tokens[pos][0] == "LEFT_BRACE"):
        token.append(Tokens[pos][0])
        pos += 1
        result = declaration()
        #print(result[0])
        if (result[0] == True):
            token.append(result[1])
            #print(result[0])
            if(Tokens[pos][0] != "RIGHT_BRACE"):
                pos += 1
            #print("Estamos en", pos, "que tiene el valor:", Tokens[pos])
        else:
            return [False, []]
        if (Tokens[pos][0] == "RIGHT_BRACE"):
            token.append(Tokens[pos][0])
            #if (pos + 1 <= len(Tokens)):
                #pos += 1
            #print("\n\n\nexito\n\n\n")
            return [True, ["Block", token]]
        else:
            return [False, []]
    else:
        return [False, []]


def main():
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