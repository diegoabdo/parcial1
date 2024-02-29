class Nodo:
    def __init__(self, dato):
        # instanciar
        self.dato = dato
        self.nodo_siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cola = None
        self.tamannio = 0

    def evaluar_polinomio(self, evaluar):
        actual = self.head
        polinomio_result = ListaEnlazada()
        contador = 1
        while actual:
            result = pow(actual.dato, evaluar)
            polinomio_result.insertar_at_beginning(result)
            actual = actual.nodo_siguiente
            contador += 1
        return polinomio_result

    def sumar(self, polinomio1, polinomio2):
        actual1 = polinomio1.head
        actual2 = polinomio2.head
        polinomio_result = ListaEnlazada()
        while actual1 is not None and actual2 is not None:
            result = actual1.dato + actual2.dato
            polinomio_result.insertar_final(result)
            actual1 = actual1.nodo_siguiente
            actual2 = actual2.nodo_siguiente

        return polinomio_result

    def restar(self, polinomio1, polinomio2):
        actual1 = polinomio1.head
        actual2 = polinomio2.head
        polinomio_result = ListaEnlazada()
        while actual1 is not None and actual2 is not None:
            result = actual1.dato - actual2.dato
            polinomio_result.insertar_final(result)
            actual1 = actual1.nodo_siguiente
            actual2 = actual2.nodo_siguiente

        return polinomio_result


    def search_data_retposition(self, user_data):
        current = self.head
        old = self.head
        counter = 0
        while current is not None:
            if current.dato == user_data:
                return counter
            current = current.nodo_siguiente
            counter += 1

    # Metodo insertar al inicio
    def insertar_inicio(self, dato):
        new_nodo = Nodo(dato)
        # si
        if (self.head is None):
            self.head = new_nodo
            return
        new_nodo.nodo_siguiente = self.head
        self.head = new_nodo


    # Metodo insertar al final
    def insertar_final(self, dato):
        new_nodo = Nodo(dato)
        if (self.head == None):
            self.head = new_nodo
            return
        actual = self.head
        while (actual.nodo_siguiente):
            actual = actual.nodo_siguiente

        actual.nodo_siguiente = new_nodo
    def insertar_at_beginning(self,element) :
        if self.head is None:
            new_node = Nodo(element)

            self.head = new_node
        else:
            new_node = Nodo(element)
            new_node.nodo_siguiente = self.head
            self.head = new_node


    def imprimir_lista(self):
        actual = self.head
        contador = 1
        while actual:
            print(f"({actual.dato}x-{contador})", end=" + ")
            actual = actual.nodo_siguiente
            contador += 1

    def insert_at_end(self, element):
        if self.head is None:
            new_node = Nodo(element)
            self.head = new_node
        else:
            current = self.head
            while current.nodo_siguiente is not None:
                current = current.nodo_siguiente
            new_node = Nodo(element)
            current.nodo_siguiente = new_node

    def insert_at_position(self, element, position):
        counter = 1
        current = self.head
        while counter < position - 1 and current is not None:
            counter += 1
            current = current.nodo_siguiente
        if position == 1:
            new_node = Nodo(element)
            new_node.nodo_siguiente = current
            self.head = new_node
        else:
            new_node = Nodo(element)
            new_node.nodo_siguiente = current.nodo_siguiente
            current.nodo_siguiente = new_node
    def delete_from_beginning(self):
        if self.head is None:
            print("La lista está vacía, no se puede eliminar nada")
        else:
            node = self.head
            self.head = self.head.nodo_siguiente
            del node

    def delete_from_last(self):
        if self.head is None:
            print("La lista está vacía, no hay elementos para eliminar")
        else:
            current = self.head
            previous = None
            while current.nodo_siguiente is not None:
                previous = current
                current = current.nodo_siguiente
            previous.nodo_siguiente = None
            del current
    def delete_at_position(self, position):
        if self.head is None:
            print("La lista está vacia, no hay elementos para eliminar")
        else:
            current = self.head
            previous = None
            count = 1
            while current.nodo_siguiente is not None and count < position:
                previous = current
                current = current.nodo_siguiente
                count += 1
            if current == self.head:
                self.head = current.nodo_siguiente
                del current
            else:
                previous.nodo_siguiente = current.nodo_siguiente
                del current
    def count_elements(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.nodo_siguiente
        print("Numero de elementos en la lsita: ", count)
    def replace_element(self, old_element, new_element):
        current = self.head
        while current is not None:
            if current.dato == old_element:
                current.dato = new_element
                break
            current = current.nodo_siguiente

    def updateAtPosition(self, new_element, position):
        if self.head is None and position != 1:
            print("No element to update in the linked list.")
            return
        elif self.head is None and position == 1:
            newNode = Nodo(new_element)
            self.head = newNode
            return
        count = 1
        current = self.head
        while current.nodo_siguiente is not None and count < position:
            count += 1
            current = current.nodo_siguiente
        if count == position:
            current.dato = new_element
        elif current.next is None:
            print("Not enough elements in the linked list.")



