from keyboard import write
from ipaddress import ip_address
from time import sleep
import tkinter as tk
from tkinter import ttk
import threading


# Functions
def check_values():
    btn_start["state"] = tk.DISABLED

    # Switch name
    hostname_value = hostname.get().strip()
    match hostname_value:
        case "":
            hostname_value = " "
            label_hostname["fg"] = "black"
        case hostname_value if hostname_value[0].isalpha() and hostname_value.isascii():
            hostname_value = f"hostname {hostname_value}"
            label_hostname["fg"] = "black"
        case _:
            label_hostname["fg"] = "red"
            hostname_value = False

    # Switch console_password
    con_password_value = con_password.get().strip()
    match con_password_value:
        case "":
            con_password_value = " "
            label_con_password["fg"] = "black"
        case con_password_value if con_password_value.isascii():
            con_password_value = (
                f"line con 0\npassword {con_password_value}\nlogin\nexit"
            )
            label_con_password["fg"] = "black"
        case _:
            con_password_value = ""
            label_con_password["fg"] = "red"

    # Switch IP & netmask
    ip_value = ip.get().strip()
    netmask_value = netmask.get().strip()
    if (not ip_value or netmask_value) and (not netmask_value or ip_value):
        # IP
        match ip_value:
            case "":
                ip_value = " "
                label_ip["fg"] = "black"
            case ip_value:
                try:
                    ip_address(ip_value)
                except ValueError:
                    ip_value = ""
                    label_ip["fg"] = "red"
                ip_value = f"int vlan 1\nip address {ip_value}"
                label_ip["fg"] = "black"

        # Netmask
        match netmask_value:
            case "":
                netmask_value = " "
                label_netmask["fg"] = "black"
            case netmask_value:
                try:
                    ip_address(netmask_value)
                except ValueError:
                    netmask_value = ""
                    label_netmask["fg"] = "red"
                netmask_value = f"{netmask_value}\nno shutdown\nexit"
                label_netmask["fg"] = "black"
    else:
        label_ip["fg"] = "red"
        label_netmask["fg"] = "red"

    # Switch user_name & user_password
    user_name_value = user_name.get().strip()
    user_password_value = user_password.get().strip()
    if (not user_name_value or user_password_value) and (
        not user_password_value or user_name_value
    ):
        # User_name
        match user_name_value:
            case "":
                user_name_value = " "
                label_user_name["fg"] = "black"
            case user_name_value if user_name_value[
                0
            ].isalpha() and user_name_value.isascii():
                user_name_value = f"username {user_name_value} privilege 15 password"
                label_user_name["fg"] = "black"
            case _:
                user_name_value = ""
                label_user_name["fg"] = "red"

        # User_password
        match user_password_value:
            case "":
                user_password_value = " "
                label_user_password["fg"] = "black"
            case user_password_value if user_password_value[
                0
            ].isalpha() and user_password_value.isascii():
                user_password_value = f"{user_password_value}"
                label_user_password["fg"] = "black"
            case _:
                user_password_value = ""
                label_user_password["fg"] = "red"
    else:
        label_user_name["fg"] = "red"
        label_user_password["fg"] = "red"

    # Switch vty & vty_password
    vty_value = vty.get().strip()
    vty_password_value = vty_password.get().strip()
    if (not vty_value or vty_password_value) and (not vty_password_value or vty_value):
        # VTY
        match vty_value:
            case "":
                vty_value = " "
                label_vty["fg"] = "black"
            case vty_value if vty_value.isdigit() and int(vty_value) > 0:
                vty_value = f"line vty 0 {vty_value}\ntransport input telnet\npassword"
                label_vty["fg"] = "black"
            case _:
                vty_value = ""
                label_vty["fg"] = "red"

        # VTY_password
        match vty_password_value:
            case "":
                vty_password_value = " "
                label_vty_password["fg"] = "black"
            case vty_password_value if vty_password_value[
                0
            ].isalpha() and vty_password_value.isascii():
                vty_password_value = f"{vty_password_value}\nlogin\nexit"
                label_vty_password["fg"] = "black"
            case _:
                vty_password_value = ""
                label_vty_password["fg"] = "red"
    else:
        label_vty["fg"] = "red"
        label_vty_password["fg"] = "red"

    # Switch STP
    stp_value = stp.get().strip().lower()
    match stp_value:
        case "":
            stp_value = " "
            label_stp["fg"] = "black"
        case "корневой" | "root":
            stp_value = "spanning-tree vlan 1 root primary"
            label_stp["fg"] = "black"
        case "резервный" | "secondary":
            stp_value = "spanning-tree vlan 1 root secondary"
            label_stp["fg"] = "black"
        case stp_value if stp_value.isdigit() and (int(stp_value) % 4096 == 0) and (
            0 <= int(stp_value) <= 65535
        ):
            stp_value = f"spanning-tree vlan 1 priority {stp_value}"
            label_stp["fg"] = "black"
        case _:
            stp_value = ""
            label_stp["fg"] = "red"

    # Switch enable_password
    enable_password_value = enable_password.get().strip()
    match enable_password_value:
        case "":
            enable_password_value = " "
            label_enable_password["fg"] = "black"
        case enable_password_value if enable_password_value[
            0
        ].isalpha() and enable_password_value.isascii():
            enable_password_value = f"enable secret {enable_password_value}"
            label_enable_password["fg"] = "black"
        case _:
            enable_password_value = ""
            label_enable_password["fg"] = "red"

    if not (
        hostname_value
        and con_password_value
        and ip_value
        and netmask_value
        and user_name_value
        and user_password_value
        and vty_value
        and vty_password_value
        and stp_value
        and enable_password_value
    ):
        label_attention["text"] = "Невозможные параметры!"
        btn_start["state"] = tk.NORMAL
    else:
        commands = f"""
en
conf t
{hostname_value}
no ip domain-lookup
{enable_password_value}
{con_password_value}
{vty_value} {vty_password_value}
banner motd "This is a secure system Authorized Access Only!"
{user_name_value} {user_password_value}
service password-encryption
{ip_value} {netmask_value}
{stp_value}
end
wr
"""
        label_attention["text"] = "Установите курсор на строку ввода консоли!!!"
        label_attention["fg"] = "red"
        thread = threading.Thread(target=start_write, args=(commands,))
        thread.start()


