# Erick Siller Ojeda A01382929
# Basado en la documentación de PLY: https://www.dabeaz.com/ply/ply.html#ply_nn0
# ----------------------------------------------------------------------------------------------------------

import ply.lex as lex

# Palabras reservadas del lenguaje
reserved = {
    # Palabras de inicialización
    "program": "PROGRAM",
    "main": "MAIN",
    # Condicionales
    "if": "IF",
    "else": "ELSE",
    # Ciclos
    "for": "FOR",
    "while": "WHILE",
    # Funciones print
    "write": "WRITE",
    "writeln": "WRITELN",
    # Tipos de datos
    "int": "INT",
    "float": "FLOAT",
    "bool": "BOOL",
    "string": "STRING",
    # Valores booleanos
    "true": "TRUE",
    "false": "FALSE",
    # Operadores lógicos
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    # Retorno de funciones
    "return": "RETURN",
}

# Lista de tokens
tokens = [
    # Inicio
    "IDENTIFIER",
    # Variables
    "ASSIGN",
    # Símbolos
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    "INCREMENT",
    "DECREMENT",
    # Operadores de comparación
    "EQUAL",
    "NOT_EQUAL",
    "GREATER",
    "LESS",
    "GREATER_EQUAL",
    "LESS_EQUAL",
    # Operadores lógicos
    "LOGICAL_AND",
    "LOGICAL_OR",
    "LOGICAL_NOT",
    # Símbolos especiales
    "SEMICOLON",
    "COLON",
    "COMMA",
    "L_PAREN",
    "R_PAREN",
    "L_BRACE",
    "R_BRACE",
    "L_BRACKET",
    "R_BRACKET",
] + list(reserved.values())

# Expresiones regulares para los tokens
t_ASSIGN = r"="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULO = r"%"
t_INCREMENT = r"\+\+"
t_DECREMENT = r"--"
t_EQUAL = r"=="
t_NOT_EQUAL = r"!="
t_GREATER = r">"
t_LESS = r"<"
t_GREATER_EQUAL = r">="
t_LESS_EQUAL = r"<="
t_LOGICAL_AND = r"&&"
t_LOGICAL_OR = r"\|\|"
t_LOGICAL_NOT = r"!"
t_SEMICOLON = r";"
t_COLON = r":"
t_COMMA = r","
t_L_PAREN = r"\("
t_R_PAREN = r"\)"
t_L_BRACE = r"\{"
t_R_BRACE = r"\}"
t_L_BRACKET = r"\["
t_R_BRACKET = r"\]"


# Token para identificadores
def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, t.type)  # Verifica si es una palabra reservada
    return t


# Token para números enteros
def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Token para números de punto flotante
def t_FLOAT(t):
    r"\d+\.\d*"
    t.value = float(t.value)
    return t


# Token para cadenas de texto
def t_STRING(t):
    r'"(?:\\"|.)*?"'
    t.value = str(t.value)
    return t


# Token para saltos de línea
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Ignorar espacios y tabulaciones
t_ignore = " \t"


# Ignorar comentarios
def t_comment(t):
    r"//.*"
    pass


# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


# Crear el lexer
lexer = lex.lex()

# Leer el archivo de entrada
with open("tests/while/test.txt", "r") as file:
    data = file.read()

# Inicializar el lexer con los datos de entrada
lexer.input(data)

# Tokenizar el código de entrada
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)
