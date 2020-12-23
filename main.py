'''
  Archivo principal para el menú e interactuar con los otros paquetes
'''

# Imprime el menú y le pide información al usuario
def print_menu():
  print('''
    ¿Qué quieres hacer?

    (1) Evaluar una expresión algebráica
    (2) Traducir expresión a prefijo
    (3) Traducir expresión a posfijo
    (4) Salir
  ''')

  return int(input())

# Pide una expresión algebráica
def ask_for_algebraic_expression():
  return input('Ingresa la expresión algebráica: ')

# Punto de entrada al programa
if __name__ == "__main__":
  while True:
    # Pedir una elección al usuario
    choice = print_menu()

    if choice == 1:
      ask_for_algebraic_expression()
    elif choice == 2:
      ask_for_algebraic_expression()
    elif choice == 3:
      ask_for_algebraic_expression()
    elif choice == 4:
      print('Bye... :)')
      break
    else:
      print('No reconozco esa elección :(')
