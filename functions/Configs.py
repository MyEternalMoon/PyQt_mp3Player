import os
import json




def initconfig():
    if os.path.isfile("config.txt"):
        with open("config.txt","r") as f:
            k = f.read()
            if (len(k)) != 0:
                info = json.loads(k,encoding="utf-8")
            else:
                info = {}
                info["musicStorage"] = os.getcwd() + "\\music"
                info["userName"] = "Administrator"
    else:
        info={}
        info["musicStorage"] = os.getcwd()+"\\music"
        info["userName"] = "Administrator"

    with open("config.txt","w") as f:
        f.write(json.dumps(info))
   # print(info)
    return info


def saveConfig(infos):
    with open("config.txt","w") as f:
        f.write(json.dumps(infos))