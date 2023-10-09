
def get_token():
    return 0
def install_id():
    return 0
def recognize_comments(input_string):
    # Definimos los estados
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4

    state = S0
    pos = 0
    comments = []
    comment_start = -1

    while pos < len(input_string):
        char = input_string[pos]

        # Estado inicial (S0)
        if state == S0:
            if char == '/':
                state = S1
                comment_start = pos
            pos += 1

        # Estado S1
        elif state == S1:
            if char == '/':
                state = S2
            elif char == '*':
                state = S3
            else:
                state = S0
                comment_start = -1
            pos += 1

        # Estado S2 (comentario de línea única)
        elif state == S2:
            if char == '\n':
                state = S0
                comments.append(input_string[comment_start:pos])
                comment_start = -1
            pos += 1

        # Estado S3 (comienzo de comentario de múltiples líneas)
        elif state == S3:
            if char == '*':
                state = S4
            pos += 1

        # Estado S4
        elif state == S4:
            if char == '/':
                state = S0
                comments.append(input_string[comment_start:pos + 1])
                comment_start = -1
            elif char == '*':
                # Nos mantenemos en S4
                pass
            else:
                state = S3
            pos += 1

    return comments

def recognize_stop_words(input_string):
    S0 = 0
    S13 = 13
    S14 = 14
    S15 = 15
    input_string += "|"
    
    keywords = [
        "AND", "ELSE", "FALSE", "FUN", "FOR", "IF", "NULL", "OR",
        "PRINT", "RETURN", "TRUE", "VAR", "WHILE"]
    

    state = S0
    pos = 0
    comment_start = -1
    
    i = 0
    
    stop_word = ""
    
    while pos < len(input_string):
        char = input_string[pos]
        # Estado inicial (S0)
        if state == S0:
            if char.isalpha():
                state = S13
                print(char)
                stop_word += char   
            pos += 1
            
        elif state == S13:
            if char.isalpha() or char.isnumeric():                
                state = S13
                comment_start = pos
                stop_word += char                
                print(stop_word)
                   
            else:
                print(char,"char ya no es caracter o num")
                state = 14
            pos += 1
            
        
        if state == S14:
            for i in range (len(keywords)):
                if stop_word == keywords[i]:
                    print("Es una palabra reservada: ")
                    return (stop_word,i)
            state = S15
            

    print("Es un identificador")          
        

    return stop_word


def recognize_tokens(input_string):
    S0 = 0
    S13 = 13
    S14 = 14
    S15 = 15
    input_string += "|"
    
    keywords = [
        "AND", "ELSE", "FALSE", "FUN", "FOR", "IF", "NULL", "OR",
        "PRINT", "RETURN", "TRUE", "VAR", "WHILE"]
    

    state = S0
    pos = 0
    comment_start = -1
    
    i = 0
    
    token = ""
    
    while pos < len(input_string):
        char = input_string[pos]
        # Estado inicial (S0)
        if state == S0:
            if char.isalpha():
                state = S13
                print(char)
                stop_word += char   
            pos += 1
            
        elif state == S13:
                
            pos += 1      
        

    return token
    


# Ejemplo de uso
test_string = """
int x = 10; // This is a single-line comment
/* This is a 
multi-line comment */
int y = 20;
"""

def main():
    print(recognize_stop_words("falasia"))

if __name__ == "__main__":
    main()