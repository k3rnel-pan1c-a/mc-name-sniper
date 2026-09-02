from os import system
import json
from colorama import Fore
import requests
from requests_futures.sessions import FuturesSession
from time import time, sleep
import asyncio
import aiohttp
from datetime import datetime,timedelta
import logging
from itertools import islice
from sys import exit
import sys
from discord_webhooks import DiscordWebhooks
logging.basicConfig(level=logging.INFO, format='%(message)s')
# notification = win10toast.ToastNotifier()
session = FuturesSession()

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
TearsInfo = f'{LIGHT_BLUE}[INFO]{WHITE} '
TearsInput = f'{LIGHT_BLUE}[INPUT]{WHITE} '
name_task = f'{LIGHT_BLUE}[OUTPUT]{WHITE} '
Emails = []
Passwords = []
times = []
version = "1.0"

if sys.platform == "linux" or sys.platform == "linux2":
    system('clear')
elif sys.platform == "darwin":
    system('clear')
elif sys.platform == "win32":
    system('cls')

print(f"""{PURPLE}████████╗███████╗ █████╗ ██████╗ ███████╗    {LIGHT_GRAY}███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
{PURPLE}╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝    {LIGHT_GRAY}██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
{PURPLE}   ██║   █████╗  ███████║██████╔╝███████╗    {LIGHT_GRAY}███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
{PURPLE}   ██║   ██╔══╝  ██╔══██║██╔══██╗╚════██║    {LIGHT_GRAY}╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
{PURPLE}   ██║   ███████╗██║  ██║██║  ██║███████║    {LIGHT_GRAY}███████║██║ ╚████║██║██║     ███████╗██║  ██║
{PURPLE}   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    {LIGHT_GRAY}╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
{WHITE}                                                                            by Anas{PURPLE}#6812

""")


# async def snipe(request):
#     payload = request.json()
#


try:

    file = open('accounts.txt', 'r+')
except:
    print(f"{name_task}Sorry you dont have an accounts file, please create one ")
    exit()
Lines = file.readlines()
file.close()
print(f'{TearsInfo}Loaded {len(Lines)} account(s)!')
print(f'{TearsInfo}Using a custom discord webhook')
if len(sys.argv) > 1:
    name_requested = sys.argv[1]
    try:

        num_accounts = sys.argv[2]

    except :
        num_accounts = ""
    try:
        custom_delay = sys.argv[3]
    except :
        custom_delay = ""

else:

    name_requested = input("\n" + TearsInput + "Name you wanna snipe : ")
    num_accounts = input(TearsInput + "Accounts IN (leave empty for all) : ")
    custom_delay = input(TearsInput + "Do u wanna use a custom delay ? (leave empty to use default delay) : ")
# mc_bearers = input(f"{TearsInput}Do u wanna use a custom bearer ? (y/n) : ")

webhook = DiscordWebhooks("https://discordapp.com/api/webhooks/752541141559279617/PhyLI8V2GpFcp0arv6G1xAkejn7HbmQ6kzQzu9eGx481UIG-Isj5NSqW4qcMDTGl1CkH")

# if mc_bearers == "n":
#     pass
# else:
#     if num_accounts == "":
#         for i in range
#
#     for i in range(int(num_accounts)):

name_task = f'{LIGHT_CYAN}[{name_requested}]{WHITE} '
print(f'\n{TearsInfo}Started task to snipe {name_requested}...')
sleep(0.5)
if num_accounts == "":
    pass
else:
    Lines = islice(Lines, int(num_accounts))
for line in Lines:
    EmailThrowaway = line.split(':')[0]
    EmailThrowaway = EmailThrowaway.replace('\n', '')
    Emails.append(EmailThrowaway)
    PasswordThrowaway = line.split(':')[1]
    PasswordThrowaway = PasswordThrowaway.replace('\n', '')
    Passwords.append(PasswordThrowaway)
