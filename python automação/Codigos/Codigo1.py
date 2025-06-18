# pip install pyautogui

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever 
#pyautogui.hotkey -> atalhos do teclado (crtl + shift)
    



#passo 1: abrir o sistema da empresa
 #   sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win") #abrir o botao do windows

pyautogui.write("chrome") #escreve na barrinha do windows

pyautogui.press("enter") #aperta enter

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

#pedir pra o computador esperar 3s ( importar o time para esperar os 3s)
time.sleep(1)

#passo 2: logar no sistema
pyautogui.click(x=604, y=378)

pyautogui.write("testedeemail@gmail.com")
pyautogui.press("tab") #passa para os cantos da senha

pyautogui.write("senha123")
pyautogui.press("enter") 
#passo 3: importar a base de dados dos produtos (pandas e openpyxl)


tabela = pandas.read_csv("produtos.csv") #pandas read ler uma base de dados, e colocamos em uma tabela para ele armazenar oq está sendo feito

print(tabela)


time.sleep(2)

#passo 4: cadastrar 1 produto

for linha in tabela.index:

    # SEPARANDO POR CATEGORIA

    #CÓDIGO
    pyautogui.click(x=521, y=256)

    codigo = tabela.loc[linha, "codigo"] #criamos variaveis para cada categoria
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #MARCA
    marca = tabela.loc[linha, "marca"]# comando tabela.loc e linha, é para localizar algo na tabela e linha fala que esta nas linhas e nao nas colunas por exemplo.
    pyautogui.write(str(marca))  
    pyautogui.press("tab")

    #TIPO
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #CATEGORIA
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #PREÇO UNITARIO
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
       
    #CUSTO
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #OBSMouse    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
     pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000)

#passo 5: repetir o passo 4 ate acabar todos os produtos 