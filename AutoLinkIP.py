import tkinter as tk
import webbrowser
import re

root = tk.Tk()
root.attributes("-topmost", True)
root.title("Abrir IP")
root.resizable(False, False)

# Obter dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Definir largura e altura da janela
window_width = 100  # Ajuste conforme necessário
window_height = 50   # Ajuste conforme necessário

# Calcular a posição da janela
x = screen_width - window_width
y = screen_height - window_height

# Definir a posição da janela
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

tkvar = tk.StringVar(root)

def open_links_auto(*args):
    ip = tkvar.get().strip()
    # Validar o formato do IP
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        webbrowser.open(f"http://{ip}")
        webbrowser.open(f"https://{ip}")
        webbrowser.open(f"http://{ip}:8081")
        webbrowser.open(f"https://{ip}:8081")
        tkvar.set("")

tkvar.trace_add("write", open_links_auto)

entry = tk.Entry(root, textvariable=tkvar, width=15)
entry.pack()
root.mainloop()
