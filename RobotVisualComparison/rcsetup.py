import os
import re
import subprocess
import winreg
import time
import colorama
from colorama import Fore

def rcsetup():
    python_path = os.environ.get("Path", "Machine")
    python_path = [path for path in python_path.split(";") if "Python" in path][0]
    python_path = re.sub(r"\\Scripts\\?", "", python_path)

    site_packages_path = os.path.join(python_path, "Lib", "site-packages", "RobotVisualComparison")
    if not os.path.exists(site_packages_path):
        print("Error: RobotVisualComparison library not installed properly")

    magick_path = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI"

    exe_path = os.path.join(site_packages_path, "Magick.exe")
    if os.path.exists(exe_path) and not os.path.exists(os.path.join(magick_path,"magick.exe")):
        subprocess.run([exe_path, "/silent"], shell=True)
        print("Configuring............", end="", flush=True)
        for i in range(20):
            print(".", end="", flush=True)
            time.sleep(0.8)
        print(Fore.WHITE+" | "+Fore.GREEN + 'Done !' + Fore.WHITE+" |")
    elif not os.path.exists(os.path.join(magick_path,"magick.exe")):
        print(f"Error: {exe_path} not found.")
        
    vscode_path = rf"c:\users\{os.environ.get('USERNAME')}\AppData\Local\Programs\Microsoft VS Code\bin"
    
    if vscode_path not in os.environ.get("Path","User"):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, vscode_path + ";" + os.environ.get("Path", ""))
        winreg.CloseKey(key)
        print("\nSetting VS code Path...",end="", flush=True)
        for i in range(20):
            print(".", end="", flush=True)
            time.sleep(0.8)
        print(Fore.WHITE+" | "+Fore.GREEN + 'Done !' + Fore.WHITE+" |")
    else:
        print("Info: VSCode path already exists. ")
    
    if magick_path not in os.environ.get("Path", "User"):
        code_path = "" if vscode_path in os.environ.get("Path","User") else vscode_path+";"
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, magick_path + ";" + code_path + os.environ.get("Path", ""))
        winreg.CloseKey(key)
        print("\nSetting Comparison Path",end="", flush=True)
        for i in range(20):
            print(".", end="", flush=True)
            time.sleep(0.8)
        print(Fore.WHITE+" | "+Fore.GREEN + 'Done !' + Fore.WHITE+" |")
    else:
        print("Info: Comparison software path already exists. ")
