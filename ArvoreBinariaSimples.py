pip install anytree

# O método RenderTree é para ajudar a mostrar a saída
from anytree import Node, RenderTree

#estabelecendo o nó
root = Node(10)

#Estabelecendo o que vier depois do nó
# 2 parametros - valor do nó e os outros qual será o nó anterior
level1 = Node(34, parent=root)
level2 = Node(89, parent=root)
level3 = Node(45, parent=level1)
level3 = Node(50, parent=level2)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
