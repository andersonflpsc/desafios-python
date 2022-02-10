nome = str(input())
sal = float(input())
vendas = float(input())
comiss = vendas * (15/100)
total = sal + comiss
print("TOTAL = R$ {:.2f}".format(total))


