'''
  Este archivo contiene las funciones para evaluar una expresión algebráica
  previamente traducida a posfijo. También hay una función para pedirle la usuario
  los valores de las incógnitas.
'''

# Importar dependencias
from Stack import Stack, Node
from operators import OPERATORS, get_operator_related_function
from helper import is_number

# Obtiene las incóngnitas que se deben pedir al usuario
def identify_variables(prefix_expression:str) -> [str]:
  variables = []

  for char in prefix_expression.split():
    if not (char in OPERATORS or char in '() ' or is_number(char) or char in variables):
      variables.append(char)
  
  return variables

# Le pide el valor de las incógnitas al usuario
def ask_for_variables(variables:[str]) -> dict:
  # Almacenar las variables que se pedirán
  variables_dict = {}

  for variable in variables:
    value = float(input('Ingresa el valor de {}: '.format(variable)))
    variables_dict[variable] = value
  
  return variables_dict

# Evalúa una expresión en prefijo
def evaluate_prefix_expression(prefix_expression:str, variables:dict) -> float:
  # Dividir expresión por espacios y voltear la expresión
  characters = prefix_expression.split()[::-1]

  # Crear un Stack
  evaluation_stack = Stack()

  # Iterar por los caracteres
  for char in characters:
    # Verificar el tipo de caracter
    if is_number(char):
      evaluation_stack.push(float(char))
    elif char in variables:
      evaluation_stack.push(variables[char])
    # Asumir que es un operador
    else:
      # Obtener los últimos dos elementos
      first_operand = evaluation_stack.pop()
      second_operand = evaluation_stack.pop()

      # Obtiene la operación a realizar
      fn = get_operator_related_function(char)

      # Realiza la operación
      result = fn(first_operand.data, second_operand.data)
      evaluation_stack.push(result)
  
  return evaluation_stack.pop().data