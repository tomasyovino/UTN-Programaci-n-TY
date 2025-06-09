# Proyecto Integrador: Árboles Avanzados

## Descripción del proyecto
Este proyecto implementa y compara dos estructuras de datos jerárquicas avanzadas:
- **Binary Search Tree (BST)**: árbol binario de búsqueda sin balanceo.
- **AVL Tree**: árbol de búsqueda auto-balanceado que mantiene altura O(log n) en cada operación.

El objetivo es estudiar las implementaciones, demostrar sus recorridos básicos y evaluar empíricamente su rendimiento en inserción y búsqueda.

## Estructura de carpetas
```
integrador_1/
├── __init__.py
├── Node.py
├── BinarySearchTree.py
├── AVLTree.py
├── benchmark.py
└── index.py
```

## Instrucciones de uso

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tomasyovino/UTN-Programaci-n-TY.git
   cd integradores
   ```

2. **Ejecutar demo de recorridos**  
   ```bash
   python -m integrador_1.index
   ```
   Esto mostrará los recorridos inorden, preorden y postorden del BST y del AVL, además de operaciones de búsqueda y eliminación.

3. **Ejecutar benchmark de rendimiento**  
   ```bash
   python -m integrador_1.benchmark
   ```
   Generará una tabla CSV con los tiempos promedio de inserción y búsqueda para distintos valores de `n`.

## Reflexiones del equipo

- **Aprendizajes técnicos**:  
  - Comprendimos en profundidad cómo la complejidad de las operaciones cambia al introducir balanceo en árboles.  
  - Implementar rotaciones en AVL reforzó conceptos de recursión y diseño de algoritmos.

- **Retos encontrados**:  
  - Manejo de casos de duplicados en BST y AVL.  
  - Asegurar que las rotaciones preservaran correctamente la estructura y propiedades del árbol.

- **Extensiones futuras**:  
  - Implementar eliminación en AVL para completar la comparación.  
  - Explorar otras estructuras balanceadas (Red-Black, B-tree).  
  - Añadir visualizaciones gráficas de los árboles y sus rotaciones.
