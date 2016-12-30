
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '9195A5F7E05E627AC0F404F95AEB41BA'
    
_lr_action_items = {'NAME':([0,2,5,7,11,12,13,14,],[1,8,8,8,8,8,8,8,]),')':([3,8,9,10,16,17,18,19,20,],[-9,-10,-7,16,-8,-4,-3,-5,-6,]),'(':([0,2,5,7,11,12,13,14,],[5,5,5,5,5,5,5,5,]),'+':([1,3,6,8,9,10,15,16,17,18,19,20,],[-10,-9,12,-10,-7,12,12,-8,-4,-3,-5,-6,]),'*':([1,3,6,8,9,10,15,16,17,18,19,20,],[-10,-9,13,-10,-7,13,13,-8,13,13,-5,-6,]),'-':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[2,-10,2,-9,2,11,2,-10,-7,11,2,2,2,2,11,-8,-4,-3,-5,-6,]),'NUMBER':([0,2,5,7,11,12,13,14,],[3,3,3,3,3,3,3,3,]),'/':([1,3,6,8,9,10,15,16,17,18,19,20,],[-10,-9,14,-10,-7,14,14,-8,14,14,-5,-6,]),'=':([1,],[7,]),'$end':([1,3,4,6,8,9,15,16,17,18,19,20,],[-10,-9,0,-2,-10,-7,-1,-8,-4,-3,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,5,7,11,12,13,14,],[6,9,10,15,17,18,19,20,]),'statement':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','lex.py',59),
  ('statement -> expression','statement',1,'p_statement_expr','lex.py',64),
  ('expression -> expression + expression','expression',3,'p_expression_binop','lex.py',69),
  ('expression -> expression - expression','expression',3,'p_expression_binop','lex.py',70),
  ('expression -> expression * expression','expression',3,'p_expression_binop','lex.py',71),
  ('expression -> expression / expression','expression',3,'p_expression_binop','lex.py',72),
  ('expression -> - expression','expression',2,'p_expression_uminus','lex.py',84),
  ('expression -> ( expression )','expression',3,'p_expression_group','lex.py',89),
  ('expression -> NUMBER','expression',1,'p_expression_number','lex.py',94),
  ('expression -> NAME','expression',1,'p_expression_name','lex.py',99),
]
