#!/usr/bin/env python3
import glob,os.path,json,argparse
parser=argparse.ArgumentParser()
parser.add_argument("--md",action="store_true")
args=parser.parse_args()
def link(path):
    return f"[{os.path.basename(os.path.dirname(path))}]({path})"
for profile in glob.iglob("ProfilesV2/*/"):
    with open(os.path.join(profile,"manifest.json"),encoding="utf-8") as manifest:
        contents=json.load(manifest)
        name=contents["Name"]
        # I couldn't find any other useful info
        if args.md:
            print("# ",end="")
        if 'AppIdentifier' in contents:
            print(f"{name} {"`" if args.md else ""}[{contents["AppIdentifier"]}]{"`" if args.md else ""}")
        else:
            print(f"{name}")
        if args.md:
            print()
    for page in glob.iglob(os.path.join(profile,"Profiles/*/")):
        with open(os.path.join(page,"manifest.json"),encoding="utf-8") as manifest:
            contents=json.load(manifest)
            print(" - " if args.md else "    ",end="")
            for controller in contents["Controllers"]:
                if controller["Actions"]:
                    print(f"{link(page)}")
                    break
            else:
                print(f"{link(page)} (empty)")
            if args.md:
                print()