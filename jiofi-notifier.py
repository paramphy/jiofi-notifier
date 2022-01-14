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
def battery():  
    URL = "http://jiofi.local.html/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
   
    batterylevel = soup.find('input', attrs = {'id':'batterylevel'}) 
    batterystatus = soup.find('input', attrs = {'id':'batterystatus'})
    batterylevel = int(stringremove(str(batterylevel).split("=")[-1]))
    batterystatus = stringremove(str(batterystatus).split("=")[-1])
    return(batterylevel,batterystatus)
def main():

    batterylevel, batterystatus = battery()
    print("Jiofi is connected")
    if batterylevel < 25 and batterystatus != "Charging":
        notification.notify(
            #title of the notification,
            title = "Jiofi battry is low. Please consider charging it.",
            #the body of the notification
            message = "Battery level = {bl} % \nBattery status = {bs}".format(
                        bl = batterylevel,
                        bs = batterystatus),  
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
