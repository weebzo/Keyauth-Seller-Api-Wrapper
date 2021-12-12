import json
from auth_helper import info
from auth_helper import gen


with open("config.json","r") as f:
        config = json.load(f)
        print("Config Loaded")

stats = info.stats(config["seller_keys"][0])
license_info = info.license_info(config["seller_keys"][0],"FF7-LI2-STU-D63")
gen_keys = gen.gen_license(config["seller_keys"][0],1,None,1,5)
if stats != "false":
    print(stats)
else:
    print("couldnt get stats")
if license_info != "false":
    print(license_info)
else:
    print("Couldnt get info")
if gen_keys != "failed":
    print(gen_keys)
else:
    print("Could gen keys")

