import time
import os 
import sys

os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import ctypes
from colorama import Fore, Back, Style




# Функция для реализации анимации загрузки

def load_animation():

  

    # Строка, которая будет отображаться при загрузке приложения

    load_str = "loading..."

    ls_len = len(load_str)

  

  

    # Строка для создания вращающейся линии

    animation = "|/-\\"

    anicount = 0

      

    # используется для отслеживания

    # продолжительность анимации

    counttime = 0        

      


    i = 0                     

  

    while (counttime != 100):

          

        # скорость анимации


        time.sleep(0.075) 

                              

        # преобразование строки в список

        # как строка неизменна

        load_str_list = list(load_str) 

          

        # x-> получение кода ASCII

        x = ord(load_str_list[i])

          

        # y-> для хранения измененного кода ASCII

        y = 0                             

  


        # переключать прописные буквы в строчные и наоборот

        if x != 32 and x != 46:             

            if x>90:

                y = x-32

            else:

                y = x + 32

            load_str_list[i]= chr(y)

          

        # для хранения результирующей строки

        res =''             

        for j in range(ls_len):

            res = res + load_str_list[j]

              

        # отображение результирующей строки

        sys.stdout.write(f"\r {Fore.RED}{Style.BRIGHT}"+res + animation[anicount])

        sys.stdout.flush()

  

        # Назначение строки загрузки

        # к результирующей строке

        load_str = res

  

          

        anicount = (anicount + 1)% 4

        i =(i + 1)% ls_len

        counttime = counttime + 1

      

    # для ОС Windows

    if os.name =="nt":

        os.system("cls")

          

    # для Linux / Mac

    else:

        os.system("clear")

  
# драйверная программа

if __name__ == '__main__': 

    load_animation()

  


    sys.stdout.write(f"{Style.RESET_ALL}{Fore.YELLOW}") 


try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(f"Модуль discord_webhook Не установлен '{'py -3' if os.name == 'nt' else 'python3.8'} pip install discord_webhook'\nPress enter to exit")
    exit()
try:
    import requests
except ImportError:
    input(f"Модуль requests Не установлен Выполните '{'py -3' if os.name == 'nt' else 'python3.8'} pip install requests'\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt": # windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Mr_VINIK Studio")
        else: # unix
            print(f'\33]0;Nitro Generator and Checker - Made by Mr_VINIK Studio\a', end='', flush=True)
        self.slowType("Starting...", .40)
        time.sleep(1)
        print(f"""
{Fore.MAGENTA}{Style.BRIGHT}
╭━╮╱╭┳━━━┳━━━┳━╮╱╭╮
┃┃╰╮┃┃╭━╮┃╭━━┫┃╰╮┃┃
┃╭╮╰╯┃┃╱╰┫╰━━┫╭╮╰╯┃
┃┃╰╮┃┃┃╭━┫╭━━┫┃╰╮┃┃
┃┃╱┃┃┃╰┻━┃╰━━┫┃╱┃┃┃
╰╯╱╰━┻━━━┻━━━┻╯╱╰━╯ {Back.RESET} {Style.RESET_ALL}
                                                        """)
        print()
        time.sleep(1) 
        print()
        self.slowType(f" {Fore.GREEN}Loading successful! Please wait... ", .05)
        print()
        print()
        time.sleep(4)
        self.slowType(f" {Fore.RED} {Style.BRIGHT} {Back.GREEN} created by Mr_VINIK Studio {Style.RESET_ALL} {Back.RESET}", .02)
        time.sleep(1)
        self.slowType(f"\n{Fore.MAGENTA}Количество кодов, которые нужно сгенерировать и проверить: {Fore.GREEN}", .02, newLine = False)

        num = int(input(''))

        self.slowType(f"\n{Fore.MAGENTA}Введите ссылку веб-перехвата (вебхука) Discord\nНажми enter, чтобы игнорировать: {Fore.GREEN}", .02, newLine = False)
        url = input('')
        webhook = url if url != "" else None


        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 24
                ))
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f"{Fore.MAGENTA}Error | {url} ")

            if os.name == "nt": #windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid")
                print("")
            else: # unix
                print(f'\33]0;NGEN - {len(valid)} Valid | {invalid} Invalid\a', end='', flush=True)

        print(f"""
{Fore.YELLOW}Проверка завершена!
{Fore.YELLOW}Результаты:
{Fore.GREEN} Valid: {len(valid)}
{Fore.RED} Invalid: {invalid}
{Fore.GREEN} Valid Codes: {', '.join(valid )}""")



    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 24
                ))

                file.write(f"https://discord.gift/{code}\n")
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                
                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f"{Fore.GREEN}Valid | {nitro} ")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()
                    else:
                        break

                else:
                    print(f"{Fore.RED} {Style.BRIGHT} Invalid | {nitro} {Style.RESET_ALL}")
                    invalid += 1

        return {"valid" : valid, "invalid" : invalid}

    def quickChecker(self, nitro, notify = None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{Fore.GREEN}Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"Валидный нитро-код обнаружен!!! @everyone \n{nitro}"
                ).execute()

            return True

        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid | {nitro} {Style.RESET_ALL}", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
