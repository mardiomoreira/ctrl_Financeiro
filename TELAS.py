from ast import For
from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox, Treeview
from wsgiref import validate
from FUNCOES import *
from numero import *
from tkcalendar import DateEntry
#Classe pra validar o campo Valor
class window2():
    def __init__(self):
        pass
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

class TELAS(window2):
    def cadastro(self):
        self.jcadastro = Tk()
        self.jcadastro.title('Cadastro de Movimentação')
        self.largura = 700
        self.altura = 400
        self.largura_screen = self.jcadastro.winfo_screenwidth()
        self.altura_screen = self.jcadastro.winfo_screenheight()
        self.posX = self.largura_screen/2 - self.largura/2
        self.posY = self.altura_screen/2 - self.altura/2
        self.jcadastro.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posY))
        self.jcadastro.configure(bg='#B0E0E6')
        self.jcadastro.resizable(width=0,height=0)
        #criação do menu principal
        def quit():
            self.jcadastro.destroy()
        self.barradeMenus = Menu(self.jcadastro, tearoff=0)
        self.menuArquivo=Menu(self.barradeMenus, tearoff=0)
        self.menuArquivo.add_command(label='Categoria',command=self.categoria)
        self.menuArquivo.add_command(label='Movimentação',command=self.exibicao)
        self.menuArquivo.add_separator()
        self.menuArquivo.add_command(label='Fechar',command=quit)
        self.barradeMenus.add_cascade(label='Arquivo',menu=self.menuArquivo)
        self.jcadastro.config(menu=self.barradeMenus)
                ### RÓTULOS ###
        self.ROTULO_titulo = Label(self.jcadastro,text='Cadastro de Movimentação',font=('Ivy',18, 'bold'),bg='red')
        self.ROTULO_titulo.place(x=0,y=0, width=self.largura)
        self.ROTULO_data = Label(self.jcadastro, text='Data: ', font=('Ivy',10, 'bold'))
        self.ROTULO_data.place(x=1,y=40)
        self.ROTULO_data.configure(bg='#B0E0E6')
        self.ROTULO_descricao = Label(self.jcadastro, text='Descrição: ', font=('Ivy',10, 'bold'),bg='#B0E0E6')
        self.ROTULO_descricao.place(x=180,y=40)
        self.ROTULO_categoria = Label(self.jcadastro, text='Categoria: ', font=('Ivy',10, 'bold'),bg='#B0E0E6')
        self.ROTULO_categoria.place(x=1,y=70)
        self.ROTULO_valor = Label(self.jcadastro, text='Valor: ', font=('Ivy',10, 'bold'),bg='#B0E0E6')
        self.ROTULO_valor.place(x=230,y=70)
                ### ENTRADA ###
        self.ENTRADA_data = DateEntry(self.jcadastro,font=('Ivy',11),bg="darkblue",locale='pt_br')
        self.ENTRADA_data.configure(background='red', foreground='yellow')
        self.ENTRADA_data.place(x=45,y=40)
        self.ENTRADA_descricao = Entry(self.jcadastro, justify='center')
        self.ENTRADA_descricao.place(x=255,y=40, width=430)
        ## Validação campo Valor somente números
        self.vcmd = (self.jcadastro.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.ENTRADA_valor = Entry(self.jcadastro, justify='center', validate = 'key', validatecommand = self.vcmd)
        self.ENTRADA_valor.place(x=275,y=70)
        ### BOTÕES ###
        self.BOTAO_cadastrar = Button(self.jcadastro,text='Cadastrar',font=('Ivy',11,'bold'),command=self.addMovimentacao)
        self.BOTAO_cadastrar.place(x=410,y=66)
        self.BOTAO_limpar = Button(self.jcadastro,text='Limpar',font=('Ivy',11,'bold','italic'))
        self.BOTAO_limpar.place(x=505,y=66)
        ### COMBO ###
        self.COMBOBOX_categoria = Combobox(self.jcadastro)
        self.COMBOBOX_categoria.place(x=75,y=70)
        ## Popular ComboBox
        self.funcoes = FUNCOES()
        self.rowsCOMBO = self.funcoes.combo_categoria()
        self.dictCOMBO = {}
        self.listaCOMBO = []
        for i in self.rowsCOMBO:
            self.dictCOMBO[i[1]]= i[0]
            self.listaCOMBO.append(i[1])
        self.COMBOBOX_categoria['values'] = self.listaCOMBO
        ### TREEVIEW
        self.columns = ('col01', 'col02', 'col03', 'col04', 'col05')
        self.tree = Treeview(self.jcadastro, columns=self.columns, show='headings')
        # definindo Títulos
        self.tree.heading('col01', text='ID', anchor='center')
        self.tree.heading('col02', text='Descrição', anchor='center')
        self.tree.heading('col03', text='Categoria', anchor='center')
        self.tree.heading('col04', text='Data', anchor='center')
        self.tree.heading('col05', text='Valor', anchor='center')
        # Configurando tamanho de Cada Coluna
        self.tree.column('col01',width=30,minwidth=30)
        self.tree.column('col02',width=30,minwidth=30)
        self.tree.column('col03',width=30,minwidth=30)
        self.tree.column('col04',width=30,minwidth=30)
        self.tree.column('col05',width=15,minwidth=15)
        # add a scrollbar
        self.scrollbar = Scrollbar(self.jcadastro, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        # Posicionando
        self.tree.place(x=1,y=120, width=self.largura-20, height=350)
        self.scrollbar.place(x=680,y=120,height=350)
    
        # Popular Treeview
        for i in self.tree.get_children():
             self.tree.delete(i)
        self.funcoes = FUNCOES()
        self.linhas= self.funcoes.treeviewCadastro()
        #print(self.linhas)
        for (id,descricao,categoria,data,valor) in self.linhas:
            self.tree.insert('',END,values=(id,descricao,categoria,data,valor))
            
        self.jcadastro.mainloop()
    def addMovimentacao(self):
        self.chave = self.COMBOBOX_categoria.get()
        self.descricao = self.ENTRADA_descricao.get()
        self.data = self.ENTRADA_data.get()
        self.valor = float(self.ENTRADA_valor.get())
        self.valor = real(self.valor) 
        # showinfo('Categoria','chave da categoria: '+str(self.idcat))
        # showinfo('Categoria','Descrição: '+str(self.descricao))
        # showinfo('Categoria','Data: '+str(self.data))
        # showinfo('Categoria','Valor: '+str(self.valor))
        if (self.chave == '')or (self.descricao == '') or (self.data == '') or (self.valor == ''):
              showinfo('AVISO','todos os campos são Obrigatórios!!!')
        else:
          self.idcat =  self.dictCOMBO[self.chave]
          self.cat = self.idcat
          self.funcoes = FUNCOES()
          self.funcoes.addMOVIMENTACAO(self.cat,self.descricao,self.data,self.valor)
          showinfo('AVISO',"Cadastro Realizado com Sucesso!!!")
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.funcoes = FUNCOES()
        self.linhas= self.funcoes.treeviewCadastro()
        #print(self.linhas)
        for (id,descricao,categoria,data,valor) in self.linhas:
            self.tree.insert('',END,values=(id,descricao,categoria,data,valor))
          
    def categoria(self):
        self.funcoes = FUNCOES()
        self.jcategoria = Toplevel()
        self.jcategoria.title('Cadastro de Categoria - Controle Financeiro')
        self.jcategoria.focus_force()
        self.jcategoria.grab_set()
        self.largura = 400
        self.altura = 300
        self.largura_screen = self.jcategoria.winfo_screenwidth()
        self.altura_screen = self.jcategoria.winfo_screenheight()
        self.posX = self.largura_screen/2 - self.largura/2
        self.posY = self.altura_screen/2 - self.altura/2
        self.jcategoria.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posY))
        self.jcategoria.configure(bg='#B0E0E6')
        # Não permitir Redimensionamento
        self.jcategoria.resizable(width=0,height=0)
        ### Componentes ###
                ### ROTULOS ###
        self.ROTULO_titulo = Label(self.jcategoria,text='Cadastro de Categoria',font=('Ivy',18, 'bold'),bg='red')
        self.ROTULO_titulo.place(x=0,y=0, width=self.largura)
        self.ROTULO_tipo = Label(self.jcategoria,text='Tipo: ',font=('Ivy',12,'italic'),bg='#B0E0E6')
        self.ROTULO_tipo.place(x=10,y=40)
        self.ROTULO_descricao = Label(self.jcategoria,text='Descrição: ',font=('Ivy',12,'italic'),bg='#B0E0E6')
        self.ROTULO_descricao.place(x=10,y=80)
        ### ComboBox ###
        self.COMBOBOX_tipo = Combobox(self.jcategoria, values=['RENDA','DESPESA'],justify='center')
        self.COMBOBOX_tipo.place(x=55,y=42)
        ### ENTRADAS ###
        self.ENTRADAS_descricao = Entry(self.jcategoria, justify='center')
        self.ENTRADAS_descricao.place(x=92,y=82, width=(self.largura)-190)
        ### BOTAO ###
        self.BOTOES_cadastrar = Button(self.jcategoria,text='Cadastrar', activebackground='red', activeforeground='white',font=('Ivy',11,'bold'),command=self.cad_Categoria)
        self.BOTOES_cadastrar.place(x=310,y=78)
        ### TREEVIEW ###
        self.columns = ('col01', 'col02', 'col03')
        self.tv = Treeview(self.jcategoria, columns=self.columns, show='headings')
        # definindo Títulos
        self.tv.heading('col01', text='ID', anchor='center')
        self.tv.heading('col02', text='Tipo', anchor='center')
        self.tv.heading('col03', text='Descrição', anchor='center')
        # Configurando tamanho de Cada Coluna
        self.tv.column('col01',width=30,minwidth=30,anchor='center')
        self.tv.column('col02',width=30,minwidth=30,anchor='center')
        self.tv.column('col03',width=30,minwidth=30,anchor='center')
        # add a scrollbar
        self.TV_altura = 170
        self.scrollbar = Scrollbar(self.jcategoria, orient=VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=self.scrollbar.set)
        # Posicionando
        self.tv.place(x=1,y=120, width=(self.largura)-30,height=self.TV_altura)
        self.scrollbar.place(x=(self.largura)-30,y=120,height=self.TV_altura)
        self.popularTreviewcadastro()
        self.jcategoria.mainloop()
    def popularTreviewcadastro(self):
        # Limpando Treeview
        for i in self.tv.get_children():
            self.tv.delete(i)
        ## Populando a Treeview
        self.funcoes = FUNCOES()
        self.linhas= self.funcoes.popularTREEVIEWcategoria()
        for (id,tipo,descricao) in self.linhas:
            self.tv.insert('',END,values=(id,tipo,descricao))

    def cad_Categoria(self):
        self.funcoes = FUNCOES()
        self.tipo = self.COMBOBOX_tipo.get()
        self.descricao = self.ENTRADAS_descricao.get()
        if (self.tipo == '') or (self.descricao == ''):
            showinfo('Validação de Campos','todos os Campos Obrigatório!!')
        else:
            self.funcoes.addCOTEGORIA(self.tipo, self.descricao)
        for i in self.tv.get_children():
            self.tv.delete(i)
        self.funcoes = FUNCOES()
        self.linhas= self.funcoes.popularTREEVIEWcategoria()
        for (id,tipo,descricao) in self.linhas:
            self.tv.insert('',END,values=(id,tipo,descricao))
    def exibicao(self):
        self.jexibicao = Toplevel()
        self.jexibicao.title('Movimentação')
        self.largura = 500
        self.altura = 300
        self.jexibicao.focus_force()
        self.jexibicao.grab_set()
        self.largura_screen = self.jexibicao.winfo_screenwidth()
        self.altura_screen = self.jexibicao.winfo_screenheight()
        self.posX = self.largura_screen/2 - self.largura/2
        self.posY = self.altura_screen/2 - self.altura/2
        self.jexibicao.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posX, self.posY))
        self.jexibicao.configure(bg='#B0E0E6')
        self.jexibicao.resizable(width=0,height=0)
        self.jexibicao.mainloop()
        
telas = TELAS()
telas.cadastro()