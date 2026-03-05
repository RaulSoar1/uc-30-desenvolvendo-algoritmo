#atividade - manipulação de listas em python

numeros = [10, 20, 30, 20, 40, 20, 50]

quantidade = len(numeros)
print("Quantidade de elementos na lista: ", quantidade)

vezes_20 = numeros.count(20)
print("O número 20 aparece ", vezes_20, "vezes na lista")

posicao_30 = numeros.index(30)
print("A posição do número 30 é: ", posicao_30)

existe_100 = 100 in numeros
print("O número 100 está na lista? ", existe_100)