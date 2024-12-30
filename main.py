# Proxy Check
# Coded By Tetra

import requests
from colorama import Fore, init
from pyfiglet import figlet_format
from time import sleep
from fake_useragent import UserAgent


def proxy_check(proxy_file, fresh_proxy_name):
    init(autoreset=True)
    ua = UserAgent()
    url = "https://youtube.com"

    headers = {
        "User-Agent": ua.random
    }

    try:
        with open(proxy_file, "r", encoding="utf-8") as file:
            reading = file.readlines()

        with open(fresh_proxy_name, "w", encoding="utf-8") as output_file:
            output_file.write("FRESH PROXY LIST\n\n")

            for proxy in reading:
                proxy = proxy.strip()
                proxies = {
                    "http": proxy,
                    "https": proxy
                }

                try:
                    response = requests.get(url, headers=headers, proxies=proxies, timeout=3)
                    if response.status_code == 200:
                        print(f"{Fore.GREEN} Live Proxy: {proxy}")
                        output_file.write(f"{proxy}\n")
                    else:
                        print(f"{Fore.RED} Dead Proxy: {proxy}")
                except requests.exceptions.RequestException:
                    print(f"{Fore.RED} Connection failed for proxy: {proxy}")
    except FileNotFoundError:
        print(f"{Fore.MAGENTA} Specified file path not found.")
    except Exception as e:
        print(f"{Fore.YELLOW} Unexpected error: {e}")
    finally:
        print(f"{Fore.MAGENTA} Scanning complete. Live proxies saved to {fresh_proxy_name}.")


def main():
    init(autoreset=True)
    logo = figlet_format("PROXIES")
    print(Fore.RED + logo)

    proxy_file = input(f"{Fore.BLUE}\nEnter the path to the proxy file: ")
    fresh_proxy_name = input(f"{Fore.YELLOW}\nEnter the name for the output file: ")

    proxy_check(proxy_file, fresh_proxy_name)


if __name__ == "__main__":
    main()