droptimebefore = int(time() - 3456000)
url_id = "http://api.mojang.com/users/profiles/minecraft/" + name_requested + "?at=0" + str(droptimebefore)

req = session.get(url_id)
y = json.loads(req.result().content)
if req.result().status_code == 204:
    print(f"{name_task}Name is already available")
    exit()
elif name_requested == y["name"]:
    print()
    print(f"{name_task}Bummer! Name is not available")
    exit()

else:
    oldOwnerID = y["id"]
    namefortime = y["name"]
    url_time = "http://api.mojang.com/user/profiles/" + oldOwnerID + "/names"
    req2 = session.get(url_time)
    json_decoded = json.loads(req2.result().content)
    for j, i in enumerate(json_decoded):
        if name_requested.lower() == i['name'].lower():
            counted = j + 1

    timestamp_final = (json_decoded[counted]["changedToAt"] / 1000) + 3196800
if timestamp_final < time():
    print(timestamp_final)
    print(time())
    print(name_task + CYAN + "Name has already dropped !")
    exit()
# logging in to the accounts
dropdelay = float(custom_delay)

reqs_resp = []
tokens = []
uuids = []
passwords_checked = []
emails_checked = []

if time() < ((timestamp_final - dropdelay)-30):
    print(f"{name_task}Waiting for the delay to authorize accounts...")
while True:
    if time() >=((timestamp_final - dropdelay)-30):
        break
ms1 = time() * 1000
for i in range(len(Emails)):
    reqs_resp.append(session.post('https://authserver.mojang.com/authenticate',
                                  json={'agent': {'name': 'Minecraft', 'version': 1},
                                        'username': Emails[i], 'password': Passwords[i]}))
    print(f"{name_task}Sent request to login in account {i + 1}")
print(f'\n{name_task}Time it took to log in to {len(Emails)} accounts: {int(time() * 1000 - ms1)}ms')
print()
for i in range(len(Emails)):
    req = reqs_resp[i].result()
    if req.status_code == 200:
        print(
            f'{name_task}Login {GREEN}"successful"{WHITE} with {Emails[i]} | Status code = {LIGHT_GREEN}{req.status_code}')
        req = json.loads(req.content)
        tokens.append("Bearer " + req["accessToken"])
        for uuid in req["availableProfiles"]:
            uuids.append(str(uuid["id"]))
        emails_checked.append(Emails[i])
        passwords_checked.append(Passwords[i])
    else:
        print(f'{name_task}Login {RED}"failed"{WHITE} with {Emails[i]} | Status code = {LIGHT_RED}{req.status_code}')
if not emails_checked:
    print()
    print(f"{name_task}Sorry there are no working accounts... ")
    print(f"{name_task}Killing Process...")
    sleep(2)
    exit()
reqs_resp = []
# validating the accounts
print()
print(f"{name_task}Waiting for the delay to validate accounts...")
print()

for i in range(len(emails_checked)):
    req_validate = session.get("https://api.mojang.com/user/security/challenges", headers={"Authorization": tokens[i]})
    if "[]" in str(req_validate.result().content) or req_validate.result().status_code == 200:
        print(f"{name_task}Successfully verified auth token")
    else:
        print(f"\n{name_task} Security questions are needed for account {i + 1 }")
        securityq = json.loads(req_validate.result().content)
        id_1 = securityq[0]["answer"]
        question_1 = securityq[0]["question"]
        id_2 = securityq[1]["answer"]
        question_2 = securityq[1]["question"]
        id_3 = securityq[2]["answer"]
        question_3 = securityq[2]["question"]
        answer1 = input(f"\n{TearsInput}Security Question one is (" + str(
            question_1["question"]) + ")" + "\n Your answer : ")
        answer2 = input(f"\n{TearsInput}Security Question two is (" + str(
            question_1["question"]) + ")" + "\n Your answer : ")
        answer3 = input(f"\n{TearsInput}Security Question three is (" + str(
            question_1["question"]) + ")" + "\n Your answer : ")
        payload_2 = json.dumps([
            {
                "id": id_1["id"],
                "answer": answer1
            },
            {
                "id": id_2["id"],
                "answer": answer2
            },
            {
                "id": id_3["id"],
                "answer": answer3
            }
        ])

        req_validate_security = session.post("https://api.mojang.com/user/security/location",
                                             headers={"Authorization": tokens[i]}, data=payload_2)
        req_validate_security = req_validate_security.result()
        if req_validate_security.status_code == 204:
            print(f"\n{name_task}Successfully validated auth token for account {i + 1 }")

