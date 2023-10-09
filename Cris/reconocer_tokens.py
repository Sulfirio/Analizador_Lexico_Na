


def recognize_tokens(input_string):
    S0 = 0
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
    
    while pos < len(input_string):
        char = input_string[pos]
        if state == S0:
            if char.isnumeric():
                state = S15
            
        if state == S15:
            state = S22
            if char.isnumeric():
                state = S15
                print(char)
                token +=char
            elif char == '.':
                state = S16
                print(char)
                token +=char
            elif char == 'E':
                state = S18
                print(char)
                token +=char
            pos +=1
            
        elif state == S16:
            if char.isnumeric():
                state = 17
                print(char)
                token +=char
                
        elif state == S17:
            state = S23
            if char.isnumeric():
                state = S17
                print(char)
                token +=char
            elif char == 'E':
                state = S18
                print(char)
                token +=char
            pos += 1
            
        elif state == S18:
            if char == '+' or char == '-':
                state = S19
                print(char)
                token +=char
            if char.isnumeric():
                state = S20
                print(char)
                token +=char
            pos+=1
            
        elif state == S19:
            if char.isnumeric():
                state = S20
                print(char)
                token +=char
            pos+=1
                
        elif state == S20:
            state = S21
            if char.isnumeric():
                state = S20
                print(char)
                token +=char
            pos+=1               
            
            
    print("Estado es",state)
    if state == S21:
        return (token,19)
            
            
    if state == S22:
        return (token,20)
            
            
    if state == S23:
        return (token,21)
    return (token,21)
    


# Ejemplo de uso
test_string = """
int x = 10; // This is a single-line comment
/* This is a 
multi-line comment */
int y = 20;
"""

def main():
    print(recognize_tokens("154|"))

if __name__ == "__main__":
    main()