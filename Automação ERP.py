import pyautogui
import pyperclip
import subprocess
import time
import pandas as pd


pyautogui.FAILSAFE = True #isto permite que caso que vc queira interromper o pyautogui, basta colocar o mouse em qualquer uma das 4 extremidades da tela

def localizar_imagem(imagem):
    while not pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9): #esses parâmetros permitem que o reconhecimento de imagem seja mais tolerante a imagens um pouco diferentes
        time.sleep(1)
    encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
    return encontrou

def direita(posicoes_imagem):
    return posicoes_imagem[0] + posicoes_imagem[2], posicoes_imagem[1] + posicoes_imagem[3]/2

def escrever_texto(texto): #resolvendo escrita de acentos e caracteres especiais do pyautogui
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')

#Abrir o ERP (Fakturama)
subprocess.Popen([r'C:\Program Files\Fakturama2\Fakturama.exe']) #abrindo um executável
encontrou = localizar_imagem(r'ERP_Images\fakturama_logo.png')


#Importando a base de dados de produtos
df_produtos = pd.read_excel('Produtos.xlsx')

for linha in df_produtos.index: #para cada número da linha da tabela
    nome = df_produtos.loc[linha, 'Nome']
    id = df_produtos.loc[linha, 'ID']
    categoria = df_produtos.loc[linha, 'Categoria']
    gtin = df_produtos.loc[linha, 'GTIN']
    supplier = df_produtos.loc[linha, 'Supplier']
    descricao = df_produtos.loc[linha, 'Descrição']
    imagem = df_produtos.loc[linha, 'Imagem']
    preco = df_produtos.loc[linha, 'Preço']
    custo = df_produtos.loc[linha, 'Custo']
    estoque = df_produtos.loc[linha, 'Estoque']

    #Clicar no menu New
    encontrou = localizar_imagem(r'ERP_Images\menu_new.png')
    pyautogui.click(pyautogui.center(encontrou)) #clica no centro a imagem encontrada

    #Clicar em New Product
    encontrou = localizar_imagem(r'ERP_Images\new_product.png')
    pyautogui.click(pyautogui.center(encontrou))

    #Preencher todos os campos
    encontrou = localizar_imagem(r'ERP_Images\item_number.png')
    pyautogui.click(direita(encontrou))
    escrever_texto(str(id))

    pyautogui.press('tab') #1 tecla só, hotkey é para combinação de teclas
    escrever_texto(str(nome))

    encontrou = localizar_imagem(r'ERP_Images\category.png')
    pyautogui.click(direita(encontrou))
    escrever_texto(str(categoria))

    encontrou = localizar_imagem(r'ERP_Images\GTIN.png')
    pyautogui.click(direita(encontrou))
    escrever_texto(str(gtin))

    encontrou = localizar_imagem(r'ERP_Images\supplier_code.png')
    pyautogui.click(direita(encontrou))
    escrever_texto(str(supplier))

    encontrou = localizar_imagem(r'ERP_Images\description.png')
    pyautogui.click(direita(encontrou))
    escrever_texto(str(descricao))

    encontrou = localizar_imagem(r'ERP_Images\price.png')
    pyautogui.click(direita(encontrou))
    preco_texto = f'{preco:.2f}'.replace('.',',') #formatando para duas casas decimais e depois trocando ponto por vírgula
    escrever_texto(str(preco_texto))

    encontrou = localizar_imagem(r'ERP_Images\cost.png')
    pyautogui.click(direita(encontrou))
    custo_texto = f'{custo:.2f}'.replace('.', ',')
    escrever_texto(str(custo_texto))

    encontrou = localizar_imagem(r'ERP_Images\stock.png')
    pyautogui.click(direita(encontrou))
    estoque_texto = f'{estoque:.2f}'.replace('.', ',')
    escrever_texto(str(estoque_texto))

    #Selecionar a imagem
    encontrou = localizar_imagem(r'ERP_Images\select_picture.png')
    pyautogui.click(pyautogui.center(encontrou))

    encontrou = localizar_imagem(r'ERP_Images\nome_arquivo.png')
    escrever_texto(rf'C:\Users\Hugo\Downloads\Imagens Produtos\{str(imagem)}')
    pyautogui.press('enter')

    #Clicar em salvar
    encontrou = localizar_imagem(r'ERP_Images\save.png')
    pyautogui.click(pyautogui.center(encontrou))