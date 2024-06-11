import os,json
from sys import argv
x=argv[1]if len(argv)>1 else input()
print("Add to...")
u=input("profile uuid:")
w=input("page uuid:")
z=os.path.join("ProfilesV2",u,"Profiles",w,"manifest.json")
print("confirm",z,"is the correct path",end="")
input()
with open(z,"r")as p:
    global t
    t=json.load(p)
    g=input("Position:")
    t["Controllers"][0]["Actions"][g]={"States":[{"Title":input("Name:")}],"UUID":"com.elgato.streamdeck.system.open","Settings":{"path":os.path.abspath(x)}}
with open(z,"w")as q:
    json.dump(t,q)