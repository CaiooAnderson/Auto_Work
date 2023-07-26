# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas as pd
# pyautogui.write
# pyautogui.press
# pyautogui.click
pyautogui.PAUSE = 0.4
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=593, y=400)
pyautogui.write("caiozin@gmail.com")
pyautogui.press("tab")
pyautogui.write("caiozin123")
pyautogui.press("tab" and "enter")

tabela = pd.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:
  
    pyautogui.click(x=604, y=283)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(2000)

