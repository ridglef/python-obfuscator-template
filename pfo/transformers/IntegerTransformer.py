import ast
import random

def transform(astTree: ast):
    class IntegerTransformer(ast.NodeTransformer):
        def visit_Num(self, node):
            if isinstance(node.n, int):
                key = random.randint(0, 99999999)
                enc = key ^ node.n
                node.n = key
                node = ast.BinOp(left=node, op=ast.BitXor(), right=ast.Num(enc))

            return node

    transformer = IntegerTransformer()
    transformed_tree = transformer.visit(astTree)
    return transformed_tree