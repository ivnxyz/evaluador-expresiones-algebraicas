# Clase Nodo para el Stack
class Node:

  # data es el dato a guardar y next es el siguiente nodo
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

# Estructura para el Stack
class Stack:
  head:Node = None

  # 'empuja' un nuevo nodo
  def push(self, data):
    # Crear nodo
    new_node = Node(data)

    # Empujar nodo
    if self.is_empty():
      self.head = new_node
    else:
      # Iterar hasta el último elemento
      temp = self.head

      while temp.next != None:
        temp = temp.next
      
      # Agregar nuevo nodo
      temp.next = new_node
  
  # Elimina el último nodo
  def pop(self) -> Node:
    # Verificar si hay nodos
    if self.is_empty():
      raise Exception("No hay elementos en el Stack")

    # Iterar hasta el penúltimo nodo
    last = self.head
    current = self.head

    while current.next != None:
      last = current
      current = current.next

    # Eliminar último nodo
    if last.next == None:
      self.head = None
    else:
      last.next = None

    return current
  
  # Obtiene el último nodo sin eliminarlo
  def last(self) -> Node:
    last_node = self.head

    while last_node.next != None:
      last_node = last_node.next
    
    return last_node
  
  # Verifica si el stack está vacío
  def is_empty(self) -> bool:
    return self.head == None
  
  # Sobreescribe la función str para imprimir un stack
  def __str__(self):
    node = self.head
    string_representation = ''

    while node != None:
      string_representation = '[ {} ]\n'.format(node.data) + string_representation
      node = node.next
    
    return string_representation
