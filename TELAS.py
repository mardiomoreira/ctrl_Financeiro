import locale
from tkinter import*
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox, Treeview
from FUNCOES import *
from numero import *
from tkcalendar import DateEntry

#Classe pra validar o campo Valor

class TELAS():
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
        def atualizar():
            self.jcadastro.destroy()
            self.cadastro()

            
        self.barradeMenus = Menu(self.jcadastro, tearoff=0)
        self.menuArquivo=Menu(self.barradeMenus, tearoff=0)
        self.menuArquivo.add_command(label='Cad. Categoria',command=self.categoria)
        self.menuArquivo.add_command(label='Pesq. Movimentação',command=self.exibicao)
        self.menuArquivo.add_separator()
        self.menuArquivo.add_command(label='Fechar',command=quit)
        self.menuArquivo.add_command(label='Atualizar',command=atualizar)
        self.barradeMenus.add_cascade(label='Opções',menu=self.menuArquivo)
        self.jcadastro.config(menu=self.barradeMenus)
                ### RÓTULOS ###
        self.ROTULO_titulo = Label(self.jcadastro,text='Cadastro de Movimentação',font=('Ivy',18, 'bold'),bg='#B0E0E6')
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
        self.ENTRADA_data = DateEntry(self.jcadastro,font=('Ivy',11),bg="darkblue", locale='pt_br')
        self.ENTRADA_data.configure(background='red', foreground='yellow')
        self.ENTRADA_data.place(x=45,y=40)
        self.ENTRADA_descricao = Entry(self.jcadastro, justify='center')
        self.ENTRADA_descricao.place(x=255,y=40, width=430)
        ## Validação campo Valor somente números
        self.ENTRADA_valor = Entry(self.jcadastro, justify='center')
        self.ENTRADA_valor.place(x=275,y=70)
        ### BOTÕES ###
        self.BOTAO_cadastrar = Button(self.jcadastro,text='Cadastrar',font=('Ivy',11,'bold'),command=self.addMovimentacao)
        self.BOTAO_cadastrar.place(x=410,y=66)
        self.BOTAO_limpar = Button(self.jcadastro,text='Limpar',font=('Ivy',11,'bold','italic'),command=self.limparcamposMOV)
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
        self.jcadastro.mainloop()
    def addMovimentacao(self):
        self.chave = self.COMBOBOX_categoria.get()
        self.descricao = self.ENTRADA_descricao.get()
        self.data = self.ENTRADA_data.get_date()
        self.valor = self.ENTRADA_valor.get()

        if (self.chave == '')or (self.descricao == '') or (self.data == '') or (self.valor == ''):
              showinfo('AVISO','todos os campos são Obrigatórios!!!')
        else:
            try:
                float(self.valor)  
                self.idcat =  self.dictCOMBO[self.chave]
                self.cat = self.idcat
                self.funcoes = FUNCOES()
                #print(self.data)
                self.funcoes.addMOVIMENTACAO(self.cat,self.descricao,self.data,self.valor)
                showinfo('AVISO',"Cadastro Realizado com Sucesso!!!")
                for i in self.tree.get_children():
                    self.tree.delete(i)
                self.funcoes = FUNCOES()
                self.linhas= self.funcoes.treeviewCadastro()
                #print(self.linhas)
                for (id,descricao,categoria,data,valor) in self.linhas:
                    self.tree.insert('',END,values=(id,descricao,categoria,data,valor))
                for i in self.tree.get_children():
                    self.tree.delete(i)
                self.funcoes = FUNCOES()
                self.linhas= self.funcoes.treeviewCadastro()
                for (id,descricao,categoria,data,valor) in self.linhas:
                    valor_FORM = real(valor)
                    self.tree.insert('',END,values=(id,descricao,categoria,data,valor_FORM))
                self.limparcamposMOV()
            except ValueError:
                showinfo('Validação', 'O campo VALOR deve ser somente numeros \n ou separado por pontos as casas decimais')
    def limparcamposMOV(self):
        self.ENTRADA_data.delete(0,END)
        self.ENTRADA_descricao.delete(0,END)
        self.ENTRADA_valor.delete(0,END)
        self.COMBOBOX_categoria.delete(0,END)
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
        self.largura = 700
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
        ### TREEVIEW
        # Add Some Style
        self.style = ttk.Style()
        # Pick A Theme
        self.style.theme_use('default')
        self.style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        # Change Selected Color
        self.style.map('Treeview',
            background=[('selected', "#347083")])
        
        self.columns = ('col01', 'col02', 'col03', 'col04', 'col05')
        self.TREEVIEW_pesquisa = Treeview(self.jexibicao, columns=self.columns, show='headings')
        # definindo Títulos
        self.TREEVIEW_pesquisa.heading('col01', text='ID', anchor='center')
        self.TREEVIEW_pesquisa.heading('col02', text='Tipo', anchor='center')
        self.TREEVIEW_pesquisa.heading('col03', text='Descrição', anchor='center')
        self.TREEVIEW_pesquisa.heading('col04', text='Data', anchor='center')
        self.TREEVIEW_pesquisa.heading('col05', text='Valor', anchor='center')
        # Configurando tamanho de Cada Coluna
        self.TREEVIEW_pesquisa.column('col01',width=30,minwidth=30,anchor='center')
        self.TREEVIEW_pesquisa.column('col02',width=30,minwidth=30,anchor='center')
        self.TREEVIEW_pesquisa.column('col03',width=30,minwidth=30,anchor='center')
        self.TREEVIEW_pesquisa.column('col04',width=30,minwidth=30,anchor='center')
        self.TREEVIEW_pesquisa.column('col05',width=30,minwidth=30,anchor='center')
        # add a scrollbar
        self.TV_altura = 170
        self.scrollbar = Scrollbar(self.jexibicao, orient=VERTICAL, command=self.TREEVIEW_pesquisa.yview)
        self.TREEVIEW_pesquisa.configure(yscroll=self.scrollbar.set, selectmode="extended")
        # Posicionando
        self.TREEVIEW_pesquisa_Altura = self.altura
        self.TREEVIEW_pesquisa.place(x=7,y=50, width=(self.largura)-30,height=(self.TREEVIEW_pesquisa_Altura)-120)
        #print((self.TREEVIEW_pesquisa_Altura)-120)
        self.scrollbar.place(x=(self.largura)-23,y=50,height=(self.TREEVIEW_pesquisa_Altura)-120)
        # Colorindo Coluna
        self.TREEVIEW_pesquisa.tag_configure('oddrow', background="lightblue")
        self.TREEVIEW_pesquisa.tag_configure('evenrow', background="white")
        self.contador = 0
        ### Entradas Datas
        self.ENTRADA_datamenor = DateEntry(self.jexibicao,font=('Ivy',11),bg="darkblue", locale='pt_br')
        self.ENTRADA_datamaior = DateEntry(self.jexibicao,font=('Ivy',11),bg="darkblue", locale='pt_br')
        self.ENTRADA_datamenor.place(x=100, y=5)
        self.ENTRADA_datamaior.place(x=400,y=5)
        self.ENTRADA_renda = Entry(self.jexibicao, justify='center')
        self.ENTRADA_despesa = Entry(self.jexibicao, justify='center')
        self.ENTRADA_saldo = Entry(self.jexibicao, justify='center')
        self.ENTRADA_renda.place(x=(self.largura)-630,y=(self.altura)-40, width=60)
        self.ENTRADA_despesa.place(x=(self.largura)-360,y=(self.altura)-40, width=60)
        self.ENTRADA_saldo.place(x=(self.largura)-90,y=(self.altura)-40, width=60)
        #print((self.altura)-40)
        ### ROTULOS
        self.ROTULO_datamenor = Label(self.jexibicao,text='Data Menor: ',font=('Ivy',12,'italic','bold'),bg='#B0E0E6')
        self.ROTULO_datamenor.place(x=2,y=5)
        self.ROTULO_datamaior= Label(self.jexibicao,text='Data Maior: ',font=('Ivy',12,'italic','bold'),bg='#B0E0E6')
        self.ROTULO_datamaior.place(x=302,y=5)
        self.ROTULO_renda = Label(self.jexibicao,text='Renda: ',font=('Ivy',12,'italic','bold'),bg='#B0E0E6')
        self.ROTULO_despesa = Label(self.jexibicao,text='Despesa: ',font=('Ivy',12,'italic','bold'),bg='#B0E0E6')
        self.ROTULO_saldo = Label(self.jexibicao,text='Saldo: ',font=('Ivy',12,'italic','bold'),bg='#B0E0E6')
        self.ROTULO_renda.place(x=5,y=(self.altura)-45)
        self.ROTULO_despesa.place(x=(self.largura)-445,y=(self.altura)-45)
        self.ROTULO_saldo.place(x=(self.largura)-150,y=(self.altura)-45)
        ## Botoes
        self.BOTAO_pesquisar = Button(self.jexibicao,text='Pesquisar', activebackground='red', activeforeground='white',font=('Ivy',11,'bold'),command=self.pesquisarMOVIMENTACAO)
        self.BOTAO_pesquisar.place(x=550,y=5)
        self.jexibicao.mainloop()
    def pesquisarMOVIMENTACAO(self):
        self.datamenor = self.ENTRADA_datamenor.get_date()
        self.datamaior = self.ENTRADA_datamaior.get_date()
        self.datamenor_formatada = self.datamenor.strftime('%d/%m/%Y')
        self.datamaior_formatada = self.datamaior.strftime('%d/%m/%Y')
        # Popular Treeview
        for i in self.TREEVIEW_pesquisa.get_children():
            self.TREEVIEW_pesquisa.delete(i)
        self.funcoes = FUNCOES()
        self.res = self.funcoes.pesquisaDatas(self.datamaior,self.datamenor)
        for (id,descricao,categoria,data,valor) in self.res:
            valor_formatado = real(valor)
            ndata=self.funcoes.dataFORMATADA_BR(data)
            if self.contador % 2 == 0:
                self.TREEVIEW_pesquisa.insert('',END,values=(id,descricao,categoria,ndata,valor_formatado), tags=('evenrow',))
            else:
                self.TREEVIEW_pesquisa.insert('',END,values=(id,descricao,categoria,ndata,valor_formatado), tags=('oddrow',))
            self.contador +=1
        ## Pesquisar Despesa
        #print(f"""SELECT SUM(mov_valor) FROM vw_movimentacao WHERE tipo_cat = 'RENDA' AND mov_data BETWEEN '{self.datamenor}' AND '{self.datamaior}';""")
        self.despesa = self.funcoes.pesquisaDESPESAS(self.datamaior,self.datamenor)
        for despesa in self.despesa:
            self.ENTRADA_despesa.insert(0,real(despesa[0]))
            self.despesa = despesa[0]
        ## Pesquisar Renda
        self.renda = self.funcoes.pesquisaRENDA(self.datamaior,self.datamenor)
        #print(self.renda)
        for renda in self.renda:
            self.ENTRADA_renda.insert(0,real(renda[0]))
            self.renda = renda[0]
        ## Comparando as Datas
        # if self.datamenor_formatada > self.datamaior_formatada:
        #     print('IN maior que FIN')
        # else:
        #     print('FIN maior que IN')
        self.saldo = self.renda - self.despesa
        self.ENTRADA_saldo.insert(0,real(self.saldo))
            
## Chamar as funções do banco e da tela
banco = FUNCOES()
banco.conectarBD()
banco.criarTabelas()
banco.criar_tbl_movimentacao()
banco.criar_view_movimentacao()
banco.desconectar_bd()
telas = TELAS()
telas.cadastro()

