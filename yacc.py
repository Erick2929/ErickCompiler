from lexer import tokens

# Erick Siller Ojeda A01382929
# Basado en la documentación de PLY: https://www.dabeaz.com/ply/ply.html#ply_nn0
# ----------------------------------------------------------------------------------------------------------
import ply.yacc as yacc

memoriaVariables = {}  # Diccionario para almacenar las variables

precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE", "AND", "OR"),
    ("nonassoc", "L_PAREN", "R_PAREN"),
)

# ------------------ Program structure ------------------


def p_init(p):
    "program : PROGRAM MAIN L_BRACE expressions R_BRACE"
    for e in p[4]:
        expression = program_driver(e)
        if expression != None:
            print(expression)


# ------------------ Expressions ------------------


def p_expressions(p):
    "expressions : expressions expression"
    p[1].append(p[2])
    p[0] = p[1]


def p_expressions_expression(p):
    "expressions : expression"
    p[0] = [p[1]]


def p_expression(p):
    """
    expression : var_declaration SEMICOLON
               | write SEMICOLON
               | writeln SEMICOLON
               | statement SEMICOLON
               | if_else_statement
               | for_loop
               | while_loop
               | empty
    """
    p[0] = p[1]


# ------------------ definicion de write functions ------------------


def p_write(p):
    "write : WRITE L_PAREN statement R_PAREN"
    p[0] = ("WRITE", p[3])


def p_writeln(p):
    "writeln : WRITELN L_PAREN statement R_PAREN"
    p[0] = ("WRITELN", p[3])


# ------------------ definicion de statements ------------------


def p_statement_variable(p):
    "statement : IDENTIFIER"
    p[0] = ("VAR", p[1])


def p_statement(p):
    """
    statement : statement PLUS statement
              | statement MINUS statement
              | statement TIMES statement
              | statement DIVIDE statement
              | INT
              | FLOAT
              | BOOL
              | STRING
    """
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_statement_parenthesis(p):
    """
    statement : L_PAREN statement R_PAREN
              | L_PAREN conditional R_PAREN
    """
    p[0] = p[2]


def p_statement_increment(p):
    "statement : IDENTIFIER INCREMENT"
    p[0] = ("VAR_ASSIGN", p[1], ("+", ("VAR", p[1]), 1))


def p_statement_decrement(p):
    "statement : IDENTIFIER DECREMENT"
    p[0] = ("VAR_ASSIGN", p[1], ("-", ("VAR", p[1]), 1))


# ------------------ definicion de conditional ------------------


def p_conditional(p):
    """
    conditional : conditional EQUAL conditional
                | conditional NOT_EQUAL conditional
                | conditional GREATER conditional
                | conditional LESS conditional
                | conditional GREATER_EQUAL conditional
                | conditional LESS_EQUAL conditional
                | conditional AND conditional
                | conditional OR conditional
                | TRUE
                | FALSE
                | statement
    """
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


# ------------------ definicion de for loop ------------------


def p_for_loop(p):
    "for_loop : FOR L_PAREN var_declaration SEMICOLON conditional SEMICOLON statement R_PAREN L_BRACE expressions R_BRACE"
    p[0] = ("FOR", [p[3], p[5], p[7]], p[10])


# ------------------ definicion de while loop ------------------


def p_while_loop(p):
    "while_loop : WHILE L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE"
    p[0] = ("WHILE", p[3], p[6])


# ------------------ definicion de if else statement ------------------


def p_if_else_statement(p):
    """
    if_else_statement : IF L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE ELSE L_BRACE expressions R_BRACE
                      | IF L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE
    """
    if len(p) == 12:
        p[0] = ("IF", p[3], p[6], p[10])
    else:
        p[0] = ("IF", p[3], p[6])


# ------------------ Definicion de Variable declaration ------------------


def p_variable_declaration(p):
    "var_declaration : data_type declarations"
    p[0] = ("VAR_DECLARATION", p[1], p[2])


def p_data_type(p):
    """
    data_type : INT
               | FLOAT
               | BOOL
               | STRING
    """
    p[0] = p[1]


def p_declarations(p):
    """
    declarations : IDENTIFIER COMMA declarations
                 | IDENTIFIER
    """
    if len(p) == 4:
        p[3].append(p[1])
        p[0] = p[3]
    else:
        p[0] = [p[1]]


# ------------------ definicion de Variable assignment ------------------


def p_assignment(p):
    "var_declaration : IDENTIFIER ASSIGN statement"
    p[0] = ("VAR_ASSIGN", p[1], p[3])


# ------------------------- definicion de expresion vacia -------------------------


def p_empty(p):
    """
    empty :
    """
    p[0] = ""


# ------------------ Error handling ------------------


def p_error(p):
    if p:
        raise SyntaxError(
            "Error de sintaxis: el token '%s' en la linea %d" % (p.value, p.lineno)
        )
    else:
        print("Error de sintaxis en EOF")


parser = yacc.yacc()

# ------------------ funciones -----------------------


