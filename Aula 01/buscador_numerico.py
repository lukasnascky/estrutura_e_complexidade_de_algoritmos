arquivo = "Aula 01/numeros.txt"

valor_a_econtrar = 34

with open(arquivo, 'r') as c:
    conteudo = c.read()
    lista_numeros = [int(valor) for valor in conteudo.split()]

encontrado = False

for numero in lista_numeros:
    if numero == valor_a_econtrar:
        encontrado = True
        break