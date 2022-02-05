#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import time
from plyer import notification #for getting notification on your PC

def stringremove(string):
        char_to_remove = ["\"","/>","%"]
        for char in char_to_remove:
            try:
                string = string.replace(char,"")
            except:
                pass
        return(string)

class jiostatus:
    def __init__(self):
        URL = "http://jiofi.local.html/"
        try:
            r = requests.get(URL)
        except:
            print("Jiofi is not connected")
        soup = BeautifulSoup(r.content, 'html5lib')
   
        batterylevel = soup.find('input', attrs = {'id':'batterylevel'}) 
        batterystatus = soup.find('input', attrs = {'id':'batterystatus'})
        batterylevel = int(stringremove(str(batterylevel).split("=")[-1]))
        batterystatus = stringremove(str(batterystatus).split("=")[-1])
        self.batterylevel = batterylevel
        self.batterystatus = batterystatus

    
    def lowbattery(self, lower_limit):
        if self.batterylevel < lower_limit and self.batterystatus != "Charging":
            notification.notify(
                #title of the notification,
                title = "Jiofi battry is low. Please consider charging it.",
                #the body of the notification
                message = "Battery level = {bl} % \nBattery status = {bs}".format(
                            bl = self.batterylevel,
                            bs = self.batterystatus),  
                #creating icon for the notification
                #we need to download a icon of ico file format
                app_icon = "Custom-Icon-Design-Mono-General-3-Wifi.ico",
                # the notification stays for 50sec
                timeout  = 100
                )  
            # short delay between notifications
            time.sleep(100)
    #print("Jiofi is connected")

    def fullcharge(self):
        if self.batterylevel == 100 and self.batterystatus == "Charging":
            notification.notify(
                #title of the notification,
                title = "Jiofi battry is full. Consider pluging out.",
                #the body of the notification
                message = "Battery level = {bl} % \nBattery status = {bs}".format(
                            bl = self.batterylevel,
                            bs = self.batterystatus),  
                #creating icon for the notification
                #we need to download a icon of ico file format
                app_icon = "Custom-Icon-Design-Mono-General-3-Wifi.ico",
                # the notification stays for 50sec
                timeout  = 100
                )  
            # short delay between notifications
            time.sleep(100)
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            print("Something wrong")
            #break
        time.sleep(10*60)
