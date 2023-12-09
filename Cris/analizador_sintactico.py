import sys

pos = 0
tokens = []

# Seccion declaration

def declaration():
    token =[]
    return [False,[]]

# Seccion expression

def expression():
    
    return [False,[]]

def exprStm():
    
    return [False,[]]

# Seccion Var

def varDecl():
    
    return [False,[]]

# Seccion statement

def statement():
    token = []
    return [False,[]]

# Seccion For

def forStm():
    token = []
    if(tokens[pos][0] == "FOR"):
        token.append(tokens[pos][0])
        pos+=1
        if(tokens[pos][0] == "LEFT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        result = forStm1()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        else:
            return [False,[]]
            
        result2 = forStm2()
        if(result2[0] == True):
            token.append(result2[1])
            pos+=1
        else:
            return [False,[]]
            
        result3 = forStm3()
        if(result3[0] == True):
            token.append(result3[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        result4 = statement()
        if(result4[0] == True):
            token.append(result4[1])
        else:
            return [False,[]]
        return [True,["ForStm",token]]
    else:
        return [False,[]]
    
    
def forStm1():
    token = []
    result = varDecl()
    result2 = exprStm()
    if(result[0] == True):
        token.append(result[1])
        return [True,["ForStm1",token]]
    elif(result2[0] == True):
        token.append(result2[1])
        return [True,["ForStm1",token]]
    elif(tokens[pos][0] == "SEMICOLON"):
        token.append(tokens[pos][0])
        return [True,["ForStm1",token]]
    else:
        return [False,[]]
        
def forStm2():
    token = []
    result = expression()
    if(result[0] == True):
        token.append(result[1])
        pos+=1
        if(tokens[pos][0] == "SEMICOLON"):
            token.append(tokens[pos][0])
        else:
            return [False,[]]
        return [True,["ForStm2",token]]
    elif(tokens[pos][0] == "SEMICOLON"):
        return [True,["ForStm2",tokens[pos][0]]]
    else:
        return [False,[]]
        
def forStm3():
    result = expression()
    if(result[0] == True):
        return [True,["ForStm3"],result[1]]
    
# Seccion Whil

def whileStm():
    token = []
    if(tokens[pos][0] == "WHILE"):
        token.append(token[pos][0])
        pos+=1
        if(tokens[pos][0] == "LEFT_PAREN"):
            token.append(token[pos][0])
            pos+=1
            result = expression()
            if(result[0] == True):
                token.append(result[1])
                pos+=1
            result2 = whileStm()
            if(result2[0] == True):
                token.append(result2[1])
                pos+=1
            return [True, ["WhileStm",token]]
        else:
            return [False,[]]
    else:
        return [False,[]]

# Seccion if

def ifStm():
    token = []
    if(tokens[pos][0] == "IF"):
        token.append(tokens[pos][0])
        pos+=1
        if(tokens[pos][0] == "LEFT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        result = expression()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        result2 = statement()
        if(result2[0] == True):
            token.append(result2[1])
            pos+=1
        else:
            return [False,[]]
        result3 = elseStm()
        if(result3 == True):
            token.append(result3[1])
        return [True,["ForStm",token]]
        
    else:
        return [False,[]]
    
def elseStm():
    token = []
    if(tokens[pos][0] == "ELSE"):
        token.append(tokens[pos][0])
        pos +=1
        result = statement()
        if(result[0] == True):
            token.append(result[1])
            return [True,["ElseStm",token]]
        else:
            return [False,[]]
    else:
        return [False,[]]

# Seccion Print 

def printStm():
    token = []
    if(tokens[pos][0] == "PRINT"):
        token.append(tokens[pos][0])
        pos +=1
        result = expression()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        else:
            return [False,[]]
        if(tokens[pos][0] == "SEMICOLON"):
            token.append(tokens[pos][0])
            return [True,["ElseStm",token]]
        else:    
            return [False,[]]
    else:
        return [False,[]]

#Seccion Return

def returnStm():
    token = []
    if(tokens[pos][0] == "RETURN"):
        token.append(tokens[pos][0])
        pos +=1
        result = returnOpc()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        if(tokens[pos][0] == "SEMICOLON"):
            token.append(tokens[pos][0])
            return [True,["ReturnStm",token]]
        else:    
            return [False,[]]
    else:
        return [False,[]]
    
def returnOpc():
    result = expression()
    if(result[0] == True):
        return [True,["ReturnOpc",result[1]]]
    return [False,[]]

# Seccion Term
def exprTerm():
    token = []
    result = factor() 
    if (result[0] == True):
        token.append(result[1])
        pos+=1
        result2 = term2()
        if(result2[0] == True):
            token.append(result2[1])
        return [True,["ExprTerm",token]]
    else:
        return [False,[]]
    
def term2():
    return 0

def factor():
    return 0

# Seccion Unary

def exprUnary():
    token = []
    if(tokens[pos][0] == "BANG" | tokens[pos][0] == "MINUS"):
        token.append(tokens[pos][0])
        pos+=1
        result = exprUnary()
        if(result[0] == True):
            token.append(result[1])
            return [True,["ExprUnary",token]]
        else:
            return [False,[]]
    elif(tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" | tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER" | tokens[pos][0] == "LEFT_PAREN"):
        result = exprCall()
        token.append(result[1])
        if(result[0] == True):
            return [True,["ExprUnary",token]]
    else:
        return [False,[]]
    return [False,[]]

def exprCall():    
    token = []
    if(tokens[pos][0] == "TRUE" | tokens[pos][0] == "FALSE" | tokens[pos][0] == "NULL" | tokens[pos][0] == "NUMBER" | tokens[pos][0] == "STRING" | tokens[pos][0] == "IDENTIFIER" | tokens[pos][0] == "LEFT_PAREN"):
        result = exprPrimary()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
            result2 = exprCall2()                
            if(result2[0] == True):
                token.append(result2[1])
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
        result = argOpc()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        result2 = exprCall2()
        if(result2[0] == True):
            token.append(result2[1])
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
        result = expression()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
            if(tokens[pos][0] == "RIGHT_PAREN"):
                tokens.append(tokens[pos][0])
                return [True,["ExprPrimary",token]]
            else:
                return [False,[]]
    return [False,[]]

#Seccion Argumentos

def argOpc():
    token = []
    result = expression()
    if(result[0] == True):
        token.append(result[1])
        pos+=1
        result2 = arguments()
        if(result2[0] == True):
            token.append(result2[1])
            return [True,["ArgOpc", token]]
        else:
            return [True,["ArgOpc", token]]
    else:
        return [False,[]]
    return [False,[]]

def arguments():
    token = []
    if(tokens[pos][0] == "COMMA"):
        token.append(tokens[pos][0])
        pos+=1
        result = expression()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        result2 = expression()
        if(result2[0] == True):
            token.append(result2[1])
            pos+=1
        return [True,["Arguments", token]]
    else:
        return [False,[]]
    
#Seccion Functions

def funct():
    token = []
    if(tokens[pos][0] == "IDENTIFIER"):
        token.append(tokens[pos][0])
        pos+=1
        if(tokens[pos][0] == "LEFT_PAREN"):
            token.append(tokens[pos][0])
            pos +=1
        else:
            return [False,[]]
        result = paramOpc()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos +=1
        else:
            return [False,[]]
        result2 = block()
        if(result2[0] == True):
            token.append(result2[1])
            pos+=1
            return [True,["Function", token]]
        else:
            return [False,[]]
    else:
        return [False,[]]
    
    
#Seccion parameters

def paramOpc():
    token = []
    if(tokens[pos][0] == "IDENTIFIER"):
        result = parameters()
        if(result[0] == True):
            token.append(result[1])
        return [True,["ParametersOpc",token]]
    else:
        return [False,[]]
    
def parameters():
    token = []
    if(tokens[pos][0] == "IDENTIFIER"):
        token.append(tokens[pos][0])
        pos+=1
        result = parameters2()
        if(result[0] == True):
            token.append(result[1])
        else:
            return [False,[]] 
        return [True,["Parameters",token]]
    else:
        return [False,[]]
    
def parameters2():
    token = []
    if(tokens[pos][0] == "COMMA"):
        token.append(tokens[pos][0])
        pos+=1
        if(tokens[pos][0] == "IDENTIFIER"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        result = parameters2
        if(result[0] == True):
            token.append(result[1])
        else:
            return [False,[]]
        return [True,["Parameters_2",token]]
    else:
        return [True,[""]]
    return [False,[]]

#Seccion block

def block():
    token =[]
    if(tokens[pos][0] == "LEFT_BRACE"):
        token.append(tokens[pos][0])
        pos+=1
        result = declaration()
        if(result[0] == True):
            token.append(result[1])
            pos+=1
        if(tokens[pos][0] == "LEFT_BRACE"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
    else:
        return [False,[]]


def main():
    tokens.append("BANG","!")
    tokens.append("IDENTIFIER","aux")
    return 0


if __name__ == "__main__":
    main()
