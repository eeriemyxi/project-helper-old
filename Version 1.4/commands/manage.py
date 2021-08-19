import json
import os
from extras.color_format import Colors
import colorama as col
from commands.manage_commands import commands
col.init()
def command(inp_main):
    cd_path = ''
    inp_one = " ".join(inp_main.split()[1:])
    json_data = json.loads(open('data/projects.json', 'r').read())
    if inp_one not in json_data:
        Colors().p_error("That project doesn't exist.")
        return
    path = json_data[inp_one]['path']
    if 'files' in json_data[inp_one]:
        files = json_data[inp_one]['files']
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
        elif inp('cd'):
            if inp_idk == 'cd..':
                path = list(os.path.split(path))[0] ; inp_one = list(os.path.split(inp_one))[0]
            else:
                paths=commands.cd(path, content, inp_one)
                if paths:
                    inp_one = paths['short_path']
                    path = paths['fullpath']
        elif inp('exit'):
            if content == '': return
            elif content == '-c': print('Bye!') ; exit()
            else: return
        elif inp(('mv', 'move')):
            if content != '':
                commands.mv(path, content)
            else:
                Colors.p_error('Empty input.')
        elif inp(('cp', 'copy')):
            if content != '':
                commands.cp(path, content)
            else:
                Colors.p_error('Empty input.')
        elif inp(('listdir', 'ld')):
            commands.listdir(path)
        elif inp(('ren', 'rename')):
            commands.ren(path, content)
        else:
            Colors().p_error("Command doesn't exist.")