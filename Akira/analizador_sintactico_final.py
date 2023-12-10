import sys

pos = 0
tokens = []


def analizador_sintactico(tokens):
    return 0


def expression():
    return [False, []]


# Seccion Unary

FIRST = {
    'UNARY': {'!', '-', 'true', 'false', 'null', 'number', 'string', 'id', '('},
    'PRIMARY': {'true', 'false', 'null', 'number', 'string', 'id', '('}
}


def exprTerm():
    if tokens[pos][0] in FIRST['FACTOR']:  # Si el token actual está en el conjunto FIRST de FACTOR entra
        factor()
        term_2()
    else:
        raise SyntaxError("Error sintáctico en TERM con token: " + tokens[pos][0])


def term_2():
    if tokens[pos][0] == 'MINUS':
        match('-')
        factor()
        term_2()
    elif tokens[pos][0] == 'PLUS':
        match('+')
        factor()
        term_2()
    elif tokens[pos][0] in FOLLOW['TERM_2']:
        pass
    else:
        raise SyntaxError("Error sintáctico en TERM_2 con token: " + tokens[pos][0])


def factor():
    if tokens[pos][0] in FIRST['FACTOR']:  # Si el token actual está en el conjunto FIRST de FACTOR entra
        unary()  # Llama a la función para UNARY
        factor_2()  # Llama a la función para FACTOR_2
    else:
        raise SyntaxError("Error sintáctico en FACTOR con token: " + tokens[pos][0])


def unary():
    # Implementación para UNARY
    pass


def factor_2():
    # Implementación para FACTOR_2
    pass


def match(expected_token):
    global lookahead
    if lookahead == expected_token:
        lookahead = next_token()
    else:
        raise SyntaxError("Error sintáctico, se esperaba: " + expected_token)


def exprUnary():
    token = []
    if (tokens[pos][0] == "BANG" | tokens[pos][0] == "MINUS"):
        token.append(tokens[pos][0])
        pos += 1
        comparison = exprUnary()
        if (comparison[0] == True):
            token.append(comparison[1])
            return [True, ["ExprUnary", token]]
        else:
            return [False, []]
    elif (tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" |
          tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER" | tokens[pos][0] == "LEFT_PAREN"):
        comparison = exprCall()
        token.append(comparison[1])
        if (comparison[0] == True):
            return [True, ["ExprUnary", token]]
    else:
        return [False, []]
    return [False, []]


def exprCall():
    token = []
    if (tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" |
            tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER" | tokens[pos][0] == "LEFT_PAREN"):
        comparison = exprPrimary()
        if (comparison[0] == True):
            token.append(comparison[1])
            pos += 1
            comparison2 = exprCall2()
            if (comparison2[0] == True):
                token.append(comparison2[1])
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
    if (tokens[pos][0] == "LEFT_PAREN"):
        token.append(tokens[pos][0])
        pos += 1
        comparison = argOpc()
        if (comparison[0] == True):
            token.append(comparison[1])
            pos += 1
        if (tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos += 1
        else:
            return [False, []]
        comparison2 = exprCall2()
        if (comparison2[0] == True):
            token.append(comparison2[1])
            return [True, ["ExprCall2", token]]
        else:
            return [True, ["ExprCall2", token]]
    return [False, []]


def exprPrimary():
    token = []
    if (tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" |
            tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER"):
        return [True, ["ExprPrimary", tokens[pos][0]]]
    elif (tokens[pos][0] == "LEFT_PAREN"):
        token.append(tokens[pos][0])
        pos += 1
        comparison = expression()
        if (comparison[0] == True):
            token.append(comparison[1])
            pos += 1
            if (tokens[pos][0] == "RIGHT_PAREN"):
                tokens.append(tokens[pos][0])
                return [True, ["ExprPrimary", token]]
            else:
                return [False, []]
    return [False, []]


# Seccion Argumentos

def argOpc():
    token = []
    comparison = expression()
    if (comparison[0] == True):
        token.append(comparison[1])
        pos += 1
        comparison2 = arguments()
        if (comparison2[0] == True):
            token.append(comparison2[1])
            return [True, ["ArgOpc", token]]
        else:
            return [True, ["ArgOpc", token]]
    else:
        return [False, []]
    return [False, []]


def arguments():
    token = []
    if (tokens[pos][0] == "COMMA"):
        token.append(tokens[pos][0])
        pos += 1
        comparison = expression()
        if (comparison[0] == True):
            token.append(comparison[1])
            pos += 1
        comparison2 = expression()
        if (comparison2[0] == True):
            token.append(comparison2[1])
            pos += 1
        return [True, ["Arguments", token]]
    else:
        return [False, []]


# Seccion Functions

def main():
    tokens.append("BANG", "!")
    tokens.append("IDENTIFIER", "aux")
    return 0


if __name__ == "__main__":
    main()
