from Stack import Stack
from operators import OPERATORS, get_operator_weight
from characters import LOWER_CASE_LETTERS, UPPER_CASE_LETTERS

def infix_to_postfix(expression: str):
  stack=Stack()
  output = [] #RESULTADO
  for ch in expression:
    if ch not in OPERATORS: #practicamente si lo que esta en la operacion es un numero lo pnes en el stack
      output.append(ch)
    elif ch=='(':  # poner operadores en el stack
      stack.push('(')
    elif ch==')':
      while not stack.is_empty() and stack.last().data != '(':#si no esta vacia y si el ultimo del stack no es '('
        output.append(stack.pop().data)
      stack.pop().data
    else:
      #manejar operandos con menor prioridad y ponerlos en el output
      while not stack.is_empty() and stack.last()!='(' and get_operator_weight(ch) <= get_operator_weight(stack.last().data):
        output.append(stack.pop().data) 
      stack.push(ch)
  while not stack.is_empty():
    output.append(stack.pop().data) 
  return output