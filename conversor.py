from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Conversor de Unidade (kg)')
app.resizable(False, False)


# Configuração das funções para cálculos

def convert_grama():
    global valor
    try:
        convert = str(entrada.get()).replace(',', '.')
        if entrada.get() == '' or entrada.get() == ' ':
            valor = 0
        else:
            valor = float(convert)
        result = valor * 1000
        saida = '{} kg = {} g'.format(valor, result)
        resultado['text'] = saida
        print(saida)
    except:
        resultado['text'] = 'Entrada Inválida!'


def convert_libra():
    global valor
    try:
        convert = str(entrada.get()).replace(',', '.')
        if entrada.get() == '' or entrada.get() == ' ':
            valor = 0
        else:
            valor = float(convert)
        result = valor * 2.20462
        saida = '{} kg = {} lib'.format(valor, result)
        resultado['text'] = saida
        print(saida)
    except:
        resultado['text'] = 'Entrada Inválida!'


def convert_onca():
    global valor
    try:
        convert = str(entrada.get()).replace(',', '.')
        if entrada.get() == '' or entrada.get() == ' ':
            valor = 0
        else:
            valor = float(convert)
        result = valor * 35.274
        saida = '{} kg = {} onc'.format(valor, result)
        resultado['text'] = saida
        print(saida)
    except:
        resultado['text'] = 'Entrada Inválida!'


def fechar():
    sair = messagebox.askquestion('Fechar', 'Deseja fechar a Aplicação?')
    if sair == messagebox.YES:
        app.destroy()
    else:
        pass


texto = Label(app, text='Quantidade em kg :', height=1, font=('sans-serif', 11, 'normal'))
texto.grid(row=0, column=0, padx=2)

entrada = Entry(app, font=('sans-serif', 12, 'bold'))
entrada.grid(row=0, column=1, columnspan=3)

grama = Button(app, text='Grama', font=('sans-serif', 12, 'bold'), cursor='hand2', width=5, command=convert_grama)
grama.grid(row=2, column=0, pady=10, columnspan=1)

libra = Button(app, text='Libra', font=('sans-serif', 12, 'bold'), cursor='hand2', width=5, command=convert_libra)
libra.grid(row=2, column=1, pady=10, columnspan=1)

onca = Button(app, text='Onça', font=('sans-serif', 12, 'bold'), cursor='hand2', width=5, command=convert_onca)
onca.grid(row=2, column=2, pady=10, columnspan=3)

resultado = Label(app, text='Resultado', bg='blue', fg='white', font=('Arial', 15, 'normal'), width=30, height=1)
resultado.grid(row=3, column=0, padx=10, pady=10, columnspan=5)

fechar = Button(app, text='Fechar', width=10, font=('sans-serif', 16, 'bold'), cursor='hand2', bg='red', fg='white',
                command=fechar)
fechar.grid(row=4, column=0, padx=10, pady=10, columnspan=4)

app.mainloop()
