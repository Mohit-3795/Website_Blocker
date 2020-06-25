# private/etc/hosts
#also you wanna add the final landing domain that you see on the webpage to do the blocking


import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.hotmail.com", "www.yahoo.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() <dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print("...wokring hours...")        
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        #print (content)
        
    else:
        print ("...free time... \n")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list): #here the section "for website in website_list" is just to describe what the variable website is which we have used in the starting i.e "if not any(website in line.......) "
                    file.write(line)
            file.truncate()
        
        #print (content) 
    time.sleep(3600)