def start_write(commands):
    for i in range(-5, 1):
        btn_start["text"] = f"{-i}"
        sleep(1)

    write(commands)
    label_attention["text"] = ""
    label_attention["fg"] = "black"
    btn_start["text"] = "Начать"
    btn_start["state"] = tk.NORMAL


# Window settings
win = tk.Tk()
win.title("Базовая настройка коммутатора Cisco")
master_frame = tk.Frame(master=win, borderwidth=3, relief=tk.GROOVE)
master_frame.pack(expand=1)

h = 635  # Ширина
w = 250  # Высота
win.geometry(f"{h}x{w}")
win.minsize(h, w)
# win.resizable(False, False)
win.columnconfigure(0, minsize=100)
win.columnconfigure(1, minsize=50)
win.columnconfigure(2, minsize=100)
win.columnconfigure(3, minsize=50)

# Labels
label_attention = tk.Label(master_frame, text="", font=("Arial", 12), padx=10, pady=5)
label_hostname = tk.Label(
    master_frame,
    text="Имя коммутатора: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_ip = tk.Label(
    master_frame,
    text="IP на vlan 1: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_user_name = tk.Label(
    master_frame,
    text="Имя пользователя: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_vty = tk.Label(
    master_frame,
    text="Количество vty: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_stp = tk.Label(
    master_frame,
    text="Приоритет в STP: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)

label_con_password = tk.Label(
    master_frame,
    text="Пароль для консоли: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_netmask = tk.Label(
    master_frame,
    text="Маска сети на vlan 1: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_user_password = tk.Label(
    master_frame,
    text="Пароль пользователя: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_vty_password = tk.Label(
    master_frame,
    text="Пароль для vty: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_enable_password = tk.Label(
    master_frame,
    text="Пароль для enable режима: ",
    font=("Arial", 10),
    justify=tk.LEFT,
    padx=10,
    pady=5,
    anchor="w",
)
label_rec = tk.Label(
    master_frame,
    text="Оставьте строку пустой, чтобы не настраивать это",
    font=("Arial", 8),
    padx=10,
    pady=5,
)


label_attention.grid(row=0, column=0, columnspan=4, stick="we")
label_hostname.grid(row=1, column=0, stick="w")
label_ip.grid(row=2, column=0, stick="w")
label_user_name.grid(row=3, column=0, stick="w")
label_vty.grid(row=4, column=0, stick="w")
label_stp.grid(row=5, column=0, stick="w")

label_con_password.grid(row=1, column=2, stick="w")
label_netmask.grid(row=2, column=2, stick="w")
label_user_password.grid(row=3, column=2, stick="w")
label_vty_password.grid(row=4, column=2, stick="w")
label_enable_password.grid(row=5, column=2, stick="w")
label_rec.grid(row=7, column=0, columnspan=4, stick="we")

# Entry
hostname = tk.Entry(master_frame)
hostname.insert(0, "SW1")
ip = tk.Entry(master_frame)
ip.insert(0, "192.168.1.1")
user_name = tk.Entry(master_frame)
user_name.insert(0, "admin")
vty = tk.Entry(master_frame)
vty.insert(0, "15")

con_password = tk.Entry(master_frame)
con_password.insert(0, "P@ssw0rd")
netmask = tk.Entry(master_frame)
netmask.insert(0, "255.255.255.0")
user_password = tk.Entry(master_frame)
user_password.insert(0, "P@ssw0rd")
vty_password = tk.Entry(master_frame)
vty_password.insert(0, "P@ssw0rd")
enable_password = tk.Entry(master_frame)
enable_password.insert(0, "P@ssw0rd")


hostname.grid(row=1, column=1, stick="we")
ip.grid(row=2, column=1, stick="we")
user_name.grid(row=3, column=1, stick="we")
vty.grid(row=4, column=1, stick="we")

con_password.grid(row=1, column=3, stick="we")
netmask.grid(row=2, column=3, stick="we")
user_password.grid(row=3, column=3, stick="we")
vty_password.grid(row=4, column=3, stick="we")
enable_password.grid(row=5, column=3, stick="we")

# Combobox
stp = ttk.Combobox(master_frame, values=("Корневой", "Резервный"))

stp.grid(row=5, column=1, stick="we")

# Button
btn_start = tk.Button(
    master_frame,
    text="Начать",
    command=check_values,
    activebackground="gray",
    padx=5,
    pady=5,
)
btn_start.grid(row=6, column=1, columnspan=2, stick="we")

if __name__ == "__main__":
    win.mainloop()
