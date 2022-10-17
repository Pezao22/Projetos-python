#--------------------------------------------------------------------------------------------------------------
# É muito importante para o bom funcionamento que os arquivos excel estejam na mesma pasta que o script python
# para nao temos erros ou bugs
#--------------------------------------------------------------------------------------------------------------
import openpyxl
import pyautogui
#-----------------------------------------[ CONFIGURAÇOES ]----------------------------------------------------

planilha_inclusao = 'adere.xlsx'  # planilha que deseja modificar
planilha_inclusao_pg = 'pg'       # nome da pagina dentro da planilha

nova_planilha = 'adere_new.xlsx'  # Nova planilha que sera salva já com as alteraçes
#--------------------------------------------------------------------------------------------------------------
pyautogui.alert('Click em OK e vá tomar um Café !!!')

# carregando aquivo
planilha = openpyxl.load_workbook(planilha_inclusao) # Planilha de inclusao de dados

# selecionando a pagina
pagina = planilha[planilha_inclusao_pg] # pagina da planilha de inclusao
sla = False
# Imprimindo os dados de cada linha
for linha in pagina.iter_rows(min_row=2):
    if linha[2].value != 'None':
        nota = str(linha[0].value)
        # pesquisar ctrc
        pyautogui.doubleClick(275,129, duration=0.5)
        pyautogui.write('CPN')
        pyautogui.doubleClick(333,131, duration=0.5)
        pyautogui.press('del')
        pyautogui.write(nota)
        pyautogui.press('enter')
        # clicar em ocorrencias
        pyautogui.click(53,772, duration=1)
        # selecionar e copiar o trecho
        pyautogui.moveTo(354,501, duration=1)
        pyautogui.mouseDown()
        pyautogui.moveTo(540,502, duration=1)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl','c')
        # Fechar a pagina da nota
        pyautogui.click(1410,18, duration=0.2)
        pyautogui.click(1410,18, duration=0.2)
        # salvar na planilha
        pyautogui.click(318,881, duration=0.5)
        if not sla:
            sla = True
            pyautogui.click(453,202,duration=0.3)
        else:
            pyautogui.press('down')
        pyautogui.hotkey('ctrl','v')
        # voltar para tela de pesquisa
        pyautogui.click(1322,11,duration=0.2)


#print('Novo arquivo excel criado com Sucesso')

#planilha.save(nova_planilha) # Salvar uma nova planilha com os dados modificados