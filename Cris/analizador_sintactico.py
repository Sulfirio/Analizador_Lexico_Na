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
        comparison = forStm1()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
        else:
            return [False,[]]
            
        comparison2 = forStm2()
        if(comparison2[0] == True):
            token.append(comparison2[1])
            pos+=1
        else:
            return [False,[]]
            
        comparison3 = forStm3()
        if(comparison3[0] == True):
            token.append(comparison3[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        comparison4 = statement()
        if(comparison4[0] == True):
            token.append(comparison4[1])
        else:
            return [False,[]]
        return [True,["ForStm",token]]
    else:
        return [False,[]]
    
    
def forStm1():
    token = []
    comparison = varDecl()
    comparison2 = exprStm()
    if(comparison[0] == True):
        token.append(comparison[1])
        return [True,["ForStm1",token]]
    elif(comparison2[0] == True):
        token.append(comparison2[1])
        return [True,["ForStm1",token]]
    elif(tokens[pos][0] == "SEMICOLON"):
        token.append(tokens[pos][0])
        return [True,["ForStm1",token]]
    else:
        return [False,[]]
        
def forStm2():
    token = []
    comparison = expression()
    if(comparison[0] == True):
        token.append(comparison[1])
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
    comparison = expression()
    if(comparison[0] == True):
        return [True,["ForStm3"],comparison[1]]
    
# Seccion Whil

def whileStm():
    token = []
    if(tokens[pos][0] == "WHILE"):
        token.append(token[pos][0])
        pos+=1
        if(tokens[pos][0] == "LEFT_PAREN"):
            token.append(token[pos][0])
            pos+=1
            comparison = expression()
            if(comparison[0] == True):
                token.append(comparison[1])
                pos+=1
            comparison2 = whileStm()
            if(comparison2[0] == True):
                token.append(comparison2[1])
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
        comparison = expression()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos+=1
        else:
            return [False,[]]
        comparison2 = statement()
        if(comparison2[0] == True):
            token.append(comparison2[1])
            pos+=1
        else:
            return [False,[]]
        comparison3 = elseStm()
        if(comparison3 == True):
            token.append(comparison3[1])
        return [True,["ForStm",token]]
        
    else:
        return [False,[]]
    
def elseStm():
    token = []
    if(tokens[pos][0] == "ELSE"):
        token.append(tokens[pos][0])
        pos +=1
        comparison = statement()
        if(comparison[0] == True):
            token.append(comparison[1])
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
        comparison = expression()
        if(comparison[0] == True):
            token.append(comparison[1])
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
        comparison = returnOpc()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
        if(tokens[pos][0] == "SEMICOLON"):
            token.append(tokens[pos][0])
            return [True,["ReturnStm",token]]
        else:    
            return [False,[]]
    else:
        return [False,[]]
    
def returnOpc():
    comparison = expression()
    if(comparison[0] == True):
        return [True,"ReturnOpc",comparison[1]]
    return [False,[]]

# Seccion Unary

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

#Seccion Argumentos

def argOpc():
    token = []
    comparison = expression()
    if(comparison[0] == True):
        token.append(comparison[1])
        pos+=1
        comparison2 = arguments()
        if(comparison2[0] == True):
            token.append(comparison2[1])
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
        comparison = expression()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
        comparison2 = expression()
        if(comparison2[0] == True):
            token.append(comparison2[1])
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
        comparison = paramOpc()
        if(comparison[0] == True):
            token.append(comparison[1])
            pos+=1
        if(tokens[pos][0] == "RIGHT_PAREN"):
            token.append(tokens[pos][0])
            pos +=1
        else:
            return [False,[]]
        comparison2 = block()
        if(comparison2[0] == True):
            token.append(comparison2[1])
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
        comparison = parameters()
        if(comparison[0] == True):
            token.append(comparison[1])
        return [True,["ParametersOpc",token]]
    else:
        return [False,[]]
    
def parameters():
    token = []
    if(tokens[pos][0] == "IDENTIFIER"):
        token.append(tokens[pos][0])
        pos+=1
        comparison = parameters2()
        if(comparison[0] == True):
            token.append(comparison[1])
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
        comparison = parameters2
        if(comparison[0] == True):
            token.append(comparison[1])
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
        comparison = declaration()
        if(comparison[0] == True):
            token.append(comparison[1])
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
