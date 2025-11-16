"""Дерево з деталізованими порівняннями та print-ами"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)
root.left.left.left = Node(1)

def search(node, value):
    if node is None:
        return None
    
    print(f"Порівнюю: шукаю {value}, зараз вузол {node.value}")     # показує порівняння

    if node.value == value:
        print(f"Збіг! Знайдено вузол {node.value}")                 # якщо знайдено
        return node

    print(f"→ Йду вліво від {node.value}")                          # рух вліво
    left_result = search(node.left, value)
    if left_result:
        return left_result

    print(f"→ Йду вправо від {node.value}")                         # рух вправо
    right_result = search(node.right, value)
    return right_result

result = search(root, 7)

if result:
    print("Знайдено:", result.value)
else:
    print("Не знайдено")


def bst_search(node, value):                                        # BST-пошук з порівняннями
    if node is None:
        print("Дійшла до порожнього вузла — значення немає")
        return None

    print(f"Порівнюю {value} з вузлом {node.value}")

    if value == node.value:
        print(f"Знайдено! Вузол {node.value}")
        return node

    if value < node.value:
        print(f"{value} < {node.value} → йду вліво")
        return bst_search(node.left, value)
    else:
        print(f"{value} > {node.value} → йду вправо")
        return bst_search(node.right, value)


result = bst_search(root, 113)

if result:
    print("Знайдено:", result.value)
else:
    print("Не знайдено")

                                                    
def delete_node(node, value):                                       # видалення вузла в BST
    if node is None:
        return None

    if value < node.value:
        node.left = delete_node(node.left, value)
    elif value > node.value:
        node.right = delete_node(node.right, value)
    else:
        print(f"Знайдено вузол {value} — видаляємо")

        
        if node.left is None:                                       # випадок 1: 0 або 1 дитина
            return node.right
        elif node.right is None:
            return node.left
                    
        temp = node.right                                           # випадок 2: два нащадки
        while temp.left is not None:
            temp = temp.left

        print(f"Мінімальний у правому піддереві: {temp.value}")
        node.value = temp.value
        node.right = delete_node(node.right, temp.value)

    return node


print("\nВидаляємо значення 3...\n")                                # перевірка після видалення
root = delete_node(root, 3)

def inorder(n):                                                     # In-order (виведе дерево по порядку)
    if n:
        inorder(n.left)
        print(n.value, end=" ")
        inorder(n.right)

print("\nДерево після видалення 3:")
inorder(root)
print()

print("\nВидаляємо кінцевий вузол 18...\n")                         # видаляю кінцевий вузол
root = delete_node(root, 18)

print("\nДерево після видалення 18:")
inorder(root)
print()