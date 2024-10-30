"""
IMPORTACION DE MODULOS Y PAQUETES
"""

# Siempre es mejor importar especificamente lo que vas a usar para no hacer pesado el proyecto
from tkinter import Tk
from tkinter.ttk import Treeview

root = Tk()
root.title("GUI")

tree = Treeview(root)
tree["columns"] = ("Nombre", "Email")
tree.column("#0")
tree.column("Nombre")
tree.column("Email")

tree.heading("#0", text="id")
tree.heading("Nombre", text="Nombre")
tree.heading("Email", text="Email")

tree.grid(row=0, column=0)

root.mainloop()