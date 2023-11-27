class Token:
    def __init__(self, token_type, value, literal=None):
        self.type = token_type
        self.value = value
        self.literal = literal


token_dict = {
    "COMMA": ",",
    "DOT": ".",
    "ASTERIC": "*",
    "IDENTIFIER": "identifier",
    "SELECT": "EOF",
    "DISTINCT": "EOF",
    "FROM": "EOF"
}

keywords = [
    "AND", "ELSE", "FALSE", "FUN", "FOR", "IF", "NULL", "OR",
    "PRINT", "RETURN", "TRUE", "VAR", "WHILE", "SELECT","DISTINCT","FROM"]


def analizador_lexico(input_string):
    tokens = []
    errors = []
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    S10 = 10
    SA = -1
    S14 = 14

    state = S0
    pos = 0
    token = ""
    comments = []
    comment_start = -1
    char_to_token = {v: k for k, v in token_dict.items()}
    while pos < len(input_string):
        char = input_string[pos]
        print("Estado ", state,"con char",char)
        if state == S0:
            token = ""
            if char.isspace():
                pos += 1
                continue
            elif char.isalpha():
                state = S2
            elif char == '*':
                state = S3
                continue
            elif char == '.':
                state = S14
                continue
            elif char == ',':
                state = S14
                continue
            else:
                state = SA
        if state == S1:
            if char.isalpha() or char.isnumeric():
                state = S1
                token += char
            elif char == ".":
                state = 14
                continue
            elif char == ",":
                state = 14
                continue
            else:
                state = 14
            pos += 1

        if state == S2:
            tokens.append("ASTERIC",char)
            pos+=1
            
        if state == S3:
            tokens.append("DOT",char)
            pos+=1
            
        if state == S4:
            tokens.append("COMMA",char)
            pos+=1
            
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
        
        if state == SA:
            print("Error.")
            return tokens
            
    return tokens


def analizador_descendente(tokens):
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
    SFIN = -2
    
    SA = -1
    
    S = 0
    
    result = "Exito"
    for token in tokens:
        if S == S0:
            if token[0] == "SELECT":
                S = S1
            else:
                S = SA
                
        elif S == S1:
            if token[0] == "ASTERIC":
                S = S2
            elif token[0] == "DISTINCT":
                S = S3
            elif token[0] == "IDENTIFIER":
                S = S4
            else: 
                S = SA
                       
                
        elif S == S2:
            if token[0] == "FROM":
                S = S5
            else:
                S = SA
            
            
                
        elif S == S3:
            if token[0] == "*":
                S = S2
            elif token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA
            
            
                
        elif S == S4:
            if token[0] == "COMMA":
                S = S6
            elif token[0] == "DOT":
                S = S7
            elif token[0] == "FROM":
                S = S5
            else:
                S = SA
            
            
            
                
        elif S == S5:
            if token[0] == "IDENTIFIER":
                S = S8
            else:
                S = SA
            
            
            
                
        elif S == S6:
            if token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA
            
            
                
        elif S == S7:
            if token[0] == "IDENTIFIER":
                S = S4
            else:
                S = SA
            
            
            
                
        elif S == S8:
            if token[0] == "COMMA":
                S = S9
            elif token[0] == "DOT":
                S = S10
            else:
                S = SA
            
            
                
        elif S == S9:
            if token[0] == "IDENTIFIER":
                S = S8
            else:
                S = SA
            
            
                
        elif S == S10:
            if token[0] == "IDENTIFIER":
                S = S8
            else:
                S = SA
            
            
            
            
            
            
        if S == SA:
            return "Error"
        
            
        
    return result

def main():
    test_string = """
    var nombre = "Nombre";
    var apellido1 = "Apellido";

    print nombre + " " + apellido1; 
    """
    tokens = analizador_lexico(test_string)
    for token in tokens:
        print(token)
    analisis = analizador_descendente(tokens)
    

if __name__ == "__main__":
    main()
