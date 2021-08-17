#Conversor de imagens
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import pyautogui


def ImportaPNG():

    global im

    Importar = filedialog.askopenfilename()
    im = Image.open(Importar).convert('RGB')


    resposta['text'] = f'''
    Click no botão abaixo pra converter a imagem
    em seguida escolha o local pra salvar!
    '''

def ConvertePNG():

    global im

    Exportar = filedialog.asksaveasfilename(defaultextension='.jpg')
    im.save(Exportar)
    pyautogui.alert('Imagem convertida e salva com sucesso!')
    janela.destroy()


janela = Tk()
janela.title('Conversor de PNG para JPG')
texto = Label(janela, text='Importe a imagem PNG clicando no botão abaixo!', bg='royalblue', fg='white', font=('helvetica', 15, 'bold'))
texto.grid(column=0, row=0, padx=30, pady=30)
janela.resizable(0, 0)

botao_import = Button(janela, text='Importar imagem PNG', bg='azure3', command=ImportaPNG)
botao_import.grid(column=0, row=10, padx=10, pady=10)

resposta = Label(janela, text='',  fg='red', font=('helvetica', 10, 'bold'))
resposta.grid(column=0, row=11, padx=0, pady=0)

botao_convert = Button(janela, text='Converter PNG para JPG', bg='azure3', command=ConvertePNG)
botao_convert.grid(column=0, row=12, padx=10, pady=10)

by = Label(janela, text='By Saulo 2021', font=('helvetica', 7, 'bold'))
by.grid(column=0, row=13, padx=0, pady=0)


janela.mainloop()

