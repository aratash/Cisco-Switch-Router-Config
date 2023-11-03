import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.win = tk.Tk()
        self.window()
        self.declareWidget()
        self.placeWidget()

    # Window settings
    def window(self):
        self.win.title("CSRC")
        self.master_frame = tk.Frame(master=self.win, borderwidth=3, relief=tk.GROOVE)
        self.master_frame.pack(expand=1)
        self.h = 635  # Ширина
        self.w = 250  # Высота
        self.win.geometry(f"{self.h}x{self.w}")
        self.win.minsize(self.h, self.w)
        self.win.columnconfigure(0, minsize=100)
        self.win.columnconfigure(1, minsize=50)
        self.win.columnconfigure(2, minsize=100)
        self.win.columnconfigure(3, minsize=50)

    def declareWidget(self):
        # Labels
        self.label_attention = tk.Label(
            self.master_frame, text="", font=("Arial", 12), padx=10, pady=5
        )
        self.label_hostname = tk.Label(
            self.master_frame,
            text="Имя коммутатора: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_ip = tk.Label(
            self.master_frame,
            text="IP на vlan 1: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_user_name = tk.Label(
            self.master_frame,
            text="Имя пользователя: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_vty = tk.Label(
            self.master_frame,
            text="Количество vty: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_stp = tk.Label(
            self.master_frame,
            text="Приоритет в STP: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )

        self.label_con_password = tk.Label(
            self.master_frame,
            text="Пароль для консоли: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_netmask = tk.Label(
            self.master_frame,
            text="Маска сети на vlan 1: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_user_password = tk.Label(
            self.master_frame,
            text="Пароль пользователя: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_vty_password = tk.Label(
            self.master_frame,
            text="Пароль для vty: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_enable_password = tk.Label(
            self.master_frame,
            text="Пароль для enable режима: ",
            font=("Arial", 10),
            justify=tk.LEFT,
            padx=10,
            pady=5,
            anchor="w",
        )
        self.label_rec = tk.Label(
            self.master_frame,
            text="Оставьте строку пустой, чтобы не настраивать это",
            font=("Arial", 8),
            padx=10,
            pady=5,
        )

        # Entry
        self.hostname = tk.Entry(self.master_frame)
        self.hostname.insert(0, "SW1")
        self.ip = tk.Entry(self.master_frame)
        self.ip.insert(0, "192.168.1.1")
        self.user_name = tk.Entry(self.master_frame)
        self.user_name.insert(0, "admin")
        self.vty = tk.Entry(self.master_frame)
        self.vty.insert(0, "15")

        self.con_password = tk.Entry(self.master_frame)
        self.con_password.insert(0, "P@ssw0rd")
        self.netmask = tk.Entry(self.master_frame)
        self.netmask.insert(0, "255.255.255.0")
        self.user_password = tk.Entry(self.master_frame)
        self.user_password.insert(0, "P@ssw0rd")
        self.vty_password = tk.Entry(self.master_frame)
        self.vty_password.insert(0, "P@ssw0rd")
        self.enable_password = tk.Entry(self.master_frame)
        self.enable_password.insert(0, "P@ssw0rd")

        # Combobox
        self.stp = ttk.Combobox(self.master_frame, values=("Корневой", "Резервный"))

        # Buttons
        self.btn_start = tk.Button(
            self.master_frame,
            text="Начать",
            activebackground="gray",
            padx=5,
            pady=5,
        )
        self.btn_start.grid(row=6, column=1, columnspan=2, stick="we")

    def placeWidget(self):
        # Labels
        self.label_attention.grid(row=0, column=0, columnspan=4, stick="we")
        self.label_hostname.grid(row=1, column=0, stick="w")
        self.label_ip.grid(row=2, column=0, stick="w")
        self.label_user_name.grid(row=3, column=0, stick="w")
        self.label_vty.grid(row=4, column=0, stick="w")
        self.label_stp.grid(row=5, column=0, stick="w")

        self.label_con_password.grid(row=1, column=2, stick="w")
        self.label_netmask.grid(row=2, column=2, stick="w")
        self.label_user_password.grid(row=3, column=2, stick="w")
        self.label_vty_password.grid(row=4, column=2, stick="w")
        self.label_enable_password.grid(row=5, column=2, stick="w")
        self.label_rec.grid(row=7, column=0, columnspan=4, stick="we")

        # Entry
        self.hostname.grid(row=1, column=1, stick="we")
        self.ip.grid(row=2, column=1, stick="we")
        self.user_name.grid(row=3, column=1, stick="we")
        self.vty.grid(row=4, column=1, stick="we")

        self.con_password.grid(row=1, column=3, stick="we")
        self.netmask.grid(row=2, column=3, stick="we")
        self.user_password.grid(row=3, column=3, stick="we")
        self.vty_password.grid(row=4, column=3, stick="we")
        self.enable_password.grid(row=5, column=3, stick="we")

        # Combobox
        self.stp.grid(row=5, column=1, stick="we")

        # Buttons
        self.btn_start.grid(row=6, column=1, columnspan=2, stick="we")


if __name__ == "__main__":
    window = App()
    window.win.mainloop()
