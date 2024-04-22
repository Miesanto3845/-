import tkinter as tk
from PIL import Image, ImageTk

class RestaurantMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Меню ресторану")

        self.menu_items = [
            {"name": "Піца", "price": "$10", "image": "pizza.jpg"},
            {"name": "Салат", "price": "$8", "image": "salad.jpg"},
            {"name": "Стейк", "price": "$15", "image": "steak.jpg"}
        ]
        self.current_item_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.item_name_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.item_name_label.pack(pady=10)

        self.item_price_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.item_price_label.pack(pady=5)

        self.item_image_label = tk.Label(self.root)
        self.item_image_label.pack(pady=10)

        self.prev_button = tk.Button(self.root, text="Назад", command=self.show_previous_item)
        self.prev_button.pack(side="left", padx=10)

        self.next_button = tk.Button(self.root, text="Далі", command=self.show_next_item)
        self.next_button.pack(side="right", padx=10)

        self.show_item(self.current_item_index)

    def show_item(self, index):
        item = self.menu_items[index]
        self.item_name_label.config(text=item["name"])
        self.item_price_label.config(text="Ціна: " + item["price"])

        image_path = item["image"]
        image = Image.open(image_path)
        image = image.resize((200, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.item_image_label.config(image=photo)
        self.item_image_label.image = photo

    def show_previous_item(self):
        self.current_item_index = (self.current_item_index - 1) % len(self.menu_items)
        self.show_item(self.current_item_index)

    def show_next_item(self):
        self.current_item_index = (self.current_item_index + 1) % len(self.menu_items)
        self.show_item(self.current_item_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()