def binary_operations(p):
    if p[0] == "+":
        return program_driver(p[1]) + program_driver(p[2])
    elif p[0] == "-":
        return program_driver(p[1]) - program_driver(p[2])
    elif p[0] == "*":
        return program_driver(p[1]) * program_driver(p[2])
    elif p[0] == "/":
        return program_driver(p[1]) / program_driver(p[2])
    elif p[0] == "==":
        return program_driver(p[1]) == program_driver(p[2])
    elif p[0] == "!=":
        return program_driver(p[1]) != program_driver(p[2])
    elif p[0] == ">":
        return program_driver(p[1]) > program_driver(p[2])
    elif p[0] == "<":
        return program_driver(p[1]) < program_driver(p[2])
    elif p[0] == ">=":
        return program_driver(p[1]) >= program_driver(p[2])
    elif p[0] == "<=":
        return program_driver(p[1]) <= program_driver(p[2])
    elif p[0] == "and":
        return program_driver(p[1]) and program_driver(p[2])
    elif p[0] == "or":
        return program_driver(p[1]) or program_driver(p[2])


# ------------------ asignacion de variables ------------------


def variable_assignment(p):
    if p[1] not in memoriaVariables:
        raise NameError("'%s' no esta declarado" % (p[1]))
    value = program_driver(p[2])
    if type(value).__name__ == "str":
        dataType = "string"
    else:
        dataType = type(value).__name__

    if dataType == memoriaVariables[p[1]]["dataType"]:
        if type(value) == str:
            memoriaVariables[p[1]]["value"] = value.strip('"')
        else:
            memoriaVariables[p[1]]["value"] = value
    else:
        if dataType == "int":
            if memoriaVariables[p[1]]["dataType"] == "float":
                memoriaVariables[p[1]]["value"] = float(value)
            else:
                raise TypeError(
                    "El valor asignado no es de tipo 'int' en la variable de tipo '%s'"
                    % (dataType)
                )
        elif dataType == "float":
            raise TypeError(
                "El valor asignado no es de tipo 'float' en la variable de tipo '%s'"
                % (dataType)
            )
        elif dataType == "string":
            raise TypeError(
                "El valor asignado no es de tipo 'string' en la variable de tipo '%s'"
                % (dataType)
            )
        elif dataType == "bool":
            raise TypeError(
                "El valor asignado no es de tipo 'bool' en la variable de tipo '%s'"
                % (dataType)
            )


def variable_declaration(p):
    for v in p[2]:
        if v not in memoriaVariables:
            memoriaVariables[v] = {"dataType": p[1], "value": None}


def variable_value(p):
    if p[1] not in memoriaVariables:
        raise NameError("'%s' no esta declarado" % (p[1]))
    if memoriaVariables[p[1]]["value"] == None:
        raise NameError("'%s' no esta definido" % (p[1]))
    return memoriaVariables[p[1]]["value"]


# ------------------ executable functions ------------------


def execute(expressions):
    for e in expressions:
        program_driver(e)


def for_loop(p):
    init = program_driver(p[1][0])
    condition = program_driver(p[1][1])
    while condition:
        execute(p[2])
        program_driver(p[1][2])
        condition = program_driver(p[1][1])


def while_loop(p):
    if type(p[1]) != str and len(p[1]) < 3:
        while program_driver(p[1]):
            execute(p[2])
    else:
        operator = p[1][0]
        while program_driver(
            (operator, program_driver(p[1][1]), program_driver(p[1][2]))
        ):
            execute(p[2])


def if_else_statement(p):
    if len(p[1]) == 3:
        operator = p[1][0]
        left = p[1][1]
        right = p[1][2]
        condition = program_driver(
            (operator, program_driver(left), program_driver(right))
        )
        if len(p) == 3:
            if condition:
                return execute(p[2])
        else:
            if condition:
                return execute(p[2])
            else:
                return execute(p[3])
    else:
        condition = program_driver(p[1])
        if len(p) == 3:
            if condition:
                return execute(p[2])
        else:
            if condition:
                return execute(p[2])
            else:
                return execute(p[3])


def write_function(p):
    print(program_driver(p[1]), end="")


def writeln_function(p):
    print(program_driver(p[1]))


def program_driver(p):
    if type(p) == tuple:
        operators = ["+", "-", "*", "/", "==", "!=", ">", "<", ">=", "<=", "and", "or"]
        if p[0] in operators:
            return binary_operations(p)
        elif p[0] == "VAR_ASSIGN":
            return variable_assignment(p)
        elif p[0] == "VAR_DECLARATION":
            return variable_declaration(p)
        elif p[0] == "VAR":
            return variable_value(p)
        elif p[0] == "IF":
            return if_else_statement(p)
        elif p[0] == "FOR":
            return for_loop(p)
        elif p[0] == "WHILE":
            return while_loop(p)
        elif p[0] == "WRITE":
            return write_function(p)
        elif p[0] == "WRITELN":
            return writeln_function(p)
    else:
        return p


with open("tests/writes/write.txt", "r") as file:
    s = file.read()
    result = parser.parse(s)
