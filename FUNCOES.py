from ast import Return
from tkinter import *
from tkinter.messagebox import showinfo
import sqlite3
class FUNCOES():
    def conectarBD(self):
        self.conn = sqlite3.connect("financeiro.db3")
        self.cursor = self.conn.cursor()
    def desconectar_bd(self):
        self.conn.close()
    def criarTabelas(self):
        self.conectarBD(); print("Conectando ao Banco de Dados!!!")
        ### Criar tabela
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_categoria (
                                id_cat           INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
                                tipo_cat         VARCHAR (7)  NOT NULL,
                                descri_cat       VARCHAR (50) NOT NULL,
                                datacadastro_cat DATE         DEFAULT (CURRENT_DATE) 
                                    );
                        """)
        self.conn.commit();print("Banco de dados criado!!!")
        self.desconectar_bd();print("Banco de Dados desconectado")
    def criar_tbl_movimentacao(self):
        self.conectarBD()
        ## Criar a tabela
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_movimentacao (
                                id_mov          INTEGER      PRIMARY KEY AUTOINCREMENT
                                                            NOT NULL,
                                fk_categoria_id              REFERENCES tbl_categoria (id_cat) ON DELETE RESTRICT
                                                            NOT NULL,
                                mov_descricao   VARCHAR (40),
                                mov_data        DATE,
                                mov_valor       DECIMAL
                                    );
                        """)
        self.conn.commit();print("tabela Movimentacao Criada com Sucesso")
        self.desconectar_bd();print("Banco de Dados desconectado")
    def criar_view_movimentacao(self):
        self.conectarBD()
        self.cursor.execute(""" CREATE VIEW IF NOT EXISTS vw_movimentacao 
                            AS SELECT * FROM tbl_movimentacao INNER JOIN 
                            tbl_categoria ON tbl_categoria.id_cat = tbl_movimentacao.fk_categoria_id; """)
        self.conn.commit();print("View Movimentação criado com sucesso!!!")
    def addCOTEGORIA(self,tipo,descricao):
            self.conectarBD()
            self.cursor.execute("""INSERT INTO tbl_categoria (tipo_cat, descri_cat) VALUES (?,?)""",(tipo,descricao))
            self.conn.commit()
            showinfo('Aviso','Cadastro Realizado com Sucesso!!!')
    def addMOVIMENTACAO(self,categoria,descricao,data,valor):
            self.conectarBD()
            self.cursor.execute(""" INSERT INTO tbl_movimentacao (
                                    fk_categoria_id, 
                                    mov_descricao, 
                                    mov_data, 
                                    mov_valor)  
                                    VALUES (?,?,?,?)""",(categoria,descricao,data,valor))
            self.conn.commit()
            self.desconectar_bd()
    def popularTREEVIEWcategoria(self):
        self.conectarBD()
        self.cursor.execute('select id_cat,tipo_cat,descri_cat FROM tbl_categoria;')
        self.rows = self.cursor.fetchall()
        return self.rows
    def combo_categoria(self):
        self.dictCOMBO = {}
        self.listaCOMBO = []
        self.conectarBD()
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT id_cat,descri_cat FROM tbl_categoria;')
        self.rowsCOMBO = self.cur.fetchall()
        return self.rowsCOMBO
    def treeviewCadastro(self):
        self.conectarBD()
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT id_mov, mov_descricao, descri_cat,mov_data,mov_valor FROM vw_movimentacao;')
        self.rowstreview = self.cur.fetchall()
        return self.rowstreview
