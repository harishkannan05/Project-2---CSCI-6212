import heapq
import random
from time import time, sleep

class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(symbol_freq):
    # Create leaf nodes for each symbol and add them to a min-heap
    heap = [Node(symbol, freq) for symbol, freq in symbol_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Remove two nodes with the lowest frequencies from the heap
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)

        # Create a new internal node with the sum of frequencies
        new_node = Node(None, left_node.frequency + right_node.frequency)
        new_node.left = left_node
        new_node.right = right_node

        # Add the new internal node back to the heap
        heapq.heappush(heap, new_node)

    # The remaining node in the heap is the root of the Huffman tree
    return heap[0]

def build_huffman_codes(node, prefix="", code={}):
    if node is not None:
        if node.symbol is not None:
            code[node.symbol] = prefix
        build_huffman_codes(node.left, prefix + "0", code)
        build_huffman_codes(node.right, prefix + "1", code)
    return code

def huffman_coding(symbol_freq):
    root = build_huffman_tree(symbol_freq)
    codes = build_huffman_codes(root)
    return codes

# Example usage:
n = 10
while (n<=1000000):
    start_time = time()
    sleep(1)    #Added 1s to avoid getting 0.0s for small 'n' values
    symbols = [chr(i) for i in range(n)]  
    symbol_freq = {symbol: random.randint(1, 1000) for symbol in symbols}
    huffman_codes = huffman_coding(symbol_freq)

    print((time() - start_time)*10**9)
    n = n*10