'''
  Archivo principal para el menú e interactuar con los otros paquetes
'''

# Importar dependencias
from operators import OPERATORS
from prefix import infix_to_prefix

# Pide un polinomio al usuario y limpia la entrada
def ask_for_polynomial():
  polynomial = input('Ingresa el polinomio: ')

  # Eliminar espacios innecesarios
  polynomial = polynomial.replace(' ', '')
  clear_polynomial = ''

  # Insertar espacios al rededor de los operadores y paréntesis
  for char in polynomial:
    if char in OPERATORS or char in '()':
      clear_polynomial += ' {} '.format(char)
    else:
      clear_polynomial += char

  return clear_polynomial

# Punto de entrada al programa
if __name__ == "__main__":
  polynomial = ask_for_polynomial()
  prefix_expression = infix_to_prefix(polynomial)
  print(prefix_expression)