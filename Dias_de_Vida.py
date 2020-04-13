from datetime import *
from tkinter import *

janela = Tk()
janela.title('Dias de Vida')
janela.iconbitmap('LSoft.ico')
janela.resizable(False, False)
janela.config(bg='gray')

hoje = date.today()
dia = ''
mes = ''
ano = ''
nascimento = 0


def calcular():
    global dia, mes, ano, nascimento
    dia = dias.get()
    mes = meses.get()
    ano = anos.get()

    nascimento1 = (dia + '-' + mes + '-' + ano)
    nascimento = date(int(nascimento1[6:11]), int(nascimento1[3:5]), int(nascimento1[0:2]))
    data = hoje - nascimento
    saida['text'] = ('Você viveu {} dias'.format(data.days).upper())


titulo = Label(janela, bg='gray', fg='white', font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'),
               text='Dias que Você já viveu'.upper())
titulo.pack()

frame = Frame(janela, bg='skyblue3', width=430, height=350)
frame.pack()

dia1 = Label(frame, fg='black', bg='skyblue3', text='Dia do Seu Nascimento', font=('Arial sans serif', 14, 'bold'))
dia1.grid(row=1, column=0, padx=3, pady=3)

dias = Entry(frame, font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'), bd=2, width=10)
dias.grid(row=1, column=1, padx=3, pady=3)

mes1 = Label(frame, fg='black', bg='skyblue3', text='Mês do seu Nascimento', font=('Arial sans serif', 14, 'bold'))
mes1.grid(row=2, column=0, padx=3, pady=3)

meses = Entry(frame, font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'), bd=2, width=10)
meses.grid(row=2, column=1, padx=3, pady=3)

ano1 = Label(frame, fg='black', bg='skyblue3', text='Ano do seu Nascimento', font=('Arial sans serif', 14, 'bold'))
ano1.grid(row=3, column=0, padx=3, pady=3)

anos = Entry(frame, font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'), bd=2, width=10)
anos.grid(row=3, column=1, padx=3, pady=3)

botao = Button(frame, command=calcular, bg='green3', text='Calcular', font=('Arial sans serif', 18, 'bold'), height=4)
botao.grid(row=1, column=3, padx=3, pady=2, rowspan=3)

resultado = Label(frame, fg='blue4', bg='skyblue3', font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 25, 'bold'),
                  text='Resultado'.upper(), bd=5)
resultado.grid(row=4, column=0, padx=5, pady=10, columnspan=3)

saida = Label(frame, bg='skyblue3', fg='red4', font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'),
              text='Olha Aqui'.upper(), bd=3)
saida.grid(row=6, column=0, columnspan=3)

janela.mainloop()
