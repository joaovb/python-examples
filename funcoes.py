def get_soma(a, b):
    return a + b

def get_multiplicacao(a, b):
    return a * b

#(32 °F − 32) × 5/9 = 0 °C
def get_fah(temp):
    return (temp - 32) * (5/9)

print(get_soma(78, 90))
print(get_multiplicacao(23, 7))
print(get_fah(40))
