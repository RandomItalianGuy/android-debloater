import json,subprocess,os
from time import sleep
from os import system, name

def clearScreen(): 
    # for windows os
    if name == 'nt': 
        clrscr = system('cls') 
    # for mac and linux os
    else: 
        clrscr = system('clear') 

print("\nHi, welcome to version 0.3.1 of my Android-Debloater Script.\nIf you have read the disclaimer, press Y. Press any other key to exit the script.\n")
ch=input()
if ch.lower()=="y":
    directory = 'packages/'
    print('\nYou can choose from one of the following json files.\n')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"): 
            print(os.path.splitext(filename)[0])
            continue
            
    print("\nWhich json do you want to choose?")
    str=input()    
    if file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename == (str+'.json'):
            clearScreen()
            print('\nYou have chosen the following json: '+str)
            sleep(1)
        else:
            print("\nThe package that you selected doesn't exist. The script is terminating.")
            exit()     
            
    print('\nDo you want to run the script in auto mode?\nPress Y if so, or any other key to start manual mode.')    
    ch=input()
    if ch.lower()=="y":
        print('\nThe script will start in auto mode in 2 seconds.')
        sleep(2)
        with open('packages/'+str+'.json') as json_file:
            data = json.load(json_file)
        for p in data[str]:
            try:    
                result = subprocess.check_output('adb shell pm uninstall -k --user 0 ' + p['package_name'], stderr=subprocess.STDOUT)                 
                print('App ' + p['display_name'] + 'uninstalled.\n')
                sleep(1)          
            except subprocess.CalledProcessError as e:
                print('\nError: ' + e.stdout.decode('utf-8'))
                print('App "' + p['display_name'] + '" not uninstalled.\n')              
    else:
    
        print('Starting manual mode.')
        with open('packages/'+str+'.json') as json_file:
            data = json.load(json_file)
        for p in data[str]:
            print('\nApp name: ' + p['display_name'])
            print('Package name: ' + p['package_name'] + "\n")
            print('Notes: ' + p['notes'] + "\n")
            print('Press Y to uninstall, any other key to skip')
            ch=input()
            if ch.lower()=="y":          
                try:    
                    result = subprocess.check_output('adb shell pm uninstall -k --user 0 ' + p['package_name'], stderr=subprocess.STDOUT)                 
                    print('App uninstalled.\n')
                    sleep(1)
                    clearScreen()              
                except subprocess.CalledProcessError as e:
                    print('\nError: ' + e.stdout.decode('utf-8'))
                    print('App' + p['display_name'] + ' not uninstalled.\n')
            else:
                print('App skipped.\n')
                sleep(1)
                clearScreen()   
else:
    print("You didn't accept the disclaimer. The script is terminating.")  
    exit()
    
    
    


