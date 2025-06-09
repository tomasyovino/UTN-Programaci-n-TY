from .BinarySearchTree import BinarySearchTree
from .AVLTree import AVLTree

def esperar(mensaje):
    input(mensaje)

if __name__ == "__main__":
    values = [50, 30, 70, 20, 40, 60, 80]
    bst = BinarySearchTree()
    avl = AVLTree()

    print("=== Demo interactivo: BST y AVL ===")
    esperar("\nPaso 1: Crear e insertar valores. Presiona Enter para continuar...")
    for x in values:
        bst.insert(x)
        avl.insert(x)
    print("Valores insertados en BST:", values)
    print("Valores insertados en AVL:", values)

    esperar("Paso 2: Mostrar recorrido inorden. Presiona Enter...")
    print("BST Inorden (de menor a mayor):", bst.inorder())
    print("AVL Inorden (de menor a mayor):", avl.inorder())

    esperar("Paso 3: Mostrar recorrido preorden del BST. Presiona Enter...")
    print("BST Preorden:", bst.preorder())

    esperar("Paso 4: Mostrar recorrido postorden del BST. Presiona Enter...")
    print("BST Postorden:", bst.postorder())

    esperar("Paso 5: Buscar valor 60. Presiona Enter...")
    print("¿Existe el 60 en BST?", bst.search(60))
    print("¿Existe el 60 en AVL?", avl.search(60))

    esperar("Paso 6: Eliminar valor 30 en BST. Presiona Enter...")
    bst.delete(30)
    print("BST tras eliminar 30 (Inorden):", bst.inorder())

    print("\nDemo completado. ¡Gracias por seguir los pasos!")
