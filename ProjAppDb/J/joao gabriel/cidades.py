from Banco import Banco

class cidades:
    def __init__(self, idcidades=0, nome="", UF=""):
        self.idcidades = idcidades
        self.nome = nome
        self.UF = UF

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (nome, UF) VALUES (?, ?)",
                      (self.nome, self.UF))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {str(e)}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? WHERE idcidades = ?",
                      (self.nome, self.UF, self.idcidades))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {str(e)}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidades = ?", (self.idcidades,))
            banco.conexao.commit()
            c.close()
            return "cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {str(e)}"

    def selectUser(self, idcidades):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidades = ?", (idcidades,))
            for linha in c:
                self.idcidades = linha[0]
                self.nome = linha[1]
                self.UF = linha[2]

            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {str(e)}"
