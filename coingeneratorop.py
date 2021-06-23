from concurrent.futures import ProcessPoolExecutor
from amino import Client
from amino import SubClient
from amino import lib
from datetime import datetime
from os import path
from hashlib import sha1
import webbrowser
import base64
import string   
import random
import json
from concurrent.futures import ThreadPoolExecutor
THIS_FOLDER = path.dirname(path.abspath(__file__))
devicefile=path.join(THIS_FOLDER,"device")
from yaml import load, FullLoader

def load_bots():
    with open('bots.yaml', 'r', encoding="utf-8") as yaml_file:
        return load(yaml_file, Loader=FullLoader)
        
bots = load_bots()

def gendevid(st: int = 50):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = st))
    dev='01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + MetaSpecial.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
    return dev

def magicnum():
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime

def sendobj(sub: SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ]
    sub.send_active_obj(timers=timer)

def log(cli: Client, email: str):
    try:
        cli.login_sid(SID=email['sid'])
        print(f"logged into {email['email']}\n")
    except Exception as e:
        print(e)
        return None

def task(client: Client,sub: SubClient,email: str,cid: str,i : int):
    try:
        sendobj(sub)
        print(f"Sent coin generating object for {email['email']} times :- {i+1}")
    except:
        return None

def threadit(email: str):
    print(email['email'])
    cid="17186288"
    device=gendevid()
    dicto={
    "device_id": f"{device}",
    "device_id_sig": "Aa0ZDPOEgjt1EhyVYyZ5FgSZSqJt",
    "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
    }
    devfile=open(devicefile,"w")
    json.dump(dicto,devfile)
    devfile.close()
    client=Client(deviceId=device)
    print("client created")
    log(cli=client,email=email)
    subclient=SubClient(comId=cid,profile=client.profile)
    for i in range(30):
        task(client,subclient,email,cid,i)
    print(f"FINISHED MINING {email['email']}")

def main():
    with ProcessPoolExecutor(max_workers=60) as executor:
        _ = [executor.submit(threadit, bot) for bot in bots]

if __name__ == '__main__':
    main()
