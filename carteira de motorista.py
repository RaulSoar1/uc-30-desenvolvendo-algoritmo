# Pergunta ao usuário se ele possui carteira de motorista
resposta = input("Você possui carteira de motorista? (S/N): ")

# Converte a resposta para minúsculo
resposta = resposta.lower()

# Converte para booleano
if resposta == "s":
    possui_carteira = True
else:
    possui_carteira = False

# Imprime o valor booleano e o tipo
print("Valor booleano:", possui_carteira)
print("Tipo:", type(possui_carteira))