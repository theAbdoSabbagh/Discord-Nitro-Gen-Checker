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

async def main():
  made = []
  if os.name == 'nt': # CLS clears the screen, here we check if the OS is windows and then execute the command, CLS works on windows only.
    os.system('cls')
  print("""███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ██████╗ ██████╗ ███████╗███████╗
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║     ██║   ██║██║  ██║█████╗  ███████╗
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║     ██║   ██║██║  ██║██╔══╝  ╚════██║
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╗╚██████╔╝██████╔╝███████╗███████║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                    
                             ██████╗ ███████╗███╗   ██╗                             
                            ██╔════╝ ██╔════╝████╗  ██║                             
                            ██║  ███╗█████╗  ██╔██╗ ██║                             
                            ██║   ██║██╔══╝  ██║╚██╗██║                             
                            ╚██████╔╝███████╗██║ ╚████║                             
                             ╚═════╝ ╚══════╝╚═╝  ╚═══╝                             
                                                                                    
                 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗             
                ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗            
                ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝            
                ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗            
                ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║            
                 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝            
                                                                          """)
  print(f"{Fore.MAGENTA}[!] Finding a valid Nitro code is almost impossible. This tool just creates codes and checks if they were valid or not.")
  print(f"{Fore.CYAN}Github: https://github.com/Sxvxgee{Fore.RESET}")
  print(f"""{Fore.CYAN}[1] Automatic valid code finder.
[2] Custom valid code finder.{Fore.RESET}""")
  chosen_mode = valid_int("> ")
  if int(chosen_mode) == 1:
    print(f"{Fore.MAGENTA}[!] Attempting to find a valid code...\n[!] You'll hear a beep sound once a valid code is found.{Fore.RESET}")
    thread_run_until_find()
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
  else:
    times = valid_int("How many codes would you like to generate? ")
    if times >= 10:
      max_threads = int(round(times/2)) 
      while True:
        threads_ = valid_int(f"How many threads would you like to use? [Speeds up the generation, Max {max_threads}] ")
        if threads_ > max_threads:
          error(f"Max threads is {max_threads} only.")
        else:
          break
    else:
      threads_ = 1
    if times >= 50:
      print(f'''{Fore.CYAN}[!] The terminal will most likely become messed up & hard to read.
  [!] You can know if you got any valid Nitro code by checking if a file named "valid.txt" was created.{Fore.RESET}''')
      await asyncio.sleep(3)
    print(f"{Fore.MAGENTA}[!] Generating codes...{Fore.RESET}")
    thread_do_request(threads_, times, made)
    print(f"\n\n{Fore.GREEN}[!] Finished generating codes.{Fore.RESET}")
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 



if __name__ == '__main__':
  asyncio.run(main())
  input("Press Enter to close.")
  sys.exit()
