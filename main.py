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
