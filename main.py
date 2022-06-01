source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def assert_to_tree(src):
    out = {}
    for target, value in src:
        if target is None:
            out[value] = {}

        else:
            # Let's find target node
            stack = [out]

            while stack:
                child = stack.pop(0)
                for parent, tree in child.items():
                    if parent == target:  # target node found
                        child[parent][value] = {}
                        break

                    stack.append(tree)

                # Continue if nothing found
                else:
                    continue

                # Break the While loop if target node found
                break

    return out


result = assert_to_tree(source)
print(result)
print(result == expected)
