#print("resposta", resp)
#print("resultado", resultado)

resp = input("você vai passar de ano? s/N: ").strip().lower()

#resultado = (resp == "s"):
resultado = resp in ("s", "sim")

print("resultado ", resultado)
print(type(resultado))