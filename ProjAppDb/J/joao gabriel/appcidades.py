import tkinter as tk
from cidades import cidades

class Application:
    def __init__(self, master=None):
        self.janela1 = tk.Frame(master)
        self.janela1.pack()
        self.msg1 = tk.Label(self.janela1, text="Informe os dados da Cidade:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idcidades_label = tk.Label(self.janela2, text="Id cidade:")
        self.idcidades_label.pack(side="left")
        self.idcidades = tk.Entry(self.janela2, width=20)
        self.idcidades.pack(side="left")

        self.busca = tk.Button(self.janela2, text="buscar", command=self.buscarcidades)
        self.busca.pack()

        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = tk.Label(self.janela3, text="Cidade:")
        self.nome_label.pack(side="left")
        self.nome = tk.Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = tk.Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = tk.Label(self.janela5, text="UF:")
        self.telefone_label.pack(side="left")
        self.telefone = tk.Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela10 = tk.Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = tk.Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela11 = tk.Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = tk.Button(self.janela11, width=10, text="inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = tk.Button(self.janela11, width=10, text="alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = tk.Button(self.janela11, width=10, text="excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

    def buscarcidades(self):
        user = cidades()
        idcidades = self.idcidades.get()
        self.autentic["text"] = user.selectUser(idcidades)
        self.idcidades.delete(0, tk.END)
        self.idcidades.insert(tk.INSERT, user.idcidades)
        self.nome.delete(0, tk.END)
        self.nome.insert(tk.INSERT, user.nome)
        self.telefone.delete(0, tk.END)
        self.telefone.insert(tk.INSERT, user.telefone)
        self.email.delete(0, tk.END)
        self.email.insert(tk.INSERT, user.email)
        self.usuario.delete(0, tk.END)
        self.usuario.insert(tk.INSERT, user.usuario)
        self.senha.delete(0, tk.END)
        self.senha.insert(tk.INSERT, user.senha)

    def inserirUsuario(self):
        user = cidades()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.limparCampos()

    def alterarUsuario(self):
        user = cidades()
        user.idcidades = self.idcidades.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.updateUser()
        self.limparCampos()

    def excluirUsuario(self):
        user = cidades()
        user.idcidades = self.idcidades.get()
        self.autentic["text"] = user.deleteUser()
        self.limparCampos()

    def limparCampos(self):
        self.idcidades.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.telefone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.usuario.delete(0, tk.END)
        self.senha.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    Application(root)
    root.mainloop()
