class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome
        
joao = Pessoa('João')
print(joao)
carlos = Pessoa('Carlos')
print(carlos)
