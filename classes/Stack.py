from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            return None

    def size(self) -> int:
        return len(self.items)

    def reverse(self) -> None:
        self.items.reverse()

    def __str__(self) -> str:
        result = ""
        for key, item in enumerate(self.items):
            result += item

        return result

    def print(self) -> None:
        result = ""
        for key, item in enumerate(self.items):
            result += item
        print(f'{result}')