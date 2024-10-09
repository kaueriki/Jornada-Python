# link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas
# pyautogui.write -escrever um texto
# pyautogui.click -clicar com o mouse
# pyautogui.press -apertar uma tecla
# pyautogui.hotkey("ctrl", "c") - apertar duas teclas
pyautogui.PAUSE = 0.5
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# Digitar o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# Fazer login
pyautogui.click(x=427, y=362)
pyautogui.write("kaueriki@gmail.com")
pyautogui.click(x=427, y=463)
pyautogui.write("1234")
pyautogui.click(x=658, y=517)

time.sleep(1) 

tabela = pandas.read_csv("produtos.csv")
print(tabela)




for linha in tabela.index:
    pyautogui.click(x=541, y=251)
    # Codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #Marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #Tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #Categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #PReco
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #OBS
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(2000)

    linha= linha + 1