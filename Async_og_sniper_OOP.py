import blocking
import requests
from colorama import Fore, init, Style
import json
import urllib3
from time import time, sleep
import asyncio
import aiohttp
from datetime import datetime
# from datetime import timedelta
import threading
from itertools import islice
import os
import timeit
from licensing.models import *
from licensing.methods import Key, Helpers
from requests_futures.sessions import FuturesSession
session = FuturesSession()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init()
class og_sniper:
    def __init__(self):
        # ctypes.windll.kernel32.SetConsoleTitleW(f"Teen name sniper | Anas#6812")
        print("\n\n    ███        ▄████████    ▄████████ ███▄▄▄▄   ")
        time.sleep(0.2)
        print("▀█████████▄   ███    ███   ███    ███ ███▀▀▀██▄ ")
        time.sleep(0.2)
        print("   ▀███▀▀██   ███    █▀    ███    █▀  ███   ███ ")
        time.sleep(0.2)
        print("    ███   ▀  ▄███▄▄▄      ▄███▄▄▄     ███   ███ ")
        time.sleep(0.2)
        print("    ███     ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███ ")
        time.sleep(0.2)
        print("    ███       ███    █▄    ███    █▄  ███   ███ ")
        time.sleep(0.2)
        print("    ███       ███    ███   ███    ███ ███   ███ ")
        time.sleep(0.2)
        print("   ▄████▀     ██████████   ██████████  ▀█   █▀  ")
        time.sleep(0.2)
        print("                                                ")
        time.sleep(0.2)
        print(Fore.GREEN + "\n[Teen]" + Style.RESET_ALL + " Welcome to Teen sniper!")
        self.name_requested = input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " Name you wanna snipe : ")
        self.proxy_option = input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " Do you wanna use proxies (y/n)? : ")
        self.Threads = int(input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " How many threads do I use : "))
        calculate_ping = (
                Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " Calculating ping with mojang server... ")
        print(calculate_ping)
        time.sleep(1)
        self.accounts_location = int(input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " Do u wanna add accounts or import from file ? (1/2) : "))
        time.sleep(1)
        self.accounts = []
        self.responses = []
        if int(self.accounts_location) == 1:
            self.num_account_used = int(
                input(
                    Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " How many accounts do u wanna use? : "))
            for i in range(int(self.num_account_used)):
                self.account_used = input(
                    Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " Account you wanna use to snipe (email:password) : ")
                self.account_used.strip()
                self.accounts.append(self.account_used)
            print(
                Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " Getting Bearer and uuid . . .")
        elif int(self.accounts_location) == 2:
            self.num_account_used = int(
                input(
                    Fore.GREEN + "\n[" + Style.RESET_ALL + "Starting" + Fore.GREEN + "]" + Style.RESET_ALL + " How many accounts do u wanna use? : "))
            self.combo_loader(self.num_account_used)

    def combo_loader(self, number_accounts):
        _combo_ = open("accounts.txt", "r").readlines()
        lines_cache = islice(_combo_, number_accounts)
        _combo_new = [items.rstrip() for items in lines_cache]
        for lines in _combo_new:
            self.accounts.append(lines)

    def security_questions(self, response, url3, headers_head):
        y2 = json.loads(response)

        id_1 = y2[0]["answer"]
        question_1 = y2[0]["question"]
        id_2 = y2[1]["answer"]
        question_2 = y2[1]["question"]
        id_3 = y2[2]["answer"]
        question_3 = y2[2]["question"]
        answer1 = input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Validating" + Fore.GREEN + "]" + Style.RESET_ALL + " Security Question one is (" + str(
                question_1["question"]) + ")" + "\n Your answer : ")
        answer2 = input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Validating" + Fore.GREEN + "]" + Style.RESET_ALL + " Security Question two is (" + str(
                question_2["question"]) + ")" + "\n Your answer : ")
        answer3 = input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Validating" + Fore.GREEN + "]" + Style.RESET_ALL + " Security Question three is (" + str(
                question_3["question"]) + ")" + "\n Your answer : ")
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

        req_validate_security = requests.post(url3, headers=headers_head, data=payload_2)
        return req_validate_security.status_code

    def mojang_time(self):
        username = self.name_requested
        timestamp2 = time.time()
        timestamp3 = str(timestamp2).split('.')
        url_id = "http://api.mojang.com/users/profiles/minecraft/" + username + "?at=0" + str(
            int(timestamp3[0]) - 3196800)

        req = requests.get(url_id)
        y = json.loads(req.content)
        if self.name_requested in str(req.content):
            print(
                Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.RED + "]" + Style.RESET_ALL + "Name not available")
            return False

        else:
            oldOwnerID = y["id"]
            namefortime = y["name"]
            url_time = "http://api.mojang.com/user/profiles/" + oldOwnerID + "/names"
            req2 = requests.get(url_time)
            decoded = req2.content.decode("utf-8")
            json_decoded = json.loads(decoded)

            for count, i in enumerate(json_decoded):
                if username == i["name"]:
                    timestamp_final = (json_decoded[count + 1]["changedToAt"])
                    timestamp_final = int(timestamp_final) + 3196800000
            timestamp = datetime.datetime.fromtimestamp(timestamp_final / 1e3)
            self.time_drop = timestamp
            self.time_drop2 = self.time_drop.strftime("%I:%M:%S")

    def authentication(self, user, password):
        url = "https://authserver.mojang.com/authenticate"
        url2 = "https://api.mojang.com/user/security/challenges"
        url3 = "https://api.mojang.com/user/security/location"
        header = {
            "content-type": "application/json"
        }

        payload = json.dumps({

            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": user,
            "password": password,
            "requestUser": "true"
        })

        req = session.post(url, headers=header, data=payload)

        response = req.result().content
        if "accessToken" in str(response):
            y = json.loads(response)
            available_profiles = (y["availableProfiles"])
            name = (available_profiles[0]['name'])
            print(
                Fore.GREEN + "\n[" + Style.RESET_ALL + "Success" + Fore.GREEN + "]" + Style.RESET_ALL + " Logged in successfully as "+Fore.LIGHTBLUE_EX + name)
            # the result is a Python dictionary:
            authtoken = (y["accessToken"])
            self.authtoken3 = "Bearer " + authtoken
            headers_head = {"Authorization": self.authtoken3}
            req_validate = session.get(url2, headers=headers_head)
            if "[]" in str(req_validate.result().content):
                print(
                    Fore.GREEN + "\n[" + Style.RESET_ALL + "Success" + Fore.GREEN + "]" + Style.RESET_ALL + " Successfully validated auth token")
                return response
            else:
                print(
                    Fore.GREEN + "\n[" + Style.RESET_ALL + "Validating" + Fore.GREEN + "]" + Style.RESET_ALL + " Security questions are needed")
                security_ques = self.security_questions(req_validate.content, url3, headers_head)
                if security_ques == 204:
                    print(
                        Fore.GREEN + "\n[" + Style.RESET_ALL + "Success" + Fore.GREEN + "]" + Style.RESET_ALL + " Successfully validated auth token")
                    return response

        else:
            print(
                Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.RED + "]" + Style.RESET_ALL + " Login Failed with " + Fore.LIGHTBLUE_EX + user + "| Status code: " + str(req.result().status_code))
            return False

    def authentication2(self, user, password):
        y = self.authentication(user, password)
        if y is False:
            return False
            
        else:
            y = json.loads(y)
            authtoken = (y["accessToken"])
            authtoken2 = "Bearer " + authtoken
            profiles_uuid = (y["availableProfiles"])
            uuid = (profiles_uuid[0]['id'])
            headers_head = {"content-type": "application/json",
                            "Authorization": authtoken2}

            data1 = json.dumps({"name": self.name_requested, "password": password})
            return uuid, headers_head, data1

    def initialize(self):
        self.ms1 = time.time() * 1000
        for i in self.accounts:
            self.userpass = i.split(":")
            self.resp = self.authentication2(self.userpass[0], self.userpass[1])

            if self.resp is False:
                pass
            else:
                self.responses.append(self.resp)
        print()
        print(f'Time it took to log in to {len(self.accounts)} accounts: {int(time.time() * 1000 - self.ms1)}ms')
        sleep(.5)
        print()
        self.num_account_used = len(self.responses)

    def skin_change(self, whole_response):
        uuid2 = whole_response[0]
        url2 = "https://api.mojang.com/user/profile/" + uuid2 + "/skin"
        headers2 = {
            "Authorization": whole_response[1]
        }
        data2 = {
            "model": "",
            "url": "https://textures.minecraft.net/texture/9e3de071bf77754737ce68f36da9ac77e00f261fda2aaa554afe19538cc8710c"

        }
        req = requests.post(url2, headers=headers2, data=data2)
        if req.status_code == 204:
            print(
                Fore.GREEN + "\n[" + Style.RESET_ALL + "Success" + Fore.GREEN + "]" + Style.RESET_ALL + " Successfully uploaded the skin!\n")
        else:
            pass

    async def sniper_main(self, session, whole_response):
        url = "http://api.mojang.com/user/profile/" + whole_response[0] + "/name"
        start = timeit.default_timer()
        async with session.post(url, headers=whole_response[1], data=whole_response[2]) as response:
            stop = timeit.default_timer()
            if response.status == 401:
                print("[" + str(
                    stop - start) + "]" + Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.RED + "]" + Style.RESET_ALL + " Auth Failed! | Using account : " +
                      whole_response[
                          0] + " " + str(
                    response.status) + " " + str(datetime.fromtimestamp(int(round(time.time() * 1000)) / 1e3))+ "               \n")

            elif response.status == 204:
                print("[" + str(
                    stop - start) + "]" + Fore.GREEN + "\n[" + Style.RESET_ALL + "Success" + Fore.GREEN + "]" + Style.RESET_ALL + self.name_requested + " was sniped successfully  " + str(
                    response.status) + " " + str(datetime.fromtimestamp(int(round(time.time() * 1000)) / 1e3))+ "               \n")
                self.skin_change(whole_response)

            else:
                print("[" + str(
                    stop - start) + "]" + Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.RED + "]" + Style.RESET_ALL + " Name not available! | Using account : " +
                      whole_response[
                          0] + " " + str(response.status) + " " + str(
                    datetime.fromtimestamp(int(round(time.time() * 1000)) / 1e3))+ "               \n")

    async def sniper_main_proxies(self, session, whole_response):
        async with session.post("https://api.mojang.com/user/profile/" + whole_response[0] + "/name",
                                headers={"content-type": "application/json",
                                         "Authorization": whole_response[1]}, data=whole_response[2],
                                proxy="http://lum-customer-hl_8a7d6d92-zone-static:540s5kymyhti@zproxy.lum-superproxy.io:22225") as response:

            if response.status == 204:
                print(
                    Fore.GREEN + "\n[" + Style.RESET_ALL + "Success" + Fore.GREEN + "]" + Style.RESET_ALL + self.name_requested + " was sniped successfully \n " + str(
                        response.status) + " " + time.strftime("%I:%M:%S"))
                self.skin_change(whole_response)
            elif response.status == 401 or response.status == 429:
                print(
                    Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.GREEN + "]" + Style.RESET_ALL + " Auth Failed! | Using account : " +
                    whole_response[
                        0] + " \n " + str(
                        response.status) + " " + time.strftime("%I:%M:%S"))
            else:
                print(
                    Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.GREEN + "]" + Style.RESET_ALL + " Name not available! | Using account : " +
                    whole_response[
                        0] + " \n " + str(response.status) + " " + time.strftime("%I:%M:%S"))

    def loop(self, id):
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # loop.run_until_complete(self.main(id))
        asyncio.run(self.main(id))

    async def main(self, id):
        async with aiohttp.ClientSession() as session_1:
            if str(self.proxy_option) == "y":
                tasks = [self.sniper_main_proxies(session_1, self.responses[id]) for _ in range(20)]
                await asyncio.gather(*tasks)
                print((datetime.fromtimestamp(int(round(time.time() * 1000)) / 1e3)))
            elif str(self.proxy_option) == "n":
                tasks = [self.sniper_main(session_1, self.responses[id]) for _ in range(20)]
                await asyncio.gather(*tasks)
                print((datetime.fromtimestamp(int(round(time.time() * 1000)) / 1e3)))
    def threading(self):
        time_resp = self.mojang_time()
        if time_resp is False:
            pass
        else:
            self.initialize()
            if not self.responses:
                print(
                    Fore.RED + "\n[" + Style.RESET_ALL + "Failed" + Fore.RED + "]" + Style.RESET_ALL + "There are no working accounts :(")
            else:
                print(Fore.GREEN + "\n[Sniping]" + Style.RESET_ALL + " Preparing to snipe name . . .\n")
                time.sleep(3)
                print(Fore.GREEN + "[Sniping]" + Style.RESET_ALL + " Waiting for the delay . . .\n")
                print(Fore.GREEN + "[Sniping]" + Style.RESET_ALL + " " + self.name_requested + " is dropping at: " + self.time_drop2)
                while True:
                    time_str = time.strftime("%I:%M:%S")
                    if self.num_account_used == 1:
                        if self.time_drop2 == time_str:
                            self.loop(0)
                    else:
                        threads = [threading.Thread(target=self.loop, args=(i,)) for i in range(self.num_account_used)]
                        if self.time_drop2 == time_str:
                            [t.start() for t in threads]
                            break

