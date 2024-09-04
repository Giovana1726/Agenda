import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios(
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT)""")
        self.conexao.commit()

        def createTable(self):
            c = self.conexao.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS tbl_cidades(
                   idcidades INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   UF TEXT)""")
            self.conexao.commit()
        c.close()
