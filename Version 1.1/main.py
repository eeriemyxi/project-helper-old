'''
     What is this script about?
    :- You can basically create VS Code Projects with it.
     Why would I need it?
    :- I don't know. If you need it then you can use it otherwise ignore it.
'''
import json
import os
from commands import (create,
                      help,
                      change_folder)
from color_format import Colors
import colorama
from modules import Modules
if not Modules().creator(Modules().environ_check()):
    exit()
else:
    with open('settings.json', 'r') as i:
         settings = json.loads(i.read())
         i.close()
print('Type '+colorama.Fore.GREEN+ 'help '+colorama.Style.RESET_ALL +'for a list of all available commands.')
while True:
    inp = input(">>> ")
    inp = inp.startswith
    if inp(('help', 'h')):
        help.command(Colors)
    elif inp('create'):
        create.command(settings)
    elif inp(('change_folder', 'cf', 'change-folder')):
        change_folder.command(settings, Colors)
    elif inp('exit'):
        print('Bye!')
        exit()
    else:
        print(colorama.Fore.RED+"That command doesn't exist but you can suggest me to add it! do: "+colorama.Fore.GREEN+"suggest <suggestion>"+colorama.Style.RESET_ALL)