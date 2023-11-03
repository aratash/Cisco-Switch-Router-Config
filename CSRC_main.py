from keyboard import write
from ipaddress import ip_address
from time import sleep
from tkinter import DISABLED, NORMAL
import threading
import CSRC_gui as gui


# Functions
def check_values(*args):
    window.btn_start.config(state=DISABLED)

    # Switch name
    hostname_value = window.hostname.get().strip()
    match hostname_value:
        case "":
            hostname_value = " "
            window.label_hostname.config(fg="black")
        case hostname_value if hostname_value[0].isalpha() and hostname_value.isascii():
            hostname_value = f"hostname {hostname_value}"
            window.label_hostname.config(fg="black")
        case _:
            window.label_hostname.config(fg="red")
            hostname_value = False

    # Switch console_password
    con_password_value = window.con_password.get().strip()
    match con_password_value:
        case "":
            con_password_value = " "
            window.label_con_password.config(fg="black")
        case con_password_value if con_password_value.isascii():
            con_password_value = (
                f"line con 0\npassword {con_password_value}\nlogin\nexit"
            )
            window.label_con_password.config(fg="black")
        case _:
            con_password_value = ""
            window.label_con_password.config(fg="red")

    # Switch IP & netmask
    ip_value = window.ip.get().strip()
    netmask_value = window.netmask.get().strip()
    if (not ip_value or netmask_value) and (not netmask_value or ip_value):
        # IP
        match ip_value:
            case "":
                ip_value = " "
                window.label_ip.config(fg="black")
            case ip_value:
                try:
                    ip_address(ip_value)
                except ValueError:
                    ip_value = ""
                    window.label_ip.config(fg="red")
                ip_value = f"int vlan 1\nip address {ip_value}"
                window.label_ip.config(fg="black")

        # Netmask
        match netmask_value:
            case "":
                netmask_value = " "
                window.label_netmask.config(fg="black")
            case netmask_value:
                try:
                    ip_address(netmask_value)
                except ValueError:
                    netmask_value = ""
                    window.label_netmask.config(fg="red")
                netmask_value = f"{netmask_value}\nno shutdown\nexit"
                window.label_netmask.config(fg="black")
    else:
        window.label_ip.config(fg="red")
        window.label_netmask.config(fg="red")

    # Switch user_name & user_password
    user_name_value = window.user_name.get().strip()
    user_password_value = window.user_password.get().strip()
    if (not user_name_value or user_password_value) and (
        not user_password_value or user_name_value
    ):
        # User_name
        match user_name_value:
            case "":
                user_name_value = " "
                window.label_user_name.config(fg="black")
            case user_name_value if user_name_value[
                0
            ].isalpha() and user_name_value.isascii():
                user_name_value = f"username {user_name_value} privilege 15 password"
                window.label_user_name.config(fg="black")
            case _:
                user_name_value = ""
                window.label_user_name.config(fg="red")

        # User_password
        match user_password_value:
            case "":
                user_password_value = " "
                window.label_user_password.config(fg="black")
            case user_password_value if user_password_value[
                0
            ].isalpha() and user_password_value.isascii():
                user_password_value = f"{user_password_value}"
                window.label_user_password.config(fg="black")
            case _:
                user_password_value = ""
                window.label_user_password.config(fg="red")
    else:
        window.label_user_name.config(fg="red")
        window.label_user_password.config(fg="red")

    # Switch vty & vty_password
    vty_value = window.vty.get().strip()
    vty_password_value = window.vty_password.get().strip()
    if (not vty_value or vty_password_value) and (not vty_password_value or vty_value):
        # VTY
        match vty_value:
            case "":
                vty_value = " "
                window.label_vty.config(fg="black")
            case vty_value if vty_value.isdigit() and int(vty_value) > 0:
                vty_value = f"line vty 0 {vty_value}\ntransport input telnet\npassword"
                window.label_vty.config(fg="black")
            case _:
                vty_value = ""
                window.label_vty.config(fg="red")

        # VTY_password
        match vty_password_value:
            case "":
                vty_password_value = " "
                window.label_vty_password.config(fg="black")
            case vty_password_value if vty_password_value[
                0
            ].isalpha() and vty_password_value.isascii():
                vty_password_value = f"{vty_password_value}\nlogin\nexit"
                window.label_vty_password.config(fg="black")
            case _:
                vty_password_value = ""
                window.label_vty_password.config(fg="red")
    else:
        window.label_vty.config(fg="red")
        window.label_vty_password.config(fg="red")

    # Switch STP
    stp_value = window.stp.get().strip().lower()
    match stp_value:
        case "":
            stp_value = " "
            window.label_stp.config(fg="black")
        case "корневой" | "root":
            stp_value = "spanning-tree vlan 1 root primary"
            window.label_stp.config(fg="black")
        case "резервный" | "secondary":
            stp_value = "spanning-tree vlan 1 root secondary"
            window.label_stp.config(fg="black")
        case stp_value if stp_value.isdigit() and (int(stp_value) % 4096 == 0) and (
            0 <= int(stp_value) <= 65535
        ):
            stp_value = f"spanning-tree vlan 1 priority {stp_value}"
            window.label_stp.config(fg="black")
        case _:
            stp_value = ""
            window.label_stp.config(fg="red")

    # Switch enable_password
    enable_password_value = window.enable_password.get().strip()
    match enable_password_value:
        case "":
            enable_password_value = " "
            window.label_enable_password.config(fg="black")
        case enable_password_value if enable_password_value[
            0
        ].isalpha() and enable_password_value.isascii():
            enable_password_value = f"enable secret {enable_password_value}"
            window.label_enable_password.config(fg="black")
        case _:
            enable_password_value = ""
            window.label_enable_password.config(fg="red")

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
        window.label_attention["text"] = "Невозможные параметры!"
        window.btn_start.config(state=NORMAL)
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
        window.label_attention["text"] = "Установите курсор на строку ввода консоли!!!"
        window.label_attention.config(fg="red")
        thread = threading.Thread(target=start_write, args=(commands,))
        thread.start()


def start_write(commands):
    for i in range(-5, 1):
        window.btn_start["text"] = f"{-i}"
        sleep(1)

    write(commands)
    window.label_attention["text"] = ""
    window.label_attention.config(fg="black")
    window.btn_start["text"] = "Начать"
    window.btn_start.config(state=NORMAL)


if __name__ == "__main__":
    window = gui.App()
    window.btn_start.bind("<Button-1>", check_values)
    window.win.mainloop()
