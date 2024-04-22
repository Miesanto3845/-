import os
import tkinter as tk
from tkinter import ttk

def list_directories(root_dir, parent_node):
    """
    Виводить у список всі каталоги та підкаталоги для заданого каталогу.

    Args:
        root_dir (str): Шлях до початкового каталогу.
        parent_node: Батьківський вузол для дерева.

    Returns:
        None
    """
    try:
        for item in os.listdir(root_dir):
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path):
                child_node = tree.insert(parent_node, "end", text=item, open=False)
                list_directories(item_path, child_node)
    except PermissionError:
        tree.insert(parent_node, "end", text="У вас немає доступу до каталогу " + root_dir)

def on_expand(event):
    """
    Викликається при розгортанні вузла, щоб відобразити підкаталоги.

    Args:
        event: Подія розгортання вузла.

    Returns:
        None
    """
    node = event.widget.focus()
    if tree.item(node, "open"):
        return
    for child_node in tree.get_children(node):
        list_directories(tree.item(child_node, "text"), child_node)

# Створення вікна
root = tk.Tk()
root.title("Дерево каталогів")

# Створення дерева
tree = ttk.Treeview(root)
tree.pack(fill="both", expand=True)
tree.bind("<<TreeviewOpen>>", on_expand)

# Введення шляху до каталогу
root_directory = input("Введіть шлях до каталогу: ")
if os.path.isdir(root_directory):
    list_directories(root_directory, "")
else:
    tree.insert("", "end", text="Вказаний шлях не є каталогом.")

root.mainloop()
