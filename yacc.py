# Erick Siller Ojeda A01382929
# Basado en la documentación de PLY: https://www.dabeaz.com/ply/ply.html#ply_nn0
# ----------------------------------------------------------------------------------------------------------
import ply.yacc as yacc
from lexer import tokens

memoriaVariables = {}


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


# ------------------ Variable declaration ------------------


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


# def p_expression(p):
#     """
#     expression : var_declaration
#                | if_statement
#                | for_loop
#                | while_loop
#                | print
#                | empty
#     """
#     p[0] = p[1]


# ------------------------- expresion vacia -------------------------
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

# ------------------ rule functions -----------------------


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
        # if type(p[1]).__name__ == "int" or type(p[2]).__name__ == "int":
        #     raise RuntimeError("Illegal AND evaluation")
        # else:
        return program_driver(p[1]) and program_driver(p[2])
    elif p[0] == "or":
        # if type(p[1]).__name__ == "int" or type(p[2]).__name__ == "int":
        #     raise RuntimeError("Illegal OR evaluation")
        # else:
        return program_driver(p[1]) or program_driver(p[2])


# ------------------ Variables ------------------


def variable_assignment(p):
    if p[1] not in memoriaVariables:
        raise NameError("'%s' no esta declarado" % (p[1]))
    value = program_driver(p[2])
    # hacemos la excepcion de que si es un string, le ponemos el nombre de "string" en vez de "str"
    if type(value).__name__ == "str":
        dataType = "string"
    else:
        dataType = type(value).__name__

    if dataType == memoriaVariables[p[1]]["dataType"]:
        if type(value) == str:
            # agregamos las comillas a los strings
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


# ------------------ functions ------------------


# Excute blocks of code
# def execute(expressions):
#     for e in expressions:
#         program_driver(e)


def write_function(p):
    print(program_driver(p[1]))


def writeln_function(p):
    print(program_driver(p[1]) + "\n")


# MAIN DRIVER: Parse any input and run as it if was a program
def program_driver(p):
    # print("Tuplas: ", p)
    if type(p) == tuple:
        operators = ["+", "-", "*", "/", "==", "!=", ">", "<", ">=", "<=", "and", "or"]
        if p[0] in operators:
            return binary_operations(p)
        elif p[0] == "VAR_ASSING":
            return variable_assignment(p)
        elif p[0] == "VAR_DECLARATION":
            return variable_declaration(p)
        elif p[0] == "VAR":
            return variable_value(p)
        # elif p[0] == "IF":
        #     return if_else_statement(p)
        # elif p[0] == "FOR":
        #     return for_loop(p)
        # elif p[0] == "WHILE":
        #     return while_loop(p)
        elif p[0] == "WRITE":
            return write_function(p)
        elif p[0] == "WRITELN":
            return writeln_function(p)
    else:
        return p


with open("tests/variables/var.txt", "r") as file:
    s = file.read()
    result = parser.parse(s)
    # print(memoriaVariables)
