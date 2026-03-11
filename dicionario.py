contato = {
    "@camila": "camila",
    "@paola": "paola",
    "@sheron": "sheron",
    "@bruna": "bruna",
    "@joao": "joão"
}

#obter chaves
print("chaves: ")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n valores:")
for nome in contato.values():
    print(nome)

#obter pares (chave-valor)
print("\n pares: ") 
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")

    contato = {
    "@camila": 1.66,
    "@paola": 1.50,
    "@sheron": 1.80,
    "@bruna": 1.60,
    "@joao": 1.70
}
# ordenar por chave
print("ordenar por chave: ")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m")

#Ordenar por valor
from operator  import itemgetter
print("\n Ordenando por valor (altura): ")
for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
        print(f"{insta} --> {estatura:.2f}m")