import random

regiao = ["48", "51", "11",]

def cel_random2():
    pais= str(55)
    regiao_random = str(random.choice(regiao))
    numero= str(random.randint(10000000,99999999))
    final = str((pais+regiao_random+numero))

    # print(regiao_random+numero)
    return final

numero1 = str(cel_random2())
numero2 = str(cel_random2())

print(numero1,numero2)