import json
import requests
import random

def seller_builder(sellerkey: str,params: str): # makes my life easier
    url = f"https://keyauth.com/api/seller/?sellerkey={sellerkey}&type={params}"
    return url

class info:
    def stats(seller_key: str): # get application stats
        url = seller_builder(seller_key, "stats")
        res = requests.get(url)
        if res.status_code == 200: # ofc i will check the status code of the request, im not a retard
            res_json = res.json()
            keys = res_json["totalkeys"]
            banned_keys = res_json["banned"]
            return f"Total Keys: {keys} \n Banned Keys: {banned_keys}" # you can add more info, dont parse and just print what the request returned and see what info you can add
        else:
            return "false"
    def license_info(seller_key: str, license: str): # get license info
        url = seller_builder(seller_key, f"info&key={license}")
        res = requests.get(url)
        if res.status_code == 200: # ofc i will check the status code of the request, im not a retard
            res_json = res.json()
            status = res_json["status"]
            level = res_json["level"]
            last_login = res_json["lastlogin"]
            creation_date = res_json["creationdate"]
            infos = f"Status: {status} \n level: {level} \n last login: {last_login} \n creation date: {creation_date}" # you can add more info, dont parse and just print what the request returned and see what info you can add

            return infos
        else:
            return "false"
class gen:
    def gen_license(seller_key: str,expiration: int, mask: str, level: int, amount: int): # generate a license
        if expiration == None:
            expiration = 1
        if mask == None:
            mask = "XXXX-XXXX-XXXX-XXXX"
        if level == None:
            level = 1 
        if amount == None:
            amount = 1
        url = seller_builder(seller_key, f"add&expiry={expiration}&mask={mask}&level={level}&amount={amount}")
        res = requests.get(url)
        if res.status_code == 200:
            res_json = res.json()
            key = res_json["key"]
            return key
        elif res.status_code == 302:
            res_json = res.json()
            keys = res_json["keys"]
            return '\n'.join(map(str, keys))
        else:
            return "false"
    def gen_var(seller_key: str, var_name: str, var_value: str): # make a app var
        url = seller_builder(seller_key, f"addvar&name={var_name}&data={var_value}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def gen_sub(seller_key: str, sub_name: str, sub_level: int): # generate a sub
        random_subnames = ["my","balls","itch","can","you","scratch","them","im","totally","not","gay"]
        if sub_level == None:
            sub_level = 1
        if sub_name == None:
            sub_name = random.choice(random_subnames)
        url = seller_builder(seller_key, f"addsub&name={sub_name}&level={sub_level}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def add_hwid(seller_key: str, username: str, hwid: str): # add a hwid to a user
        url = seller_builder(seller_key,f"addhwiduser&user={username}&hwid={hwid}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def add_file(seller_key: str,file_url: str): # add a file
        url = seller_builder(seller_key, f"upload&url={file_url}")    
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    
class misc:
    def verify_license(seller_key: str, license: str): # check if that license exists
        url = seller_builder(seller_key, f"verify&key={license}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def verify_user(seller_key: str, user: str): # check if that user exists
        url = seller_builder(seller_key, f"verify&user={user}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False 
    def activate_license(seller_key: str, key: str, username: str, password: str): # activate a licesne
        url = seller_builder(seller_key, f"activate&user={username}&key={key}&pass={password}")  
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False   
    def delete_license(seller_key: str, key: str): # delete key
        url = seller_builder(seller_key, f"del&key={key}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def delete_user(seller_key: str, username: str): # delete user
        url = seller_builder(seller_key, f"deluser&user={username}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def delete_unused_keys(seller_key: str): # delete unused licenses
        url = seller_builder(seller_key, "delunused")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def delete_expr_users(seller_key: str): # deletes expired users
        url = seller_builder(seller_key, "delexpusers")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def delete_all_keys(seller_key: str): # deletes all keys
        url = seller_builder(seller_key, "delalllicenses")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
class moderation:
    def extend_user(seller_key: str, username: str, sub_name: str, duration: int): # duration in days
        if duration == None:
            duration = 1
        url = seller_builder(seller_key, f"extend&user={username}&name={sub_name}&expiry={duration}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def extend_all(seller_key: str, sub_name: str, duration: int): # duration in days
        if duration == None:
            duration = 1
        url = seller_builder(seller_key, f"extendall&name={sub_name}&expiry={duration}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def blacklist(seller_key: str, ip: str, hwid: str): # blacklist a user/hwid
        url = seller_builder(seller_key, f"black&ip={ip}&hwid={hwid}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def hwid_reset(seller_key: str, username: str): # resets the hwid
        url = seller_builder(seller_key, f"resetuser&user={username}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def reset_pw(seller_key: str, username: str): # this option doesnt even work well
        url = seller_builder(seller_key, f"resetpw&user={username}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def set_user_var(seller_key: str, username: str, var_name: str, var_value: str): # sets user variable
        url = seller_builder(seller_key, f"setvar&user={username}&var={var_name}&data={var_value}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def set_all_users_var(seller_key: str, var_name: str, var_value: str): # sets user variable
        url = seller_builder(seller_key, f"setvar&user=all&var={var_name}&data={var_value}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    #def get_user_var(seller_key: str, username: str, var_name: str): got commented out since i dont know the response, ik i can get the response but i dont use users and im too lazy to test
     #   url = seller_builder(seller_key, f"getvar&user={username}&var={var_name}")
      #  res = requests.get(url)
       # if res.status_code == 200:
        #    return True
        #else:
         #   return False
    def edit_app_var(seller_key: str, var_id: str, new_var_value: str):
        url = seller_builder(seller_key, f"editvar&varid={var_id}&data={new_var_value}")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    def del_all_vars(seller_key: str): # sets user variable
        url = seller_builder(seller_key, f"delallvars")
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    