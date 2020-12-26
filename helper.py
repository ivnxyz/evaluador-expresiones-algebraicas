# Indica si un string es en realidad un número
def is_number(string):
  try:
    float(string)
    return True
  except:
    return False

# Regresa la posición en la jerarquía de algún operador
def get_operator_weight(operator):
  if operator == '^': return 3
  elif operator == '*' or operator == '/': return 2
  elif operator == '+' or operator == '-': return 1
  else: return 0