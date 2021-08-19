"""
     What is this script about?
    :- You can basically create VS Code Projects with it.
     Why would I need it?
    :- I don't know. If you need it then you can use it otherwise ignore it.
"""
'''
    This is version 1.2.
'''
import json
import os
from commands import (create,
                      help,
                      change_folder,
                      manage)
from color_format import Colors
import colorama
from modules import Modules
if not Modules().creator(Modules().environ_check()):
    exit()
else:
    with open('data/settings.json', 'r') as i:
         settings = json.loads(i.read())
         i.close()
print('Type '+colorama.Fore.GREEN+ 'help '+colorama.Style.RESET_ALL +'for a list of all available commands.')
while True:
    inp_full = input(">>> ")
    inp = inp_full.startswith
    if inp(('help', 'h')):
        help.command(Colors)
    elif inp('create'):
        create.command(settings)
    elif inp(('change_folder', 'cf', 'change-folder')):
        change_folder.command(settings, Colors)
    elif inp('exit'):
        print('Bye!') ; exit()
    elif inp(('manage', 'm')):
        if len(inp_full.split()) >= 2:
            manage.command(inp_full)
        else:
            print("You forgot to enter the project name after typing manage.")
    else:
        print(colorama.Fore.RED+"That command doesn't exist but you can suggest me to add it! do: "+colorama.Fore.GREEN+"suggest <suggestion>"+colorama.Style.RESET_ALL)