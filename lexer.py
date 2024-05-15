# Erick Siller Ojeda A01382929
# Basado en la documentación de PLY: https://www.dabeaz.com/ply/ply.html#ply_nn0
# ----------------------------------------------------------------------------------------------------------
import ply.lex as lex

reserved = {
    # palabras de inicializacion
    "program": "PROGRAM",
    "main": "MAIN",
    # condicionales
    "if": "IF",
    "else": "ELSE",
    # ciclos
    "for": "FOR",
    "while": "WHILE",
    # funciones print
    "write": "WRITE",
    "writeln": "WRITELN",
    # tipos de datos
    "int": "INT",
    "float": "FLOAT",
    "bool": "BOOL",
    "string": "STRING",
    # valores booleanos
    "true": "TRUE",
    "false": "FALSE",
    # operadores logicos
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    # retorno de funciones
    "return": "RETURN",
}

tokens = [
    # Inicio
    "IDENTIFIER",
    # Variables
    "ASSIGN",
    # Simbolos
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    "INCREMENT",
    "DECREMENT",
    # Operadores de comparacion
    "EQUAL",
    "NOT_EQUAL",
    "GREATER",
    "LESS",
    "GREATER_EQUAL",
    "LESS_EQUAL",
    # Operadores logicos
    "LOGICAL_AND",
    "LOGICAL_OR",
    "LOGICAL_NOT",
    # Simbolos especiales
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


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, t.type)
    return t


def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r"\d+\.\d*"
    t.value = float(t.value)
    return t


def t_STRING(t):
    r'"(?:\\"|.)*?"'
    t.value = str(t.value)
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_comment(t):
    r"//.*"
    pass


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

with open("tests/variables/var.txt", "r") as file:
    data = file.read()

lexer.input(data)

# Tokenize


# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)
