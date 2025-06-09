class NodeBST:
    """Nodo de un Árbol Binario de Búsqueda (BST)."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class NodeAVL:
    """Nodo de un Árbol AVL con atributo de altura."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1