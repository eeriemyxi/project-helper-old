import json
import os
from commands import (create,
                      help,
                      change_folder,
                      manage,
                      suggest)
from extras.color_format import Colors
import colorama
def commands(settings):
    print('Type ' + colorama.Fore.GREEN + 'help ' + colorama.Style.RESET_ALL + 'for a list of all available commands.')
    while True:
        inp_full = input(">>> ")
        inp = inp_full.startswith
        if inp(('help', 'h')):
            help.command(Colors)
        elif inp(('create', 'c')):
            create.command(settings)
        elif inp(('change_folder', 'cf', 'change-folder')):
            change_folder.command(settings, Colors)
        elif inp('exit'):
            print('Bye!');
            exit()
        elif inp(('manage', 'm')):
            if len(inp_full.split()) >= 2:
                manage.command(inp_full)
            else:
                print("You forgot to enter the project name after typing manage.")
        elif inp('suggest'):
            suggest.command()
        elif inp(('projects', 'p')):
            with open('data/projects.json', 'r') as file:
                print('Lists of all projects:')
                file = json.loads(file.read())
                for project in file:
                    print('Name:', project)
                    print('Project path:', file[project]['path'])
        else:
            print(
                colorama.Fore.RED + "That command doesn't exist but you can suggest me to add it! do: " + colorama.Fore.GREEN + "suggest <suggestion>" + colorama.Style.RESET_ALL)