from tkinter import *
from tkinter import ttk, messagebox

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from appClientes import Clientes

class Cliente:
    def __init__(self, master=None):
        self.master = master
        self.janela21 = Frame(master)
        self.janela21.pack()
        self.msg1 = Label(self.janela21, text="Informe os dados do Cliente:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela22 = Frame(master)
        self.janela22["padx"] = 20
        self.janela22.pack()

        self.idcliente_label = Label(self.janela22, text="ID Cliente:")
        self.idcliente_label.pack(side="left")
        self.idcliente = Entry(self.janela22, width=20)
        self.idcliente.pack(side="left")

        self.busca = Button(self.janela22, text="Buscar", command=self.buscarCliente)
        self.busca.pack()

        self.janela23 = Frame(master)
        self.janela23["padx"] = 20
        self.janela23.pack()

        self.nome_label = Label(self.janela23, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela23, width=30)
        self.nome.pack(side="left")

        # Adicionando a Combobox para selecionar a cidade
        self.janela24 = Frame(master)
        self.janela24["padx"] = 20
        self.janela24.pack()

        self.cidade_label = Label(self.janela24, text="Cidade:")
        self.cidade_label.pack(side="left")
        self.cidade_combobox = ttk.Combobox(self.janela24, width=27)
        self.cidade_combobox.pack(side="left")
        self.carregarCidades()  # Carregar cidades na Combobox

        self.janela25 = Frame(master)
        self.janela25["padx"] = 20
        self.janela25.pack(pady=5)

        self.nascimento_label = Label(self.janela25, text="Nascimento:")
        self.nascimento_label.pack(side="left")
        self.nascimento = Entry(self.janela25, width=28)
        self.nascimento.pack(side="left")

        self.janela26 = Frame(master)
        self.janela26["padx"] = 20
        self.janela26.pack()

        self.cpf_label = Label(self.janela26, text="CPF:")
        self.cpf_label.pack(side="left")
        self.cpf = Entry(self.janela26, width=30)
        self.cpf.pack(side="left")

        self.janela27 = Frame(master)
        self.janela27["padx"] = 20
        self.janela27.pack()

        self.genero_label = Label(self.janela27, text="Gênero:")
        self.genero_label.pack(side="left")
        self.genero = Entry(self.janela27, width=30)
        self.genero.pack(side="left")

        self.janela28 = Frame(master)
        self.janela28["padx"] = 20
        self.janela28.pack()

        self.autentic = Label(self.janela28, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Adicionando os botões para Inserir, Alterar e Excluir
        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack(pady=5)

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirCliente)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarCliente)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirCliente)
        self.botao3.pack(side="left")

        self.botao4 = Button(self.janela11, width=10, text="Voltar", command=self.voltarParaMenu)
        self.botao4.pack(side="left")

        self.botao5 = Button(self.janela11, width=10, text="Exportar PDF", command=self.exportar_para_pdf)
        self.botao5.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Nascimento", "CPF", "Gênero", "Cidade"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Nascimento", text="Nascimento")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Gênero", text="Gênero")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def carregarCidades(self):
        cli = Clientes()
        cidades = cli.selectCidades()
        self.cidade_combobox['values'] = cidades

    def atualizarTabela(self):
        cli = Clientes()
        clientes = cli.selectAllClientes()
        self.tree.delete(*self.tree.get_children())
        for c in clientes:
            self.tree.insert("", "end", values=(c[0], c[1], c[2], c[3], c[4], c[5]))

    def buscarCliente(self):
        cli = Clientes()
        idcliente = self.idcliente.get()
        self.autentic["text"] = cli.selectCliente(idcliente)
        self.idcliente.delete(0, END)
        self.idcliente.insert(INSERT, cli.idcliente)
        self.nome.delete(0, END)
        self.nome.insert(INSERT, cli.nome)
        self.nascimento.delete(0, END)
        self.nascimento.insert(INSERT, cli.nascimento)
        self.cpf.delete(0, END)
        self.cpf.insert(INSERT, cli.cpf)
        self.genero.delete(0, END)
        self.genero.insert(INSERT, cli.genero)
        self.cidade_combobox.set(cli.cidade)

    def inserirCliente(self):
        cli = Clientes(nome=self.nome.get(), nascimento=self.nascimento.get(), cpf=self.cpf.get(), genero=self.genero.get(), cidade=self.cidade_combobox.get())
        result = cli.insertCliente()
        self.autentic["text"] = result
        self.atualizarTabela()

    def alterarCliente(self):
        cli = Clientes(idcliente=self.idcliente.get(), nome=self.nome.get(), nascimento=self.nascimento.get(), cpf=self.cpf.get(), genero=self.genero.get(), cidade=self.cidade_combobox.get())
        result = cli.updateCliente()
        self.autentic["text"] = result
        self.atualizarTabela()

    def excluirCliente(self):
        cli = Clientes(idcliente=self.idcliente.get())
        result = cli.deleteCliente()
        self.autentic["text"] = result
        self.atualizarTabela()

    def voltarParaMenu(self):
        self.master.destroy()  # Fecha a janela atual
        import Principal  # Recarrega o módulo Principal
        root = Tk()
        app = Principal.MainMenu(master=root)
        root.mainloop()

    def exportar_para_pdf(self):
        # Instanciar a classe Cidades para obter os dados
        cliente_obj = Clientes()
        clientes = cliente_obj.selectAllClientes()

        if not isinstance(clientes, list):
            messagebox.showerror("Erro", f"Erro ao buscar cidades: {clientes}")
            return

        # Preparar o arquivo PDF
        pdf_file = "relatorio_clientes.pdf"

        with PdfPages(pdf_file) as pdf:
            # Criar uma nova figura para o relatório
            fig, ax = plt.subplots(figsize=(8, 6))

            # Configuração do layout da tabela
            ax.set_axis_off()
            tbl = ax.table(
                cellText=clientes,
                colLabels=["ID", "Nome", "Cidade", "Nascimento", "CPF", "Gênero"],
                cellLoc='center',
                loc='center'
            )

            tbl.auto_set_font_size(False)
            tbl.set_fontsize(10)
            tbl.scale(1.2, 1.2)

            # Título do relatório
            ax.set_title("Relatório de Cidades", fontweight="bold", fontsize=14)

            # Adicionar o conteúdo ao PDF
            pdf.savefig(fig)
            plt.close()

        messagebox.showinfo("Sucesso", "PDF exportado com sucesso.")

