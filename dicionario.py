#sem dicionario
matricula1 = 2026001












contato = {
    "@camila": "camila",
    "@paola": "paola",
    "@sheron": "sheron",
    "@bruna": "bruna"
}

print(contato)
print(type(contato))

#Acesso direto ao dicionario
print(contato["@camila"])

#acesso seguro com get()
print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

print("original:", contato) #acessando a lista original

#Add novo elemento
contato["@giovanna"] = "Giovanna"
print("Após add: ", contato)

#atualiza elemento existente
contato["@paola"] = "paola oliveira"
print("Após add: ", contato)

contato.update({
        "@bruna": "Bruna Marquezine",
        "@camila": "camila Q"
})

print("Após atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@sheron")
print(f"removido: {removido}")
print("Após o del: ", contato)

# del remove sem retornar
del contato["@paola"]
print("Após o del: ", contato)


#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("cópia: ", copia)

print("número de contato: ", len(contato))

contato.pop("@camila")
print("Após remover um: ", len(contato))

#verificar existência
if "@joao" in contato:
    print(f"encontrado: {contato['@joao']}")

    if "@inexistente" in contato:
        print("existe")
else:
    print("não existe.")




#dicionário vazio
vazio = {}

#dicionario com tipos mistos
dados = {
    "nome": "joão",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
    }

print

("vazio: ", vazio)
print("vazio: ", dados)