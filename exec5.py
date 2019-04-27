merc = float(input("Qual o valor da mercadoria?: "))
desc = float(input("Qual o valor de desconto?: "))

totaldes = merc * desc/100

print("Seu desconto será de R$: ", totaldes)
print("valor final da compra R$: ", merc - totaldes)
