# Operadores permitidos
OPERATORS = [
  '^',
  '*',
  '/',
  '+',
  '-'
]

# Regresa la posición en la jerarquía de algún operador
def get_operator_weight(operator):
  if operator == '^': return 3
  elif operator == '*' or operator == '/': return 2
  elif operator == '+' or operator == '-': return 1
  else: return 0

# Función de suma
addition = lambda x, y: x + y
# Función de resta
subtraction = lambda x, y: x - y
# Función de multiplicación
multiplication = lambda x, y: x * y
# Función de división
division = lambda x, y: x / y
# Función de elevar a una potencia
power = lambda x, y: x ** y

# Devuelve la función correspondiente al caracter dado
def get_operator_related_function(operator:str):
  if operator == '^':
    return power
  elif operator == '*':
    return multiplication
  elif operator == '/':
    return division
  elif operator == '+':
    return addition
  elif operator == '-':
    return subtraction
  else:
    raise "Operador desconocido"