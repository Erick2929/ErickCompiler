
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEANDORnonassocL_PARENR_PARENAND ASSIGN BOOL CHAR COLON COMMA DECREMENT DIVIDE DOUBLE ELSE EQUAL FLOAT FOR GREATER GREATER_EQUAL IDENTIFIER IF INCREMENT INT LESS LESS_EQUAL LOGICAL_AND LOGICAL_NOT LOGICAL_OR L_BRACE L_BRACKET L_PAREN MAIN MINUS MODULO NOT NOT_EQUAL OR PLUS PROGRAM RETURN R_BRACE R_BRACKET R_PAREN SEMICOLON STRING TIMES WHILE WRITE WRITELNprogram : PROGRAM MAIN L_BRACE expressions R_BRACEexpressions : expressions expressionexpressions : expression\n    expression : var_declaration SEMICOLON\n               | write SEMICOLON\n               | writeln SEMICOLON\n               | statement SEMICOLON\n               | if_else_statement\n               | for_loop\n               | while_loop\n               | empty\n    write : WRITE L_PAREN statement R_PARENwriteln : WRITELN L_PAREN statement R_PARENstatement : IDENTIFIER\n    statement : statement PLUS statement\n              | statement MINUS statement\n              | statement TIMES statement\n              | statement DIVIDE statement\n              | statement MODULO statement\n              | statement EQUAL statement\n              | statement NOT_EQUAL statement\n              | statement GREATER statement\n              | statement LESS statement\n              | statement GREATER_EQUAL statement\n              | statement LESS_EQUAL statement\n              | statement AND statement\n              | statement OR statement\n              | statement LOGICAL_AND statement\n              | statement LOGICAL_OR statement\n              | INT\n              | FLOAT\n              | BOOL\n              | STRING\n    \n    statement : L_PAREN statement R_PAREN\n              | L_PAREN conditional R_PAREN\n    statement : IDENTIFIER INCREMENTstatement : IDENTIFIER DECREMENT\n    conditional : conditional EQUAL conditional\n                | conditional NOT_EQUAL conditional\n                | conditional GREATER conditional\n                | conditional LESS conditional\n                | conditional GREATER_EQUAL conditional\n                | conditional LESS_EQUAL conditional\n                | conditional AND conditional\n                | conditional LOGICAL_AND conditional\n                | conditional OR conditional\n                | conditional LOGICAL_OR conditional\n                | statement\n    for_loop : FOR L_PAREN var_declaration SEMICOLON conditional SEMICOLON statement R_PAREN L_BRACE expressions R_BRACEwhile_loop : WHILE L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE\n    if_else_statement : IF L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE ELSE L_BRACE expressions R_BRACE\n                      | IF L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE\n    var_declaration : data_type declarations\n    data_type : INT\n               | FLOAT\n               | BOOL\n               | STRING\n    \n    declarations : IDENTIFIER COMMA declarations\n                 | IDENTIFIER\n    var_declaration : IDENTIFIER ASSIGN statement\n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,27,],[0,-1,]),'MAIN':([2,],[3,]),'L_BRACE':([3,118,120,130,131,],[4,121,123,132,133,]),'IDENTIFIER':([4,5,6,11,12,13,14,15,18,20,21,22,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,63,64,80,85,86,87,88,89,90,91,92,93,94,100,101,102,103,119,121,123,124,125,126,127,129,132,133,134,135,136,137,],[16,16,-3,-8,-9,-10,-11,49,56,-54,-55,-56,-57,-2,-4,-5,-6,-7,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,99,56,49,56,56,56,56,56,56,56,56,56,56,-54,-55,-56,-57,56,16,16,16,56,16,-52,-50,16,16,16,16,-51,-49,]),'WRITE':([4,5,6,11,12,13,14,28,29,30,31,32,121,123,124,126,127,129,132,133,134,135,136,137,],[17,17,-3,-8,-9,-10,-11,-2,-4,-5,-6,-7,17,17,17,17,-52,-50,17,17,17,17,-51,-49,]),'WRITELN':([4,5,6,11,12,13,14,28,29,30,31,32,121,123,124,126,127,129,132,133,134,135,136,137,],[19,19,-3,-8,-9,-10,-11,-2,-4,-5,-6,-7,19,19,19,19,-52,-50,19,19,19,19,-51,-49,]),'INT':([4,5,6,11,12,13,14,18,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,63,64,85,86,87,88,89,90,91,92,93,94,119,121,123,124,125,126,127,129,132,133,134,135,136,137,],[20,20,-3,-8,-9,-10,-11,57,-2,-4,-5,-6,-7,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,100,57,57,57,57,57,57,57,57,57,57,57,57,20,20,20,57,20,-52,-50,20,20,20,20,-51,-49,]),'FLOAT':([4,5,6,11,12,13,14,18,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,63,64,85,86,87,88,89,90,91,92,93,94,119,121,123,124,125,126,127,129,132,133,134,135,136,137,],[21,21,-3,-8,-9,-10,-11,58,-2,-4,-5,-6,-7,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,101,58,58,58,58,58,58,58,58,58,58,58,58,21,21,21,58,21,-52,-50,21,21,21,21,-51,-49,]),'BOOL':([4,5,6,11,12,13,14,18,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,63,64,85,86,87,88,89,90,91,92,93,94,119,121,123,124,125,126,127,129,132,133,134,135,136,137,],[22,22,-3,-8,-9,-10,-11,59,-2,-4,-5,-6,-7,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,102,59,59,59,59,59,59,59,59,59,59,59,59,22,22,22,59,22,-52,-50,22,22,22,22,-51,-49,]),'STRING':([4,5,6,11,12,13,14,18,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,63,64,85,86,87,88,89,90,91,92,93,94,119,121,123,124,125,126,127,129,132,133,134,135,136,137,],[23,23,-3,-8,-9,-10,-11,60,-2,-4,-5,-6,-7,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,103,60,60,60,60,60,60,60,60,60,60,60,60,23,23,23,60,23,-52,-50,23,23,23,23,-51,-49,]),'L_PAREN':([4,5,6,11,12,13,14,17,18,19,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,64,85,86,87,88,89,90,91,92,93,94,119,121,123,124,125,126,127,129,132,133,134,135,136,137,],[18,18,-3,-8,-9,-10,-11,53,18,61,62,63,64,-2,-4,-5,-6,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-52,-50,18,18,18,18,-51,-49,]),'IF':([4,5,6,11,12,13,14,28,29,30,31,32,121,123,124,126,127,129,132,133,134,135,136,137,],[24,24,-3,-8,-9,-10,-11,-2,-4,-5,-6,-7,24,24,24,24,-52,-50,24,24,24,24,-51,-49,]),'FOR':([4,5,6,11,12,13,14,28,29,30,31,32,121,123,124,126,127,129,132,133,134,135,136,137,],[25,25,-3,-8,-9,-10,-11,-2,-4,-5,-6,-7,25,25,25,25,-52,-50,25,25,25,25,-51,-49,]),'WHILE':([4,5,6,11,12,13,14,28,29,30,31,32,121,123,124,126,127,129,132,133,134,135,136,137,],[26,26,-3,-8,-9,-10,-11,-2,-4,-5,-6,-7,26,26,26,26,-52,-50,26,26,26,26,-51,-49,]),'R_BRACE':([4,5,6,11,12,13,14,28,29,30,31,32,121,123,124,126,127,129,132,133,134,135,136,137,],[-61,27,-3,-8,-9,-10,-11,-2,-4,-5,-6,-7,-61,-61,127,129,-52,-50,-61,-61,136,137,-51,-49,]),'SEMICOLON':([7,8,9,10,16,20,21,22,23,48,49,51,52,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,83,84,97,98,105,106,107,108,109,110,111,112,113,114,115,116,117,122,],[29,30,31,32,-14,-30,-31,-32,-33,-53,-59,-36,-37,-14,-30,-31,-32,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-60,-34,-35,-48,119,-58,-12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-13,125,]),'PLUS':([10,16,20,21,22,23,51,52,54,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,97,128,],[33,-14,-30,-31,-32,-33,-36,-37,33,-14,-30,-31,-32,-33,-15,-16,-17,-18,33,33,33,33,33,33,33,-26,-27,33,33,33,33,-34,-35,33,33,33,]),'MINUS':([10,16,20,21,22,23,51,52,54,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,97,128,],[34,-14,-30,-31,-32,-33,-36,-37,34,-14,-30,-31,-32,-33,-15,-16,-17,-18,34,34,34,34,34,34,34,-26,-27,34,34,34,34,-34,-35,34,34,34,]),'TIMES':([10,16,20,21,22,23,51,52,54,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,97,128,],[35,-14,-30,-31,-32,-33,-36,-37,35,-14,-30,-31,-32,-33,35,35,-17,-18,35,35,35,35,35,35,35,-26,-27,35,35,35,35,-34,-35,35,35,35,]),'DIVIDE':([10,16,20,21,22,23,51,52,54,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,97,128,],[36,-14,-30,-31,-32,-33,-36,-37,36,-14,-30,-31,-32,-33,36,36,-17,-18,36,36,36,36,36,36,36,-26,-27,36,36,36,36,-34,-35,36,36,36,]),'MODULO':([10,16,20,21,22,23,51,52,54,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,97,128,],[37,-14,-30,-31,-32,-33,-36,-37,37,-14,-30,-31,-32,-33,-15,-16,-17,-18,37,37,37,37,37,37,37,-26,-27,37,37,37,37,-34,-35,37,37,37,]),'EQUAL':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[38,-14,-30,-31,-32,-33,-36,-37,38,85,-14,-30,-31,-32,-33,-15,-16,-17,-18,38,38,38,38,38,38,38,-26,-27,38,38,38,38,-34,-35,38,85,38,85,85,85,85,85,85,85,-44,85,-46,85,85,38,]),'NOT_EQUAL':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[39,-14,-30,-31,-32,-33,-36,-37,39,86,-14,-30,-31,-32,-33,-15,-16,-17,-18,39,39,39,39,39,39,39,-26,-27,39,39,39,39,-34,-35,39,86,39,86,86,86,86,86,86,86,-44,86,-46,86,86,39,]),'GREATER':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[40,-14,-30,-31,-32,-33,-36,-37,40,87,-14,-30,-31,-32,-33,-15,-16,-17,-18,40,40,40,40,40,40,40,-26,-27,40,40,40,40,-34,-35,40,87,40,87,87,87,87,87,87,87,-44,87,-46,87,87,40,]),'LESS':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[41,-14,-30,-31,-32,-33,-36,-37,41,88,-14,-30,-31,-32,-33,-15,-16,-17,-18,41,41,41,41,41,41,41,-26,-27,41,41,41,41,-34,-35,41,88,41,88,88,88,88,88,88,88,-44,88,-46,88,88,41,]),'GREATER_EQUAL':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[42,-14,-30,-31,-32,-33,-36,-37,42,89,-14,-30,-31,-32,-33,-15,-16,-17,-18,42,42,42,42,42,42,42,-26,-27,42,42,42,42,-34,-35,42,89,42,89,89,89,89,89,89,89,-44,89,-46,89,89,42,]),'LESS_EQUAL':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[43,-14,-30,-31,-32,-33,-36,-37,43,90,-14,-30,-31,-32,-33,-15,-16,-17,-18,43,43,43,43,43,43,43,-26,-27,43,43,43,43,-34,-35,43,90,43,90,90,90,90,90,90,90,-44,90,-46,90,90,43,]),'AND':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[44,-14,-30,-31,-32,-33,-36,-37,44,91,-14,-30,-31,-32,-33,44,44,-17,-18,44,44,44,44,44,44,44,-26,-27,44,44,44,44,-34,-35,44,91,44,91,91,91,91,91,91,91,-44,91,-46,91,91,44,]),'OR':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[45,-14,-30,-31,-32,-33,-36,-37,45,93,-14,-30,-31,-32,-33,45,45,-17,-18,45,45,45,45,45,45,45,-26,-27,45,45,45,45,-34,-35,45,93,45,93,93,93,93,93,93,93,-44,93,-46,93,93,45,]),'LOGICAL_AND':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[46,-14,-30,-31,-32,-33,-36,-37,46,92,-14,-30,-31,-32,-33,-15,-16,-17,-18,46,46,46,46,46,46,46,-26,-27,46,46,46,46,-34,-35,46,92,46,92,92,92,92,92,92,92,-44,92,-46,92,92,46,]),'LOGICAL_OR':([10,16,20,21,22,23,51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,122,128,],[47,-14,-30,-31,-32,-33,-36,-37,47,94,-14,-30,-31,-32,-33,-15,-16,-17,-18,47,47,47,47,47,47,47,-26,-27,47,47,47,47,-34,-35,47,94,47,94,94,94,94,94,94,94,-44,94,-46,94,94,47,]),'ASSIGN':([16,99,],[50,50,]),'INCREMENT':([16,56,],[51,51,]),'DECREMENT':([16,56,],[52,52,]),'COMMA':([49,],[80,]),'R_PAREN':([51,52,54,55,56,57,58,59,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,84,95,96,97,104,107,108,109,110,111,112,113,114,115,116,128,],[-36,-37,83,84,-14,-30,-31,-32,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,106,-34,-35,117,118,-48,120,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,131,]),'ELSE':([127,],[130,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'expressions':([4,121,123,132,133,],[5,124,126,134,135,]),'expression':([4,5,121,123,124,126,132,133,134,135,],[6,28,6,6,28,28,6,6,28,28,]),'var_declaration':([4,5,63,121,123,124,126,132,133,134,135,],[7,7,98,7,7,7,7,7,7,7,7,]),'write':([4,5,121,123,124,126,132,133,134,135,],[8,8,8,8,8,8,8,8,8,8,]),'writeln':([4,5,121,123,124,126,132,133,134,135,],[9,9,9,9,9,9,9,9,9,9,]),'statement':([4,5,18,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,50,53,61,62,64,85,86,87,88,89,90,91,92,93,94,119,121,123,124,125,126,132,133,134,135,],[10,10,54,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,95,97,97,97,97,97,97,97,97,97,97,97,97,97,10,10,10,128,10,10,10,10,10,]),'if_else_statement':([4,5,121,123,124,126,132,133,134,135,],[11,11,11,11,11,11,11,11,11,11,]),'for_loop':([4,5,121,123,124,126,132,133,134,135,],[12,12,12,12,12,12,12,12,12,12,]),'while_loop':([4,5,121,123,124,126,132,133,134,135,],[13,13,13,13,13,13,13,13,13,13,]),'empty':([4,5,121,123,124,126,132,133,134,135,],[14,14,14,14,14,14,14,14,14,14,]),'data_type':([4,5,63,121,123,124,126,132,133,134,135,],[15,15,15,15,15,15,15,15,15,15,15,]),'declarations':([15,80,],[48,105,]),'conditional':([18,62,64,85,86,87,88,89,90,91,92,93,94,119,],[55,96,104,107,108,109,110,111,112,113,114,115,116,122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM MAIN L_BRACE expressions R_BRACE','program',5,'p_init','yacc.py',20),
  ('expressions -> expressions expression','expressions',2,'p_expressions','yacc.py',31),
  ('expressions -> expression','expressions',1,'p_expressions_expression','yacc.py',37),
  ('expression -> var_declaration SEMICOLON','expression',2,'p_expression','yacc.py',43),
  ('expression -> write SEMICOLON','expression',2,'p_expression','yacc.py',44),
  ('expression -> writeln SEMICOLON','expression',2,'p_expression','yacc.py',45),
  ('expression -> statement SEMICOLON','expression',2,'p_expression','yacc.py',46),
  ('expression -> if_else_statement','expression',1,'p_expression','yacc.py',47),
  ('expression -> for_loop','expression',1,'p_expression','yacc.py',48),
  ('expression -> while_loop','expression',1,'p_expression','yacc.py',49),
  ('expression -> empty','expression',1,'p_expression','yacc.py',50),
  ('write -> WRITE L_PAREN statement R_PAREN','write',4,'p_write','yacc.py',59),
  ('writeln -> WRITELN L_PAREN statement R_PAREN','writeln',4,'p_writeln','yacc.py',64),
  ('statement -> IDENTIFIER','statement',1,'p_statement_variable','yacc.py',72),
  ('statement -> statement PLUS statement','statement',3,'p_statement','yacc.py',78),
  ('statement -> statement MINUS statement','statement',3,'p_statement','yacc.py',79),
  ('statement -> statement TIMES statement','statement',3,'p_statement','yacc.py',80),
  ('statement -> statement DIVIDE statement','statement',3,'p_statement','yacc.py',81),
  ('statement -> statement MODULO statement','statement',3,'p_statement','yacc.py',82),
  ('statement -> statement EQUAL statement','statement',3,'p_statement','yacc.py',83),
  ('statement -> statement NOT_EQUAL statement','statement',3,'p_statement','yacc.py',84),
  ('statement -> statement GREATER statement','statement',3,'p_statement','yacc.py',85),
  ('statement -> statement LESS statement','statement',3,'p_statement','yacc.py',86),
  ('statement -> statement GREATER_EQUAL statement','statement',3,'p_statement','yacc.py',87),
  ('statement -> statement LESS_EQUAL statement','statement',3,'p_statement','yacc.py',88),
  ('statement -> statement AND statement','statement',3,'p_statement','yacc.py',89),
  ('statement -> statement OR statement','statement',3,'p_statement','yacc.py',90),
  ('statement -> statement LOGICAL_AND statement','statement',3,'p_statement','yacc.py',91),
  ('statement -> statement LOGICAL_OR statement','statement',3,'p_statement','yacc.py',92),
  ('statement -> INT','statement',1,'p_statement','yacc.py',93),
  ('statement -> FLOAT','statement',1,'p_statement','yacc.py',94),
  ('statement -> BOOL','statement',1,'p_statement','yacc.py',95),
  ('statement -> STRING','statement',1,'p_statement','yacc.py',96),
  ('statement -> L_PAREN statement R_PAREN','statement',3,'p_statement_parenthesis','yacc.py',106),
  ('statement -> L_PAREN conditional R_PAREN','statement',3,'p_statement_parenthesis','yacc.py',107),
  ('statement -> IDENTIFIER INCREMENT','statement',2,'p_statement_increment','yacc.py',113),
  ('statement -> IDENTIFIER DECREMENT','statement',2,'p_statement_decrement','yacc.py',118),
  ('conditional -> conditional EQUAL conditional','conditional',3,'p_conditional','yacc.py',127),
  ('conditional -> conditional NOT_EQUAL conditional','conditional',3,'p_conditional','yacc.py',128),
  ('conditional -> conditional GREATER conditional','conditional',3,'p_conditional','yacc.py',129),
  ('conditional -> conditional LESS conditional','conditional',3,'p_conditional','yacc.py',130),
  ('conditional -> conditional GREATER_EQUAL conditional','conditional',3,'p_conditional','yacc.py',131),
  ('conditional -> conditional LESS_EQUAL conditional','conditional',3,'p_conditional','yacc.py',132),
  ('conditional -> conditional AND conditional','conditional',3,'p_conditional','yacc.py',133),
  ('conditional -> conditional LOGICAL_AND conditional','conditional',3,'p_conditional','yacc.py',134),
  ('conditional -> conditional OR conditional','conditional',3,'p_conditional','yacc.py',135),
  ('conditional -> conditional LOGICAL_OR conditional','conditional',3,'p_conditional','yacc.py',136),
  ('conditional -> statement','conditional',1,'p_conditional','yacc.py',137),
  ('for_loop -> FOR L_PAREN var_declaration SEMICOLON conditional SEMICOLON statement R_PAREN L_BRACE expressions R_BRACE','for_loop',11,'p_for_loop','yacc.py',149),
  ('while_loop -> WHILE L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE','while_loop',7,'p_while_loop','yacc.py',157),
  ('if_else_statement -> IF L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE ELSE L_BRACE expressions R_BRACE','if_else_statement',11,'p_if_else_statement','yacc.py',166),
  ('if_else_statement -> IF L_PAREN conditional R_PAREN L_BRACE expressions R_BRACE','if_else_statement',7,'p_if_else_statement','yacc.py',167),
  ('var_declaration -> data_type declarations','var_declaration',2,'p_variable_declaration','yacc.py',179),
  ('data_type -> INT','data_type',1,'p_data_type','yacc.py',185),
  ('data_type -> FLOAT','data_type',1,'p_data_type','yacc.py',186),
  ('data_type -> BOOL','data_type',1,'p_data_type','yacc.py',187),
  ('data_type -> STRING','data_type',1,'p_data_type','yacc.py',188),
  ('declarations -> IDENTIFIER COMMA declarations','declarations',3,'p_declarations','yacc.py',195),
  ('declarations -> IDENTIFIER','declarations',1,'p_declarations','yacc.py',196),
  ('var_declaration -> IDENTIFIER ASSIGN statement','var_declaration',3,'p_assignment','yacc.py',209),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',218),
]
