import tkinter as tk
from PIL import Image, ImageTk

class RestaurantMenuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ресторанне Меню")

        # Створення списку страв
        self.menu_items = [
            {"назва": "Страва 1", "ціна": "50 грн", "зображення": "image1.jpg"},
            {"назва": "Страва 2", "ціна": "70 грн", "зображення": "image2.jpg"},
            # Додайте інші страви за необхідності
        ]
        
        # Початковий індекс страви
        self.current_item_index = 0

        # Відображення назви страви
        self.item_name_label = tk.Label(master, text="")
        self.item_name_label.pack()

        # Відображення ціни страви
        self.item_price_label = tk.Label(master, text="")
        self.item_price_label.pack()

        # Відображення зображення страви
        self.item_image_label = tk.Label(master)
        self.item_image_label.pack()

        # Кнопки для перемикання між стравами
        self.prev_button = tk.Button(master, text="Назад", command=self.show_prev_item)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(master, text="Далі", command=self.show_next_item)
        self.next_button.pack(side=tk.RIGHT)

        # Відображення першої страви
        self.show_item(self.current_item_index)

    def show_item(self, index):
        item = self.menu_items[index]
        self.item_name_label.config(text="Назва: " + item["назва"])
        self.item_price_label.config(text="Ціна: " + item["ціна"])

        # Завантаження та відображення зображення страви
        image = Image.open(item["зображення"])
        image = image.resize((200, 200), Image.ANTIALIAS)  # Розмір можна змінювати
        photo = ImageTk.PhotoImage(image)
        self.item_image_label.config(image=photo)
        self.item_image_label.image = photo

    def show_prev_item(self):
        self.current_item_index -= 1
        if self.current_item_index < 0:
            self.current_item_index = len(self.menu_items) - 1
        self.show_item(self.current_item_index)

    def show_next_item(self):
        self.current_item_index += 1
        if self.current_item_index >= len(self.menu_items):
            self.current_item_index = 0
        self.show_item(self.current_item_index)

def main():
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()

if name == "__main__":
    main()