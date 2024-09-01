from typing import List

stack: List[str] = []

stack.append('livro A')
stack.append('livro B')
stack.append('livro C')


top_item = stack.pop() # C

print(stack, top_item)