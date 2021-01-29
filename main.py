'''
  Archivo principal para el menú e interactuar con los otros paquetes
'''

# Importar dependencias
from operators import OPERATORS
from prefix import infix_to_prefix
from postfix import infix_to_postfix
from evaluator import identify_variables, ask_for_variables, evaluate_prefix_expression

# Pide un polinomio al usuario y limpia la entrada
def ask_for_polynomial():
  polynomial = input('Ingresa el polinomio: ')

  # Eliminar espacios innecesarios
  polynomial = polynomial.replace(' ', '')
  clear_polynomial = ''

  if polynomial[0] == '+' or polynomial[0] == '-':
    polynomial = '0' + polynomial

  # Insertar espacios al rededor de los operadores y paréntesis
  for char in polynomial:
    if char in OPERATORS or char in '()':
      clear_polynomial += ' {} '.format(char)
    else:
      clear_polynomial += char

  return clear_polynomial

# Punto de entrada al programa
if __name__ == "__main__":
  # Obtener polinomio
  polynomial = ask_for_polynomial()

  # Traducir a prefijo y posfijo
  prefix_expression = infix_to_prefix(polynomial)
  postfix_expression = infix_to_postfix(polynomial)

  print("\n**** TRADUCCIÓN ****")
  print("Prefijo: ", prefix_expression)
  print("Posfijo: ", postfix_expression)
  print("********************\n")

  # Identificar las incógnitas y pedírselas al usuario
  variables = ask_for_variables(identify_variables(prefix_expression))
  
  # Evaluar la expresión
  result = evaluate_prefix_expression(prefix_expression, variables)

  # Imprimir resultado
  print("\nResultado: {}".format(result))