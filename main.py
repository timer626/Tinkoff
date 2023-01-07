import ast
import re
import astunparse
class Visitor(ast.NodeVisitor):
    def visit (self,node:ast.AST):
        print(node)
        self.generic_visit(node)
f1=open('compare.py')
f2=open('2.py')
a=f1.read()
b=f2.read()
tree1=ast.parse(a)
tree2=ast.parse(b)
str=ast.dump(tree1)
print(tree1._fields)
print(tree1.body[1]._fields)
print(str)
Visitor().visit(tree1)


