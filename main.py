import asyncio, requests, string, random, os, threading, sys, winsound
from colorama import init, Fore
init()

def error(text):
  print(f"{Fore.RED}[!] {text}{Fore.RESET}")

def valid(code):
  print(f"{Fore.GREEN}[!] Found a valid code: {code} | discord.gift/{code} {Fore.RESET}")
  with open("valid_codes.txt", "a") as f:
    f.write(f"discord.gg/{code} | {code}\n")

def invalid(code):
  print(f"{Fore.RED}[!] Found an invalid code: {code} | discord.gift/{code} {Fore.RESET}")
  with open("invalid_codes.txt", "a") as f:
    f.write(f"discord.gg/{code} | {code}\n")

def valid_int(text):
  while True:
    to_generate = input(text)
    try:
      int(to_generate)
    except:
      error("Numbers are accepted only.")
    else:
      return int(to_generate)

def do_request(the_list, times):
  for i in range(int(times)):
    code = create_codes(the_list)
    the_list.append(code)
    response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if response.status_code == 200:
      valid(code)
    else:
      invalid(code)

threads = []

def thread_do_request(threads_times, times, the_list):
  # I. Am. Speed.
  better_times = int(round(times/threads_times))
  for i in range(int(threads_times)):
    t = threading.Thread(target = do_request, args = [the_list,better_times])
    t.daemon = True
    threads.append(t)
  for i in range(int(threads_times)):
    threads[i].start()
  for i in range(int(threads_times)):
    threads[i].join()

def run_until_find():
  the_list = []
  while True:
    try:
      code = create_codes(the_list)
      the_list.append(code)
      response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
      if response.status_code == 200:
        valid(code)
        return
    except:
      break