if custom_delay == "":
    dropdelay = len(emails_checked) * 0.1
else:
    send_reqs = timestamp_final - dropdelay
print(f'\n{name_task}{DARK_GRAY}Setup was {LIGHT_GREEN}successfully{DARK_GRAY} completed!')
print(f'{name_task}{DARK_GRAY}Working accounts: {len(emails_checked)} / {len(Emails)}')
print(f'{name_task}{DARK_GRAY}Using Delay: {dropdelay}')
print(f'{name_task}{DARK_GRAY}Will send requests @ {LIGHT_GREEN}{datetime.fromtimestamp(send_reqs).strftime("%H:%M:%S.%f")}')
print()
resulteds = []
# time_list = []
async def sniper_main(session_1, i):
    global count, response3
    async with session_1.post(f'https://api.mojang.com/user/profile/{uuids[i]}/name',
                              headers={"Authorization": tokens[i]},
                              json={"name": name_requested, "password": passwords_checked[i]}, ssl=False) as response:
        time_now = datetime.now()



        resulteds.append(response.status)
        # if i == 0:
        #     first_task = time_now
        # elif i == len(emails_checked) - 1:
        #     last_task = time_now
        print(f"{name_task}Sent request to change name | Status code: {response.status} @ {Fore.CYAN}{time_now}{Fore.RESET}")
        if response.status == 204:
            count = i
            webhook.set_content(title='New Snipe!',
                                description=f'`{name_requested}` was sniped yoinked using Tears :) \n`{name_requested}` was sniped on : `{emails_checked[count]}`',
                                color=0x72FF33)
            webhook.set_thumbnail(url  = f"https://crafatar.com/renders/body/{uuids[i]}.png")

            response3 = session.post('https://api.mojang.com/user/profile/' + uuids[count] + '/skin',
                                     headers=({"Authorization": tokens[count]}), data={
                    "model": "",
                    "url": "http://textures.minecraft.net/texture/a5fb5ed4925c8d29f3d2a1cb50effa26a0e210ad7c955d7eeb64f83b78769916"
                })
            webhook.send()




