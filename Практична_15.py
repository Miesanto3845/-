import tkinter as tk
from tkinter import ttk

class CountryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("������ ���� �� �������")

        self.countries = []
        self.filtered_countries = []

        self.filter_var = tk.StringVar()
        self.filter_var.trace("w", self.filter_countries)

        self.create_widgets()

    def create_widgets(self):
        # �������� ������ ��� ����������
        filter_entry = ttk.Entry(self.root, textvariable=self.filter_var)
        filter_entry.pack(pady=10)

        # ��������� ListView
        self.country_list = ttk.Treeview(self.root, columns=("Country", "Capital"), show="headings")
        self.country_list.heading("Country", text="�����")
        self.country_list.heading("Capital", text="�������")
        self.country_list.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # ������ ��� ��������� �����
        add_button = ttk.Button(self.root, text="������ �����", command=self.add_country)
        add_button.pack(pady=5)

        # ������ ��� ��������� �����
        remove_button = ttk.Button(self.root, text="�������� �����", command=self.remove_country)
        remove_button.pack(pady=5)

        # ��������� ������ �������� ����
        self.add_example_countries()

    def add_example_countries(self):
        example_countries = [("������", "���"), ("������", "�������"), ("ͳ�������", "�����")]
        for country, capital in example_countries:
            self.add_country_to_list(country, capital)

    def add_country(self):
        country = tk.simpledialog.askstring("������ �����", "������ ����� �����:")
        capital = tk.simpledialog.askstring("������ �����", f"������ ������� {country}:")
        if country and capital:
            self.add_country_to_list(country, capital)

    def add_country_to_list(self, country, capital):
        self.countries.append((country, capital))
        self.countries.sort(key=lambda x: x[0])  # ���������� �� ������ �����
        self.update_listbox()

    def remove_country(self):
        selected_item = self.country_list.selection()
        if selected_item:
            country = self.country_list.item(selected_item, "values")[0]
            for c in self.countries:
                if c[0] == country:
                    self.countries.remove(c)
                    break
            self.update_listbox()

    def filter_countries(self, *args):
        filter_text = self.filter_var.get()
        self.filtered_countries = [c for c in self.countries if filter_text.lower() in c[0].lower() or filter_text.lower() in c[1].lower()]
        self.update_listbox()

    def update_listbox(self):
        self.country_list.delete(*self.country_list.get_children())
        for country, capital in self.filtered_countries:
            self.country_list.insert("", "end", values=(country, capital))

if __name__ == "__main__":
    root = tk.Tk()
    app = CountryApp(root)
    root.mainloop()