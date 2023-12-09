import sys

pos = 0
tokens = []


def analizador_sintactico(tokens):
    
    return 0

def expression():
    
    return [False,[]]

def exprUnary():
    token = []
    if(tokens[pos][0] == "BANG" | tokens[pos][0] == "MINUS"):
        token.append(tokens[pos][0])
        pos+=1
        comparison = exprUnary()
        if(comparison[0] == True):
            token.append(comparison[1])
            return [True,["ExprUnary",token]]
        else:
            return [False,[]]
    elif(tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" | tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER" | tokens[pos][0] == "LEFT_PAREN"):
        comparison = exprCall()
        token.append(comparison[1])
        if(comparison[0] == True):
            return [True,["ExprUnary",token]]
    else:
        return [False,[]]
    return [False,[]]

def exprCall():    
    token = []
    if(tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" | tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER" | tokens[pos][0] == "LEFT_PAREN"):
        comparison = exprPrimary()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
            comparison2 = exprCall2()                
            if(comparison2[0] == True):
                token.append(comparison2[1])
                return [True,["ExprCall",token]]
            else:
                return [True,["ExprCall",token]]
        else:
            return [False,[]]
    else:
        return [False,[]]
        
    return [False,[]]

def exprCall2():
    token = []
    if(tokens[pos][0] == "LEFT_PAREN"):
        token.append(tokens[pos][0])
        pos+=1
        comparison = argOpc()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        comparison2 = exprCall2()
        if(comparison2[0] == True):
            token.append(comparison2[1])
            return [True,["ExprCall2",token]]
        else:
            return [True,["ExprCall2",token]]
    return [False,[]]


def exprPrimary():
    token = []
    if(tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" | tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER"):
        return [True,["ExprPrimary",tokens[pos][0]]]
    elif(tokens[pos][0] == "LEFT_PAREN"):
        token.append(tokens[pos][0])
        pos +=1
        comparison = expression()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
            if(tokens[pos][0] == "RIGHT_PAREN"):
                tokens.append(tokens[pos][0])
                return [True,["ExprPrimary",token]]
            else:
                return [False,[]]
    return [False,[]]

def argOPC():
    
    return 0

def main():
    tokens.append("BANG","!")
    tokens.append("IDENTIFIER","aux")
    return 0


if __name__ == "__main__":
    main()