async def main():
    async with aiohttp.ClientSession() as session_1:
        tasks = [sniper_main(session_1, i) for i in range(len(emails_checked)) for _ in range(3)]
        start_time = time()
        await asyncio.wait(tasks)
        end_time = time()
        time_taken = end_time - start_time
        rq_sec = 3 * len(emails_checked) / time_taken
        times.append(rq_sec)
        print()
        for llk in resulteds:
            now = datetime.now()
            if llk == 400:
                print(
                    f'{name_task}Received message{RED} "NAME NOT AVAILABLE"{WHITE} | Status code: {LIGHT_RED}{llk}{WHITE} @ {Fore.CYAN}{now}{Fore.RESET}')

            elif llk == 401:
                print(
                    f'{name_task}Received message{RED} "AUTH FAILED"{WHITE} | Status code: {LIGHT_RED}{llk}{WHITE} @ {Fore.CYAN}{now}{Fore.RESET}')

            elif llk == 204:
                print(
                    f"{name_task} + {name_requested} +  was sniped {GREEN}successfully{WHITE} | Status code: {LIGHT_GREEN}{llk}{WHITE} @ {Fore.CYAN}{now}{Fore.RESET}")
                print(f"{name_task}{name_requested} was sniped on : {emails_checked[count]}")
                # notification.show_toast("Successful snipe", f"{name_requested} was yoinked successfully...",
                #                         icon_path="checkmark-512.ico",duration=50)
                if response3.result().status_code == 204 or response3.result().status_code == 200:
                    print(f'{name_task}Changed skin {GREEN}successfully')
                    print(f'{name_task}Sent message Successfully!')
                await benchmark()
                with open("accounts.txt", "r") as f:
                    lines = f.readlines()
                with open("accounts.txt", "w") as f:
                    for line in lines:
                        if emails_checked[count] in line:
                            pass
                        else:
                            f.write(line)
                print(f"{TearsInfo}Removed account from accounts.txt")
                logging.info(
                    f"{name_task}{Fore.GREEN}{str(sum(times))[0:13]}{Fore.CYAN} responses/sec {Fore.WHITE}|{Fore.CYAN} Took {Fore.WHITE}{str(time_taken)}{Fore.CYAN} seconds{Fore.RESET} | {3 * len(emails_checked)} requests")
                print(f'{name_task} Killing process...')
                sleep(2)
                exit()


            elif llk == 429:
                print(
                    f'{name_task}Received message {RED} "RATE LIMITED"{WHITE} | Status code: {LIGHT_RED}{llk}{WHITE} @ {Fore.CYAN}{now}{Fore.RESET}')

            elif llk == 504:
                print(
                    f'{name_task}Received message {RED} "GATEWAY TIMEOUT"{WHITE} | Status code: {LIGHT_RED}{llk}{WHITE} @ {Fore.CYAN}{now}{Fore.RESET}')


            else:
                print(
                    f'{name_task}Received message{RED} "Unknown Error"{WHITE} | Status code: {LIGHT_RED}{llk}{WHITE} @ {Fore.CYAN}{now}{Fore.RESET}')
        print()
        print()
        logging.info(
            f"{Fore.GREEN}{str(sum(times))[0:13]}{Fore.CYAN} responses/sec {Fore.WHITE}|{Fore.CYAN} Took {Fore.WHITE}{str(time_taken)}{Fore.CYAN} seconds{Fore.RESET} | {3 * len(emails_checked)} requests")
        await benchmark()
        print(f"{name_task}Couldn't snipe {LIGHT_RED}{name_requested}....")
        sleep(2)
        print(f'{name_task}Killing process...')


async def benchmark_reqs(session):
    async with session.get("https://snipe-benchmark.herokuapp.com/Tears-v1.0.0/snipe",ssl = False) as response:
        pass

async def benchmark():
    async with aiohttp.ClientSession() as session_2:
        bench_time = datetime.now() + timedelta(seconds=1)

        requests.post("https://snipe-benchmark.herokuapp.com/Tears-v1.0.0", json={
            "time": bench_time.timestamp() * 1000
        })
        tasks2 = [benchmark_reqs(session_2) for i in range(10)]
        while datetime.now() < bench_time:
            pass
        await asyncio.wait(tasks2)
        res = requests.get("https://snipe-benchmark.herokuapp.com/Tears-v1.0.0")
        rate = (res.json()["result"]["requests"]['rate'])
        logging.info(
            f"{name_task}{Fore.GREEN}{str(rate)}{Fore.CYAN} requests/sec")

async def warm_up():
    print(f"{TearsInfo}Starting {LIGHT_GREEN}Warm up{WHITE} before tasks...")
    print()
    async with aiohttp.ClientSession() as session_1:
        tasks = [sniper_main(session_1, i) for i in range(5)]
        await asyncio.wait(tasks)
        print()
        print(f"{TearsInfo}Warm up was {LIGHT_GREEN}successfully{WHITE} completed...")
        print()
def loop():
    loop = asyncio.get_event_loop()
    while True:
        if time() >= (send_reqs-2):
            loop.run_until_complete(warm_up())
            break
    while True:
        if time() >= send_reqs:
            asyncio.run(main())
            # loop.run_until_complete(main())
            break





loop()
