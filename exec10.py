import math

metrosquad = float(input("Informe a quantidade de metros quadrados para pintura: "))
litros = (metrosquad/6)

#questão A
latas = math.ceil(litros/18)
print("Você utilizará ", latas, "latas de tinta")
preco = latas * 80
print("Valor total: ", preco)

#questão b
galao = math.ceil(litros/3.6)
print("Será necessário: ", galao, "galões")
precogalao = galao * 25
print("Valor total R$: ", precogalao)

#questão c
latas = int(litros/18)
faltou = litros % 18
galao = math.ceil(faltou/3.6)
precogalao = galao * 25
precolata = latas * 80

print("Será necessário: ", latas, "latas")
print("e", galao, "galões")
print("valor total R$: ", precolata + precogalao)


