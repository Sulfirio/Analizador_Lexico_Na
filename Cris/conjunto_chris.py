class Token:
    def init(self, type, value):
        self.type = type
        self.value = value
        self.literal = None
        
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

    state = S0
    pos = 0    
    token = ""
    
    keywords = [
        "AND", "ELSE", "FALSE", "FUN", "FOR", "IF", "NULL", "OR",
        "PRINT", "RETURN", "TRUE", "VAR", "WHILE"]
    
    while pos < len(input_string):
        char = input_string[pos]
        if state == S0:
            if char.isnumeric():
                state = S15
            if char.isalpha():
                state = S13
        
        if state == S13:
            if char.isalpha() or char.isnumeric():                
                state = S13
                token += char                   
            else:
                state = 14
            pos += 1
            
        if state == S14:
            status = 0
            for i in range (len(keywords)):
                if token.lower == keywords[i].lower():
                    tokens.append(Token(keywords[i],token.lower,token.lower))
                    status = 1
                    i = (len(keywords))
            if status == 0:
                tokens.append(Token("IDENTIFIER", token,token))                
                    
            
        if state == S15:
            state = S22
            if char.isnumeric():
                state = S15
                token +=char
                
            elif char == '.':
                state = S16
                token +=char
                
            elif char == 'E':
                state = S18
                token +=char
            pos +=1
            
        elif state == S16:
            if char.isnumeric():
                state = 17
                token +=char
                
        elif state == S17:
            state = S23
            if char.isnumeric():
                state = S17
                token +=char
                
            elif char == 'E':
                state = S18
                token +=char
                
            pos += 1
            
        elif state == S18:
            if char == '+' or char == '-':
                state = S19
                token +=char
                
            if char.isnumeric():
                state = S20
                token +=char
                
            pos+=1
            
        elif state == S19:
            if char.isnumeric():
                state = S20
                token +=char
                
            pos+=1
                
        elif state == S20:
            state = S21
            if char.isnumeric():
                state = S20
                token +=char
                
            pos+=1
        if state == S21:
            tokens.append(Token("NUMBER", token,int(token)))
            state == 0
                
                
        if state == S22:
            tokens.append(Token("NUMBER", token,float(token)))
            state == 0
                
                
        if state == S23:
            tokens.append(Token("NUMBER", token,float(token)))
            state == 0
        
