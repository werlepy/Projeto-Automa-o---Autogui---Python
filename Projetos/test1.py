from unicodedata import name
from check50 import data
import pyautogui, sys, random

pyautogui.FAILSAFE = True

#__________________________________________________________
vogais = ["a" , "e", "i", "o", "u" ]
cons = ["b" , "c", "d", "e", "f" "g", "l", "m", "n" "p", "r", "s", "v", "t" ]


def nome_random():
    numero = random.randint(2, 3)
    name=""
    for  x in range(numero):
        vogalr = random.choice(vogais)
        randomc = random.choice(cons)
        name= name+vogalr+randomc+vogalr
    # print(name)
    return name


Nome_final = nome_random()
Segundo_nome = nome_random()

#print(Nome_final)

regiao = ["48", "51", "11",]
#__________________________________________________________
#Numeros Aleatórios


def cel_random2():
    pais= str(55)
    regiao_random = str(random.choice(regiao))
    numero= str(random.randint(90000000,99999999))
    final = str(pais+regiao_random+numero)

    # print(regiao_random+numero)
    return final

numero1 = str(cel_random2())
numero2 = str(cel_random2())

print(numero1,numero2)

#__________________________________________________________

#date= str("04-01-1999")

city = str(random.randint(1, 40))

#__________________________________________________________

pyautogui.click('postman.png')
#print("botao imagem")
pyautogui.PAUSE = 0.5

for x in range(15):
    pyautogui.doubleClick(2597, 602)     #Email
    pyautogui.write(Nome_final, 0.05)

    pyautogui.doubleClick(2587, 441)     #Nome
    pyautogui.press(['backspace'])
    pyautogui.doubleClick
    pyautogui.press(['del'])
    pyautogui.doubleClick(2587, 441)
    pyautogui.press(['del'])
    pyautogui.write(Nome_final.capitalize(), 0.05)
    pyautogui.press(['space'])
    pyautogui.write(Segundo_nome.capitalize(), 0.05)

    pyautogui.doubleClick(2742, 621)     #Primeiro Cel
    pyautogui.press(['backspace'])
    pyautogui.write(numero1, 0.05)

    pyautogui.doubleClick(2745, 638)     #Segundo Cel
    pyautogui.press(['backspace'])
    pyautogui.write(numero2, 0.05)

    pyautogui.doubleClick(2749, 500)     #Cidade
    pyautogui.press(['backspace'])
    pyautogui.write(city, 0.05)

    pyautogui.click(3702, 266, 1 )     #Send
    print("deu")
    pyautogui.moveTo(2597, 602, 3) 



#print('Press Ctrl-C to quit.')
#try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='')
#        print('\b' * len(positionStr), end='', flush=True)
#except KeyboardInterrupt:
#    print('\n')



print("#########################-------Fim do Teste -------#########################")

