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