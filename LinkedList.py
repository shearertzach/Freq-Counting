from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    print(f'|New Value Added| -> {new_data[0]}')


  def find(self, item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1


  def update_node(self, key):
    current = self.head
    found = False

    print(f'|Attempting Update| -> {key}')

    while current.data[0] != None and not found:
      current_key = current.data[0]
      current_val = current.data[1]
      print(f"|Indexing List| -> {current_key}")
      if current_key == key:
        found = True
        print(f"|Found| -> {key}")
        current.data = (current_key, current_val + 1)
        print(f"|Updated| -> FROM: {current_key}: {current_val} TO {current_key}: {current_val + 1}")
      else:
        current = current.next


  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      pass
    else:
      for _ in range(self.length()):
        print(f'{current.data[0]}: {current.data[1]}')
        current = current.next