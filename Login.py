from tkinter import Label, Frame, Entry, Button, messagebox
from tkinter import *
from Banco import Banco
from Principal import MainMenu as Mainform
class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")

        self.janela39 = Frame(master)
        self.janela39["padx"] = 20
        self.janela39.pack()

        self.img = PhotoImage(file="login.png")
        self.lblimg = Label(self.janela39, image=self.img)
        self.lblimg.pack()

        # Criar e exibir o frame para o campo de usuário
        self.janela40 = Frame(master)
        self.janela40["padx"] = 20
        self.janela40.pack()

        self.usuario_label = Label(self.janela40, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela40, width=20)
        self.usuario.pack(side="left")

        # Criar e exibir o frame para o campo de senha
        self.janela41 = Frame(master)
        self.janela41["padx"] = 20
        self.janela41.pack()

        self.senha_label = Label(self.janela41, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela41, width=20, show="*")  # Oculta o texto da senha
        self.senha.pack(side="left")

        # Criar e exibir o frame para o botão de login
        self.janela42 = Frame(master)
        self.janela42["padx"] = 20
        self.janela42.pack()

        self.botao10 = Button(self.janela42, width=10, text="Login", command=self.entrar)
        self.botao10.pack(side="left")

    def entrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        banco = Banco()
        cursor = banco.conexao.cursor()

        # Verificar se o usuário e a senha estão corretos
        cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario=? AND senha=?", (usuario, senha))
        igual = cursor.fetchone()  # Corrigido o nome da variável para 'igual'

        if igual:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.abrir()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        cursor.close()

    def abrir(self):
        self.new_window = Toplevel(self.master)
        self.app = Mainform(self.new_window)

if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    app = Login(master=root)
    root.mainloop()