if __name__ == "__main__":
    os.system("cls")
    print("\n\n    ███        ▄████████    ▄████████ ███▄▄▄▄   ")
    print("▀█████████▄   ███    ███   ███    ███ ███▀▀▀██▄ ")
    print("   ▀███▀▀██   ███    █▀    ███    █▀  ███   ███ ")
    print("    ███   ▀  ▄███▄▄▄      ▄███▄▄▄     ███   ███ ")
    print("    ███     ▀▀███▀▀▀     ▀▀███▀▀▀     ███   ███ ")
    print("    ███       ███    █▄    ███    █▄  ███   ███ ")
    print("    ███       ███    ███   ███    ███ ███   ███ ")
    print("   ▄████▀     ██████████   ██████████  ▀█   █▀  ")
    print("                                                ")
    license = input(Fore.GREEN + "\n[" + Style.RESET_ALL + "Teen" + Fore.GREEN + "]" + Style.RESET_ALL + " Enter your license  : ")
    RSAPubKey = "<RSAKeyValue><Modulus>6rzJTmoL+pk0IYakpLbiHtA7jzF9w8RLgHA6w58Q268EV4Wi7Nxa2r4mctJ0g/lbIwzLbkAAb+LUOTkh17ogCn8Jv5ofESLGyAXLTtoZxkZ8ZvVY88SmtPwu4YckDdm34eaNYxq4d+XHNd1J43y7BR+zw2xT5jplKcIAPdNKd0APjVTLTrvwU/XC+hbmBJI1lrrSynl2QPTJdyV33Cwdhv+pRYzJQUsraL/TsK4ykQoLIJmwcbUS1tYslSnolvhbcXlloBXmrvwl+Q4exSMRGz7lJBB6D7fgHRYaW20+UVDsqZZ0pT63dNMc2lkwlyKph4zbuBVnsqDEDhAojvXbhQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
    auth = "WyI5MzY0NCIsImlPaGtVVkl1YmxZaWNMRHJzVHVCb0tCMStya1FNTmhhMDhzZmlzNnoiXQ=="
    result = Key.activate(token=auth,
                          rsa_pub_key=RSAPubKey,
                          product_id=7472,
                          key=license,
                          machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        print("\n" + Fore.RED + "\n[" + Style.RESET_ALL + "Teen" + Fore.RED + "]" + Style.RESET_ALL + " The license does not work: {0}".format(result[1]))
    else:
        # everything went fine if we are here!
        print("\n" +
            Fore.GREEN + "[" + Style.RESET_ALL + "Teen" + Fore.GREEN + "]" + Style.RESET_ALL +"The license is valid!")
        print("\n[Teen] Choose your mode")
        print("1) Snipe a name")
        print("2) Block a name")
        option = input(
            Fore.GREEN + "\n[" + Style.RESET_ALL + "Teen" + Fore.GREEN + "]" + Style.RESET_ALL + " Whats your option? : ")
        while True:
            if option == "1":
                os.system("cls")
                og_sniper().threading()

                break
            elif option == "2":
                os.system("cls")
                blocking.blocking().threading()
                break
            else:
                print(Fore.GREEN + (
                        "\n[" + Style.RESET_ALL + "Teen" + Fore.GREEN + "]" + Style.RESET_ALL + " Invalid option!"))
                break
