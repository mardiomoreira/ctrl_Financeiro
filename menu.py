from tkinter import *
def semcomando():
    print('Nada')
def quit():
    app.destroy()
app=Tk()
app.title('CFB Cursos')
app.geometry('500x300')
app.configure(background='#dde')
barradeMenus = Menu(app)
menuArquivo=Menu(barradeMenus)
menuArquivo.add_command(label='Novo',command=semcomando)
menuArquivo.add_command(label='Pesquisar',command=semcomando)
menuArquivo.add_command(label='Deletar',command=semcomando)
menuArquivo.add_separator()
menuArquivo.add_command(label='Fechar',command=quit)
barradeMenus.add_cascade(label='Arquivo',menu=menuArquivo)
app.config(menu=barradeMenus)

app.mainloop()