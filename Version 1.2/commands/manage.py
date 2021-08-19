import json
from color_format import Colors
import colorama as col
from commands.manage_commands import commands
col.init()
def command(inp_main):
    inp_one = " ".join(inp_main.split()[1:])
    json_data = json.loads(open('data/projects.json', 'r').read())
    path = json_data[inp_one]['path']
    if 'files' in json_data[inp_one]:
        files = json_data[inp_one]['files']
    if inp_one not in json_data:
        Colors().p_error("That project doesn't exist.")
        return
    Colors().cprint('cyan', 'For a list of all commands, type: "help"')
    while True:
        inp_idk = input(col.Fore.CYAN+f'{inp_one}'+col.Fore.RESET + ' >>> ')
        inp = inp_idk.startswith
        content = " ".join(inp_idk.split()[1:])
        if inp(('help', 'h')):
            commands.help()
        elif inp(('rmdir', 'rmd')):
            commands.rmdir(path, content)
        elif inp(('mkdir', 'mkd')):
            commands.mkdir(path, content)
        elif inp('rm'):
            commands.rm(path, content)
        elif inp('mk'):
            commands.mk(path, content)
        elif inp('exit'):
            if content == '': return
            elif content == '-c': print('Bye!') ; exit()
            else: return
        else:
            Colors().p_error("Command doesn't exist.")