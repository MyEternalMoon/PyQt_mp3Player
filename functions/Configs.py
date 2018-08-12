import os
import json


def initconfig(path = "config.txt"):
    if os.path.isfile(path):
        with open(path,"r") as f:
            k = f.read()
            if (len(k)) != 0:
                info = json.loads(k,encoding="utf-8")
    else:
        info = {}
        info["musicStorage"] = os.getcwd() + "\\music"
        info["userName"] = "Administrator"
        info["config"] = \
            {
                'MusicStorage': os.getcwd()+"/music",
                "HeadStorage": os.getcwd()+"/Head",
                'searchAllDisc': ['D:'],
                'MemoryPlayList': 0,
                'circle': 1,
                'Internet':0,

            }

        with open(path, "w") as f:
            f.write(json.dumps(info))
    return info


def first_create_config(info):
    if len(info) != 4:
        return -1
    path = info[0]
    musicStorage = info[1]
    head = info[2]
    userName = info[3]
    ret = {}
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    print(os.getcwd())
    try:
        os.mkdir(path + "\\music")
        os.mkdir(path+"\\Head")
    except:
        pass
    ret["path"] = path
    ret["musicStorage"] = musicStorage
    ret["head"] = head
    ret["userName"] = userName
    with open("cond.txt", "w") as f:
        f.write(json.dumps(info))

    return ret



def saveConfig(infos):
    with open("config.txt","w") as f:
        f.write(json.dumps(infos))