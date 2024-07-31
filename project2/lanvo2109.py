TOKEN_TYPES = {
    'NUMBER': 0,
    'ADD': 1,
    'SUB': 2,
    'MUL': 3,
    'DIV': 4,
    'LPAREN': 5,
    'RPAREN': 6,
    'MOD': 7,
    'EQUAL': 8
}

def tokenize(tokens):
    result = []
    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            result.append((TOKEN_TYPES['NUMBER'], float(token)))
        elif token == '+':
            result.append((TOKEN_TYPES['ADD'], token))
        elif token == '-':
            result.append((TOKEN_TYPES['SUB'], token))
        elif token == '*':
            result.append((TOKEN_TYPES['MUL'], token))
        elif token == '/':
            result.append((TOKEN_TYPES['DIV'], token))
        elif token == '(':
            result.append((TOKEN_TYPES['LPAREN'], token))
        elif token == ')':
            result.append((TOKEN_TYPES['RPAREN'], token))
        elif token == '%':
            result.append((TOKEN_TYPES['MOD'], token))
        elif token == '=':
            result.append((TOKEN_TYPES['EQUAL'], token))
        else:
            raise ValueError(f"Unrecognized token: {token}")
    return result

def parse_expression(tokens):
    def parse_primary():
        token_type, token_value = tokens.pop(0)
        if token_type == TOKEN_TYPES['NUMBER']:
            return token_value
        elif token_type == TOKEN_TYPES['LPAREN']:
            expr = parse_expression()
            if tokens and tokens[0][0] == TOKEN_TYPES['RPAREN']:
                tokens.pop(0)
            return expr
        elif token_type == TOKEN_TYPES['SUB']:
            return -parse_primary()
        raise ValueError("Invalid syntax")

    def parse_term():
        result = parse_primary()
        while tokens and tokens[0][0] in (TOKEN_TYPES['MUL'], TOKEN_TYPES['DIV'], TOKEN_TYPES['MOD']):
            token_type, _ = tokens.pop(0)
            if token_type == TOKEN_TYPES['MUL']:
                result *= parse_primary()
            elif token_type == TOKEN_TYPES['DIV']:
                result /= parse_primary()
            elif token_type == TOKEN_TYPES['MOD']:
                result %= parse_primary()
        return result

    def parse_expression():
        result = parse_term()
        while tokens and tokens[0][0] in (TOKEN_TYPES['ADD'], TOKEN_TYPES['SUB']):
            token_type, _ = tokens.pop(0)
            if token_type == TOKEN_TYPES['ADD']:
                result += parse_term()
            elif token_type == TOKEN_TYPES['SUB']:
                result -= parse_term()
        return result

    return parse_expression()

def Calculator():
    current_result = None
    tokens = []
    
    while True:
        token = input("Enter Number or Symbol(+, -, *, /, %, (, ), =, E): ")
        if token == "=":
            if tokens:
                if current_result is not None:
                    tokens.insert(0, str(current_result))
                expression = " ".join(tokens)
                token_list = tokenize(tokens)
                try:
                    result = parse_expression(token_list)
                    current_result = result
                    print(f"Result: {expression} = {result}")
                except (ValueError, IndexError) as e:
                    print(f"Error: {e}")
            else:
                print("Chưa nhập biểu thức")
            tokens = []
            
        elif token == 'E':
            break
        
        else:
            tokens.append(token)
    
    if tokens:
        try:
            token_list = tokenize(tokens)
            result = parse_expression(token_list)
            print(f"Kết quả cuối cùng: {result}")
        except (ValueError, IndexError) as e:
            print(f"Lỗi: {e}")

print("Enter '+' for Addition")
print("Enter '-' for Subtraction")
print("Enter '*' for Multiplication")
print("Enter '/' for Division")
print("Enter '%' for Modulo")
print("Enter '(' for Open-Bracket")
print("Enter ')' for End-Bracket")
print("Enter '=' for Equal")
print("Enter 'E' for End")
print("Enter your expression:")
Calculator()
