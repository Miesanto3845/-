import tkinter as tk
from PIL import Image, ImageTk

class RestaurantMenuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("���������� ����")

        # ��������� ������ �����
        self.menu_items = [
            {"�����": "������ 1", "����": "50 ���", "����������": "image1.jpg"},
            {"�����": "������ 2", "����": "70 ���", "����������": "image2.jpg"},
            # ������� ���� ������ �� �����������
        ]
        
        # ���������� ������ ������
        self.current_item_index = 0

        # ³���������� ����� ������
        self.item_name_label = tk.Label(master, text="")
        self.item_name_label.pack()

        # ³���������� ���� ������
        self.item_price_label = tk.Label(master, text="")
        self.item_price_label.pack()

        # ³���������� ���������� ������
        self.item_image_label = tk.Label(master)
        self.item_image_label.pack()

        # ������ ��� ����������� �� ��������
        self.prev_button = tk.Button(master, text="�����", command=self.show_prev_item)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(master, text="���", command=self.show_next_item)
        self.next_button.pack(side=tk.RIGHT)

        # ³���������� ����� ������
        self.show_item(self.current_item_index)

    def show_item(self, index):
        item = self.menu_items[index]
        self.item_name_label.config(text="�����: " + item["�����"])
        self.item_price_label.config(text="ֳ��: " + item["����"])

        # ������������ �� ����������� ���������� ������
        image = Image.open(item["����������"])
        image = image.resize((200, 200), Image.ANTIALIAS)  # ����� ����� ��������
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