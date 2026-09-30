from data_structures.stack import Stack


class SyntaxValidator:
    #Validador de sintaxis de delimitadores utilizando Pila propia
    def __init__(self):
        self.opening_symbols = "({["
        self.closing_symbols = ")}]"
        self.matching_pairs = {')': '(', '}': '{', ']': '['}

    def validate(self, code_text):
        #Valida el balanceo de delimitadores indicando linea y caracter si hay error
        if not code_text:
            return True, "El archivo activo esta vacio o no contiene texto."

        stack = Stack()
        lines = code_text.splitlines()

        for line_index, line in enumerate(lines, start=1):
            for char_index, char in enumerate(line, start=1):
                if char in self.opening_symbols:
                    stack.push((char, line_index, char_index))
                elif char in self.closing_symbols:
                    if stack.is_empty():
                        return False, f"Error de sintaxis: Simbolo '{char}' no esperado en la linea {line_index}, caracter {char_index}."

                    top_char, top_line, top_col = stack.pop()
                    if top_char != self.matching_pairs[char]:
                        return False, f"Error de sintaxis: Se esperaba el cierre de '{top_char}' (linea {top_line}) pero se encontro '{char}' en la linea {line_index}, caracter {char_index}."

        if not stack.is_empty():
            unclosed_char, line_num, col_num = stack.pop()
            return False, f"Error de sintaxis: El simbolo '{unclosed_char}' en la linea {line_num}, caracter {col_num} no fue cerrado."

        return True, "Sintaxis de delimitadores correcta: Todos los simbolos estan balanceados."
