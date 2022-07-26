def dft(self, array):
    stack = stack()
    visited = set()
    stack.append(self)
    while len(stack) > 0 and len(visited) >= 0:
        current = stack.pop()
        array.append(current)
        visited.add(current)
    return array