#!/usr/bin/python3
"""
Returns a list of lists of ints representing the Pascal's triangle of size n
"""


def pascal_triangle(n: int):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows to generate.

    Returns:
    list: A list of lists representing Pascal's triangle up to the nth row.
    """

    if n <= 0:
        return []

    _list = []
    for i in range(n):
        row = [1]
        if _list:
            last_row = _list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        _list.append(row)
    return (_list)


if __name__ == "__main__":
    """Sample teest"""
    def print_triangle(triangle):
        """Prints a triangle"""
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
