import tkinter as tk
from Usuarios import Usuarios

class Application:
    def __init__(self, master=None):
        self.janela1 = tk.Frame(master)
        self.janela1.pack()
        self.msg1 = tk.Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = tk.Label(self.janela2, text="Id usuario:")
        self.idusuario_label.pack(side="left")
        self.idusuario = tk.Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = tk.Button(self.janela2, text="buscar", command=self.buscarUsuario)
        self.busca.pack()

        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = tk.Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = tk.Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = tk.Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = tk.Label(self.janela5, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = tk.Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela6 = tk.Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.email_label = tk.Label(self.janela6, text="E-mail:")
        self.email_label.pack(side="left")
        self.email = tk.Entry(self.janela6, width=30)
        self.email.pack(side="left")

        self.janela7 = tk.Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack(pady=5)

        self.usuario_label = tk.Label(self.janela7, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela7, width=29)
        self.usuario.pack(side="left")

        self.janela4 = tk.Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack(pady=5)

        self.senha_label = tk.Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela4, width=30, show="*")
        self.senha.pack(side="left")

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

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        self.autentic["text"] = user.selectUser(idusuario)
        self.idusuario.delete(0, tk.END)
        self.idusuario.insert(tk.INSERT, user.idusuario)
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
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.limparCampos()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.updateUser()
        self.limparCampos()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        self.autentic["text"] = user.deleteUser()
        self.limparCampos()

    def limparCampos(self):
        self.idusuario.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.telefone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.usuario.delete(0, tk.END)
        self.senha.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    Application(root)
    root.mainloop()
