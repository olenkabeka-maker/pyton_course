"""Розширити структуру, яку побудували на уроці, можливість вставки дерева в наявне дерево та видалення піддерева з дерева, що існує"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node, value):                        # вставлення одного значення
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node


def delete_node(node, value):                   # видалення одного вузла
    if node is None:
        return None

    if value < node.value:
        node.left = delete_node(node.left, value)
    elif value > node.value:
        node.right = delete_node(node.right, value)
    else:
        
        if node.left is None:                   # 0 або 1 дитина
            return node.right
        elif node.right is None:
            return node.left
                                            
        temp = node.right                       # 2 діти → беремо мінімальний справа
        while temp.left:
            temp = temp.left

        node.value = temp.value
        node.right = delete_node(node.right, temp.value)

    return node


                    
def insert_subtree(root, subtree):              # ВСТАВЛЯЄ ЦІЛЕ ПІДДЕРЕВО
    
    """Вставляє корінь subtree у root як звичайний елемент, але зберігає ВСЕ піддерево"""
    
    if subtree is None:
        return root

    
    root = insert(root, subtree.value)          # вставляю root піддерева як значення
    
    if subtree.left:                            # залишаю всіх дітей піддерева
        root = insert_subtree(root, subtree.left)

    if subtree.right:
        root = insert_subtree(root, subtree.right)

    return root



def delete_subtree(root, value):                # ВИДАЛЯЮ ВСЕ ПІДДЕРЕВО
    """ Видаляє вузол 'value' разом із усім його піддеревом. Шукає вузол і відсікає гілки"""

    if root is None:
        return None

    if value < root.value:
        root.left = delete_subtree(root.left, value)

    elif value > root.value:
        root.right = delete_subtree(root.right, value)

    else:                                       # знайдено вузол — видаляємо ВСЕ піддерево
        return None                             # прибирає його повністю

    return root

def inorder(node):                              # дДопоміжний in-order для перевірки
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

root = Node(10)
insert(root, 5)
insert(root, 15)

sub = Node(7)
insert(sub, 6)
insert(sub, 8)

root = insert_subtree(root, sub)
root = delete_subtree(root, 5)

def print_tree(node, indent="", last=True):
    """Друкує дерево боком (праворуч вгорі → ліворуч внизу)"""

    if node is not None:
        print(indent, "└── " if last else "├── ", node.value, sep="")
        indent += "    " if last else "│   "
        print_tree(node.right, indent, False)
        print_tree(node.left, indent, True)

print_tree(root)