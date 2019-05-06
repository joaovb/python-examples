# Como mesclar dois dicionários
# no Python 3.5+

x = { 'a' : 1 , 'b' : 2 }
y = { 'b' : 3 , 'c' : 4 }

z = { ** x, ** y}

print(z)

# Em Python 2.x que poderia
# usar este:
#>>> z =  Dict (x, ** y)
#>>> z
#{ 'a': 1, 'c': 4 'b': 3}

# Nesses exemplos, o Python mescla as chaves de dicionário
# na ordem listada na expressão, sobrescrevendo
# duplicatas da esquerda para a direita.
#
# Veja: https://www.youtube.com/watch? v = Duexw08KaC8
