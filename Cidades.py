from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from appCidades import Cidades  # Correto: a classe que você está usando


class Cidade:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerenciamento de Cidades")  # Título da janela
        self.janela21 = Frame(master)
        self.janela21.pack()
        self.msg1 = Label(self.janela21, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela22 = Frame(master)
        self.janela22["padx"] = 20
        self.janela22.pack()

        self.idcidade_label = Label(self.janela22, text="Id cidade:")
        self.idcidade_label.pack(side="left")
        self.idcidade = Entry(self.janela22, width=20)
        self.idcidade.pack(side="left")

        self.busca = Button(self.janela22, text="Buscar", command=self.buscarCidade)
        self.busca.pack()

        self.janela23 = Frame(master)
        self.janela23["padx"] = 20
        self.janela23.pack()

        self.cidade_label = Label(self.janela23, text="Cidade:")
        self.cidade_label.pack(side="left")
        self.cidade = Entry(self.janela23, width=30)
        self.cidade.pack(side="left")

        self.janela24 = Frame(master)
        self.janela24["padx"] = 20
        self.janela24.pack(pady=5)

        self.uf_label = Label(self.janela24, text="UF:")
        self.uf_label.pack(side="left")
        self.uf = Entry(self.janela24, width=28)
        self.uf.pack(side="left")

        self.janela25 = Frame(master)
        self.janela25["padx"] = 20
        self.janela25.pack()

        self.autentic = Label(self.janela25, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Adicionando os botões para Inserir, Alterar e Excluir
        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack(pady=5)

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirCidade)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarCidade)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirCidade)
        self.botao3.pack(side="left")

        self.botao4 = Button(self.janela11, width=10, text="Voltar", command=self.voltarParaMenu)
        self.botao4.pack(side="left")

        # Botão para Exportar Relatório
        self.botao5 = Button(self.janela11, width=10, text="Exportar PDF", command=self.exportar_para_pdf)
        self.botao5.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Cidade", "UF"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def atualizarTabela(self):
        cid = Cidades()
        cidades = cid.selectAllCidades()
        self.tree.delete(*self.tree.get_children())

        try:
            for c in cidades:
                self.tree.insert("", "end", values=(c[0], c[1], c[2]))
        except Exception as e:
            print(f"Erro ao atualizar a tabela: {e}")
            messagebox.showerror("Erro", "Ocorreu um erro ao atualizar a tabela.")

    def buscarCidade(self):
        cid = Cidades()
        idcidade = self.idcidade.get()
        self.autentic["text"] = cid.selectCidade(idcidade)
        self.idcidade.delete(0, END)
        self.idcidade.insert(INSERT, cid.idcidade)
        self.cidade.delete(0, END)
        self.cidade.insert(INSERT, cid.cidade)
        self.uf.delete(0, END)
        self.uf.insert(INSERT, cid.uf)

    def inserirCidade(self):
        cid = Cidades(cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.insertCidade()
        self.autentic["text"] = result
        self.atualizarTabela()

    def alterarCidade(self):
        cid = Cidades(idcidade=self.idcidade.get(), cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.updateCidade()
        self.autentic["text"] = result
        self.atualizarTabela()

    def excluirCidade(self):
        cid = Cidades(idcidade=self.idcidade.get())
        result = cid.deleteCidade()
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
        cidade_obj = Cidades()
        cidades = cidade_obj.selectAllCidades()

        if not isinstance(cidades, list):
            messagebox.showerror("Erro", f"Erro ao buscar cidades: {cidades}")
            return

        # Preparar o arquivo PDF
        pdf_file = "relatorio_cidades.pdf"

        with PdfPages(pdf_file) as pdf:
            # Criar uma nova figura para o relatório
            fig, ax = plt.subplots(figsize=(8, 6))

            # Configuração do layout da tabela
            ax.set_axis_off()
            tbl = ax.table(
                cellText=cidades,
                colLabels=["ID", "Cidade", "UF"],
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
