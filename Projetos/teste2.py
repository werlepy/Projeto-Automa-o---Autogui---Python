from unicodedata import name
from check50 import data
import pyautogui, random

pyautogui.FAILSAFE = True

#__________________________________________________________
vogais = ["a" , "e", "i", "o", "u" ]
cons = ["b" , "c", "d", "e", "f" "g", "l", "m", "n" "p", "r", "s", "v", "t" ]
regiao = ["48", "51", "11",]


#__________________________________________________________

#date= str("04-01-1999")


#__________________________________________________________

pyautogui.click(1953,515)
#print("botao imagem")
pyautogui.PAUSE = 0.8

for x in range(50):
    city = str(random.randint(5, 25))

    nomes = ["Jose", "Gabriel","Ana", "Gabriela","Maria", "Antonieta","Geralda", "Godofredo","Joao", "Anderson","Silva", "Goliaz","Geraldo", "Ricardo","Guilherme", "Gabriel","Muller", "Silva","Zimmer", "Josoe","Pinto", "Getulho","Vargas", "Maluff","Eistain", "Gosh","Silveira", "Antunes","DaSilva", "Sauro","Josef", "Pereira"]
    last_name = ["Muller", "Silva","Zimmer", "Josoe","Pinto", "Getulho","Vargas", "Maluff","Eistain", "Gosh","Silveira", "Antunes","DaSilva", "Sauro","Josef", "Pereira","Jose", "Gabriel","Ana", "Gabriela","Maria", "Antonieta","Geralda", "Godofredo"]

    def nome_random():
        numero = random.randint(2, 3)
        name=""
        for  x in range(numero):
            vogalr = random.choice(vogais)
            randomc = random.choice(cons)
            name= name+vogalr+randomc+vogalr
        # print(name)
        return name

    #Nome_final = nome_random()
    #Segundo_nome = nome_random()
    Nome_final = random.choice(nomes)
    Segundo_nome = random.choice(last_name)

    email = str(Nome_final+Segundo_nome)

    def cel_random2():
        pais= str(15)
        regiao_random = str(random.choice(regiao))
        numero= str(random.randint(90000000,99999999))
        final = str(pais+regiao_random+numero)

        return final

    numero1 = str(cel_random2())
    numero2 = str(cel_random2())
    print(numero1,numero2)

    pyautogui.doubleClick( 2634, 602)     #Email
    pyautogui.write(email, 0.05)
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

