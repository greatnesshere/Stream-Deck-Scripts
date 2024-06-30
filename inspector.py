# Spreadsheet-like editor for Stream Deck buttons
import os, json
def is_empty(d):
    # TODO: folders refer to pages empty page=pinned page for most
    # TODO: folders can contain the subfolders of pages
    # TODO: Images<=>Thumbnails
    # TODO: pages<=>sheets
    if not d["Controllers"][0]["Actions"]:
        return True
    return False

for f in os.scandir("ProfilesV2"):
    if f.is_dir():
        with open(os.path.join(f.path,"manifest.json"))as t:
            k=json.load(t)
            # filter
            # if not k["Name"]=="Default":
            #     continue           
            print(f.name)
            print(" Name:"+k["Name"])
            print(" AppIdentifier:"+(k["AppIdentifier"]if "AppIdentifier"in k else "(None)"))
            print(" Pages:")
        for x in os.scandir(os.path.join(f.path,"Profiles")):
            if x.is_dir():
                with open(os.path.join(x.path,"manifest.json"))as z:
                    y=json.load(z)
                    print("  "+x.name+("(Empty)"if is_empty(y)else ""))