# Importar dependencias
from postfix import infix_to_postfix

# Traduce una expresión de infijo a prefijo
def infix_to_prefix(infix_expression: str):
  # Invertir la expresión
  reversed_expression = []

  for character in infix_expression[::-1]:
    # Reemplazar paréntesis
    if character == '(':
      reversed_expression.append(')')
    elif character == ')':
      reversed_expression.append('(')
    else:
      reversed_expression.append(character)
  
  posfix_expression = infix_to_postfix(''.join(reversed_expression))
  return posfix_expression[::-1]
