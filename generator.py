from copy import deepcopy
import json
with open("default.json")as f:
    t=json.load(f)
    # print(t)
    with open("features")as p:
        with open("manifest.json")as m:
            global j
            j=json.load(m)
            print(j)
            u=p.readlines()
            for y,line in zip(u[::2],u[1::2]):
                feat=line.strip()
                pos=y.strip()
                # print(pos,feat)
                o=deepcopy(t)
                o["Actions"][0]["Actions"][1]["Settings"]["pastedText"]=feat
                n=j["Controllers"][0]["Actions"][pos]["States"][0]["Title"]
                # print(n)
                o["States"][0]["Title"]=n
                j["Controllers"][0]["Actions"][pos]=deepcopy(o)
        with open("manifest.json","w")as x:
            json.dump(j,x)
    # print(t)