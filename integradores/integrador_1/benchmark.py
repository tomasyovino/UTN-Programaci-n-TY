from .BinarySearchTree import BinarySearchTree
from .AVLTree import AVLTree
import time
import random

"""
Benchmark de rendimiento para comparar BST sin balancear y AVL.
Imprime tiempos promedio de inserción y búsqueda para distintos tamaños.
"""

def benchmark(tree_cls, n, trials=3):
    insert_times = []
    search_times = []
    for _ in range(trials):
        data = random.sample(range(n * 10), n)
        tree = tree_cls()
        t0 = time.perf_counter()
        for x in data:
            tree.insert(x)
        insert_times.append(time.perf_counter() - t0)
        t0 = time.perf_counter()
        for x in data:
            tree.search(x)
        search_times.append(time.perf_counter() - t0)
    return sum(insert_times) / trials, sum(search_times) / trials

if __name__ == "__main__":
    print("n,BST_insert_s,BST_search_s,AVL_insert_s,AVL_search_s")
    for n in [1000, 2000, 5000, 10000]:
        bst_ins, bst_srch = benchmark(BinarySearchTree, n)
        avl_ins, avl_srch = benchmark(AVLTree, n)
        print(f"{n},{bst_ins:.6f},{bst_srch:.6f},{avl_ins:.6f},{avl_srch:.6f}")