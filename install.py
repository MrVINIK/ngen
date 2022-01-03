import time
import os
import sys
from colorama import Fore, Back, Style

os.system("clear")

print(f"{Fore.YELLOW}Подключение...")

def InternetConnectionCheck():
    try:
        requests.get("https://google.com", timeout=4)
    except:
        print(f"{Fore.RED}Ваше устройство не подключено к интернету. Проверьте соединение с интернетом и повторите попытку{Fore.RESET}")
        sys.exit(1)
print() 
time.sleep(1)
print(f"""
{Fore.MAGENTA}{Style.BRIGHT} 
╭╮╱╭┳━━━┳━━━┳━━━┳━━━━┳━━━┳━━━╮
┃┃╱┃┃╭━╮┣╮╭╮┃╭━╮┃╭╮╭╮┃╭━━┫╭━╮┃
┃┃╱┃┃╰━╯┃┃┃┃┃┃╱┃┣╯┃┃╰┫╰━━┫╰━╯┃
┃┃╱┃┃╭━━╯┃┃┃┃╰━╯┃╱┃┃╱┃╭━━┫╭╮╭╯
┃╰━╯┃┃╱╱╭╯╰╯┃╭━╮┃╱┃┃╱┃╰━━┫┃┃╰╮
╰━━━┻╯╱╱╰━━━┻╯╱╰╯╱╰╯╱╰━━━┻╯╰━╯{Style.RESET_ALL}
""")

print(f"{Fore.YELLOW}выполняю проверку пакетов на наличие обновлений... Если обновления будут найдены, они будут автоматически обновлены.{Fore.RESET}")

time.sleep(1)
print() 
time.sleep(1)

os.system(" apt update -y")
os.system("apt upgrade -y")
os.system("apt full-upgrade -y")
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pip install --upgrade pip")

time.sleep(2)
os.system("clear")
time.sleep(1)
print(f"{Fore.GREEN}Обновление вашего терминала завершено! Начинаю установку важных пакетов...{Fore.RESET}")
os.system("pip install requests && pip install discord_webhook && pip install colored && pip install colorama")

time.sleep(3)
os.system("clear") 
print(f"{Fore.GREEN}Установка завершена! Запускаю программу...")

time.sleep(4)
os.system("python3 main.py") 