import tkinter as tk
from tkinter import messagebox

class SpottedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotted App")

        # Rótulo
        self.label = tk.Label(root, text="Digite sua mensagem:")
        self.label.pack(pady=10)

        # Caixa de entrada
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botão de envio
        self.button = tk.Button(root, text="Enviar", command=self.enviar_mensagem)
        self.button.pack()

    def enviar_mensagem(self):
        mensagem = self.entry.get()
        if mensagem:
            messagebox.showinfo("Mensagem Enviada", f"Mensagem: {mensagem}")
        else:
            messagebox.showwarning("Erro", "Digite uma mensagem antes de enviar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpottedApp(root)
    root.mainloop()
