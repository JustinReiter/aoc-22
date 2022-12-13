
from functools import reduce
from typing import List


class Item:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
    
    def get_size(self) -> int:
        return self.size
    
    def get_below_threshold(self, N) -> List['Dir']:
        return []

    def get_best_delete_dir(self, space_to_remove: int) -> 'Dir':
        return None


class File(Item):
    def __init__(self, name, size):
        super().__init__(name, size)


class Dir(Item):
    def __init__(self, name, parent):
        super().__init__(name)
        self.children = []
        self.parent = parent
    
    def get_size(self):
        self.size = reduce(lambda x, e: x + e.get_size(), self.children, 0)
        return self.size
    
    def get_below_threshold(self, N):
        return ([self] if self.size <= N else []) + list(
            reduce(lambda x, e: x + e.get_below_threshold(N), self.children, [])
        )
    
    def contains_name(self, name):
        return any(filter(lambda e: e.name == name, self.children))
    
    def get_best_delete_dir(self, space_to_remove) -> 'Dir':
        best_child = reduce(
            lambda best, x: best if best and best.size < x.get_best_delete_dir(space_to_remove).size else x.get_best_delete_dir(space_to_remove),
            filter(
                lambda e: e.get_best_delete_dir(space_to_remove) and e.get_best_delete_dir(space_to_remove).size >= space_to_remove,
                self.children
            ),
            None
        )

        if best_child:
            # if best_child exists, return this as it must be smaller
            return best_child
        elif space_to_remove > self.size:
            # if size not large enough, ignore
            return None
        # return self otherwise
        return self


def read_input():
    return list(map(lambda e: e.strip(), open('p7.txt', 'r').readlines()))

P1_THRESHOLD = 100_000

def p1():
    lines = read_input()

    is_ls = False
    active_dir = None
    for line in lines:
        if is_ls and not line.startswith('$'):
            # add new dir/file to dir
            if line.startswith('dir'):
                # create new directory
                if not active_dir.contains_name(line[4:]):
                    # new dir
                    active_dir.children.append(Dir(line[4:], active_dir))
            else:
                # create new file
                if not active_dir.contains_name(' '.join(line.split(' ')[1:])):
                    # new file
                    active_dir.children.append(File(' '.join(line.split(' ')[1:]), int(line.split(' ')[0])))
        else:
            # parse command
            if line.startswith('$ cd'):
                # cd new folder
                if not active_dir:
                    # root likely
                    active_dir = Dir(line[5:], None)
                    root = active_dir
                else:
                    # new dir from active_dir
                    if line[5:] == '..':
                        # parent dir
                        active_dir = active_dir.parent
                    else:
                        active_dir = next(filter(lambda e: e.name == line[5:], active_dir.children))
                is_ls = False
            else:
                is_ls = True

    root.get_size()
    element_above_threshold = root.get_below_threshold(P1_THRESHOLD)
    return reduce(lambda s, e: s + e.size, element_above_threshold if element_above_threshold else [], 0), root

TOTAL_SPACE = 70_000_000
SPACE_NEEDED = 30_000_000

def p2(root: Dir):
    space_to_remove = abs(TOTAL_SPACE - SPACE_NEEDED - root.size)
    # we have the current size of all directories
    print('{} {} {} {}'.format(TOTAL_SPACE, space_to_remove, root.size, SPACE_NEEDED))
    return root.get_best_delete_dir(space_to_remove)
    
    

    
p1_ans = p1()
print(p1_ans[0])
p2_ans = p2(p1_ans[1])
print('{} {}'.format(p2_ans.name, p2_ans.size))


