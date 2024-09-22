import random

vogais = ["a" , "e", "i", "o", "u" ]
cons = ["b" , "c", "d", "e", "f" "g", "l", "m", "n" "p", "r", "s", "v", "t" ]


def nome_random():
    numero = random.randint(2, 5)
    name=""
    for  x in range(numero):
        vogalr = random.choice(vogais)
        randomc = random.choice(cons)
        name= name+vogalr+randomc+vogalr
        print(name)
    return name


Nome_final = nome_random()
Segundo_nome = nome_random()