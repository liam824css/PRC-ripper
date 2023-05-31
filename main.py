import os
import sys
import time
import shutil

developer = "Liam824css (Github)"
file_path = "C:\\Windows\\Downloaded Program Files\\xkv3root"
github = "https://github.com/liam824css (Repo)"

title = '\033[31m' +  f""" ███████████  ███████████     █████████             ███████████    ███                                        
░░███░░░░░███░░███░░░░░███   ███░░░░░███           ░░███░░░░░███  ░░░                                         
 ░███    ░███ ░███    ░███  ███     ░░░             ░███    ░███  ████  ████████  ████████   ██████  ████████ 
 ░██████████  ░██████████  ░███          ██████████ ░██████████  ░░███ ░░███░░███░░███░░███ ███░░███░░███░░███
 ░███░░░░░░   ░███░░░░░███ ░███         ░░░░░░░░░░  ░███░░░░░███  ░███  ░███ ░███ ░███ ░███░███████  ░███ ░░░ 
 ░███         ░███    ░███ ░░███     ███            ░███    ░███  ░███  ░███ ░███ ░███ ░███░███░░░   ░███     
 █████        █████   █████ ░░█████████             █████   █████ █████ ░███████  ░███████ ░░██████  █████    
░░░░░        ░░░░░   ░░░░░   ░░░░░░░░░             ░░░░░   ░░░░░ ░░░░░  ░███░░░   ░███░░░   ░░░░░░  ░░░░░     
                                                                        ░███      ░███                        
                                                                        █████     █████                       
                                                                       ░░░░░     ░░░░░                        
                {developer} // {github}"""

def logo():
    print(title)
    print("[+] PRC Ripper V 1.0.0.B Started")
    password = input("[@] Enter PRC Password : ")
    #PRC Password is 0x000002076BF78FE0
    if password == "0x000002076BF78FE0":
        time.sleep(0.8)
        print("[+] Password Checked\n PRC-Ripper will start in 3 seconds\n")
        time.sleep(0.5)
        os.system("cd C:\\Windows\\Downloaded Program Files\\")
        os.system("takeown /f xkv3root /r")
        os.system("cd xkv3root")
        os.system("icacls prcs*.exe /deny everyone:f")
        print("\n\n")
        print(os.system('tasklist'))
        os.system('taskkill /f /im svcxkcore.exe')
        os.system('icalcs prcs*.exe /grant everyone:f')
        shutil.rmtree(file_path)
        print("finished!")
        exit()

logo()