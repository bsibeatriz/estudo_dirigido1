sal = float(input("Qual o valor so salário?? "))
porc = float(input("qual a porcentagem de correção salarial?: "))

total1 = sal * porc/100
print(" Seu aumento foi de R$: ", total1)
print("seu novo salário será R$: ", sal + total1)
