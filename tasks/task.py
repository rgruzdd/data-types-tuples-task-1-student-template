from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here
    new_tuples = []
    for i in str(num):
        new_tuples.append(int(i))
    return tuple(new_tuples)

print(get_tuple(87178291199))


