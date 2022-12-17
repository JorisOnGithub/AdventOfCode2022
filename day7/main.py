from typing import List, Optional, Dict, Callable

class DiskItem:
    def __init__(self, name: str, size: Optional[int], parent: Optional["DiskItem"]):
        self._name: str = name
        self._size = size
        self._parent: Optional["DiskItem"] = parent
        self._children: Dict[str, "DiskItem"] = dict()

    def is_directory(self):
        return self._size is None
    
    def get_child(self, name: str) -> Optional["DiskItem"]:
        return self._children.get(name, None)

    def add_child(self, child: "DiskItem"):
        print(f'adding {child._name} to {repr(self)}')
        self._children[child._name] = child

    def get_size(self):
        if self._size is not None:
            return self._size
        return sum((child.get_size() for child in self._children.values()))

    def __repr__(self):
        if not self.is_directory():
            return f'File({self._name}, {self._size})'
        return f'Dir({self._name})'


ROOT = DiskItem('/', None, None)

def print_tree(node: DiskItem, spaces=0):
    print(f'{" " * spaces}{node}')
    if node.is_directory():
        for child in node._children.values():
            print_tree(child, spaces + 2)


def directories_with_predicate(directory: DiskItem, predicate: Callable[[DiskItem], bool]):
    for child in directory._children.values():
        if not child.is_directory():
            continue
        for sub_directory in directories_with_predicate(child, predicate):
            yield sub_directory
    
    if predicate(directory):
        yield directory


def run(lines: List[str]):
    current_directory = ROOT
    for line in lines:
        if line == '$ cd /':
            current_directory = ROOT
        elif line == '$ cd ..':
            current_directory = current_directory._parent
        elif line.startswith('$ cd'):
            name = line.removeprefix('$ cd ')
            current_directory = current_directory.get_child(name)
        elif line.startswith('$ ls'):
            pass
        else:
            size_or_type, name = line.split()
            if size_or_type == 'dir':
                found_item = DiskItem(name, None, current_directory)
            else:
                found_item = DiskItem(name, int(size_or_type), current_directory)
            current_directory.add_child(found_item)

    # part 1
    part1 = sum(dir.get_size() for dir in directories_with_predicate(ROOT, lambda dir: dir.get_size() <= 100_000))
    print(f'part1: {part1}')

    # part 2
    size_available = 70000000 - ROOT.get_size()
    cleanup_needed = 30000000 - size_available

    part2 = min(dir.get_size() for dir in directories_with_predicate(ROOT, lambda dir: dir.get_size() >= cleanup_needed))
    print(f'part2: {part2}')


if __name__ == '__main__':
    with open('in', 'r') as in_file:
        lines = in_file.read().splitlines()
        run(lines)
