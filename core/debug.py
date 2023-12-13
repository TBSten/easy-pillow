from core.node import DrawNode


def print_node_tree(root_node: DrawNode):
    _print_node(root_node, 0)


def _print_node(node: DrawNode, indent: int):
    print(f"{'  '*indent}{node.label} {node.x}{node.y} {node.w}*{node.h}")
    for child in node.children:
        _print_node(child, indent+1)
