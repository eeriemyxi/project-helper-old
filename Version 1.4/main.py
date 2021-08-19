"""
     What is this script about?
    :- You can basically create coding projects with it. 
       It will create project folders for you automatically. You can manage them.
       Delete or create folder and files. Move them or copy them.
     Why would I need it?
    :- I don't know. If you need it then you can use it otherwise ignore it.
"""
'''
    This is version 1.3.
    - I've added few new commands.
    - Now it logs some of the stuff that may crash the script.
    - There is now a command line interface. You can look for it in the extras directory.
    Add cli.exe to PATH and rename the file to whatever you want. Then you can simply type the name of
    the executable to launch the script. Specify the path of the main.py file by cli.exe --path "path here".
    - Fixed some possiblities to crash the script.
'''
import json
import os
import lobby_commands
from commands import (create,
                      help,
                      change_folder,
                      manage,
                      suggest)
from extras.color_format import Colors
from startup import Startup
import logging
from extras import log
if not Startup.creator(Startup.data_folder_checkup()):
    exit()
else:
    print('Please wait untill we verify that everything is working fine.')
    if os.path.exists('logs') is False: os.mkdir('logs')
    if os.path.exists('logs/log.log'): os.remove('logs/log.log')
    logging.basicConfig(filename='logs/log.log', level=logging.DEBUG) ; log.start(logging)
    with open('data/settings.json', 'r') as i: settings = json.loads(i.read())
    Colors.cprint('green','Everything is working fine! Starting...')
lobby_commands.commands(settings)