import random
from unicodedata import name

vogais = ["a" , "e", "i", "o", "u" ]
cons = ["b" , "c", "d", "e", "f" "g", "l", "m", "n" "p", "r", "s", "v", "t" ]
print(vogais)
print(cons)

def nome_random():
    numero = random.randint(3, 7)
    name=""
    print(numero)
    for  x in range(numero):
        vogalr = random.choice(vogais)
        randomc = random.choice(cons)
        name= name+vogalr+randomc
            
       # print(name)
    return name

Nome_final = nome_random()
print(Nome_final)
#def arquivo_nomes():
#    with open('nomes.csv','w') as file:
#        writer = csv.writer(file)
#        name = nome()
#        writer.writerow([name])

#for i in range(60):
#    arquivo_nomes()