import os, shutil, colorama
from extras.color_format import Colors as colors 
from commands.help_command_list import Lists
class commands:
    @classmethod
    def help(cls):
        json = Lists.manage_help()
        for name in json:
            alts = ''
            if 'alts' in json[name]:
                alts = ' | ' + " | ".join(json[name]['alts'])
            print(f"""{name}{alts}
            - {json[name]['desc']}""")
    @classmethod
    def rmdir(cls,path, dir):
        if os.path.exists(path+'/'+dir):
            os.rmdir(path+'/'+dir)
            colors.cprint('green', 'Folder removed.')
        else:
            colors.p_error("Folder doesn't exist.")
    @classmethod
    def mkdir(cls, path, dir):
        if os.path.exists(path + '/' + dir) is False:
            os.mkdir(path + '/' + dir)
            colors.cprint('green', 'Folder added.')
        else:
            colors.p_error("Folder already exists.")
    @classmethod
    def rm(cls, path, file):
        if os.path.exists(path+'/'+file) and os.path.isfile(path+'/'+file):
            os.remove(path+'/'+file)
            colors.cprint('green', 'File removed.')
        else:
            colors.p_error("File doesn't exist or it's a folder. To delete a folder, you can use "+'"rmdir" command')
    @classmethod
    def mk(cls, path, name):
        pathn = path + '/' + name
        if os.path.exists(pathn) is False:
            open(pathn, 'w').close()
            print('File added.')
        else:
            colors.p_error('File already exists.')
    @classmethod
    def cd(cls,path, content, inp_one):
        if content != '':
            pathn = path + '\\' + content
            if os.path.exists(pathn) and os.path.isdir(pathn):
                return {
                    "fullpath": os.path.join(path, content),
                    "short_path": inp_one+'\\'+content
                }
            else:
                colors.p_error("Directory doesn't exist.")
                return None
        else:
            print('You forgot to include the path.')
    @classmethod
    def mv(cls, path, content):
        if len(content.split(':')) == 2:
            paths = [ path + i.strip(' ') for i in content.split(':') ]
            if os.path.exists(paths[0]) is True and os.path.exists(paths[1]) is False:
                try: shutil.move(paths[0], paths[1])
                except FileNotFoundError: colors.p_error('Invalid path.')
                else: colors.cprint('green', 'Done.')
            else: colors.p_error('The path where you want to move already exists. or the path from where you want to move doesn\'t.') ; return
        else:
            colors.p_error('You forgot to split both paths by : or you entered more or less than 2 paths.')
    @classmethod
    def cp(cls, path, content):
        if len(content.split(':')) == 2:
            paths = [ path + i.strip(' ') for i in content.split(':') ]
            if os.path.exists(paths[0]) is True and os.path.exists(paths[1]) is False:
                try: shutil.copy(paths[0], paths[1])
                except FileNotFoundError: colors.p_error('Invalid path.')
                except shutil.SameFileError: colors.p_error('Both of your entered path are same.')
                else: colors.cprint('green', 'Done.')
            else: colors.p_error('The path where you want to copy already exists. or the path from where you want to copy doesn\'t.') ; return
        else:
            colors.p_error('You forgot to split both paths by : or you entered more or less than 2 paths.')
    @classmethod
    def listdir(cls, path):
        print('The files and directories has been color formatted.')
        print(colorama.Fore.MAGENTA+'MAGENTA COLOR: A directory\n'+colorama.Fore.RESET+colorama.Fore.YELLOW+'YELLOW COLOR: A file.'+colorama.Fore.RESET)
        print('=:='*15)
        files = os.listdir(path)
        if len(files) == 0: print(colorama.Fore.RED+'No files found.'+colorama.Fore.RESET)
        for file in files:
            if os.path.isfile(os.path.join(path, file)):
                print('     '+colorama.Fore.YELLOW+file+colorama.Fore.GREEN+' - [ TYPE: FILE ]'+colorama.Fore.RESET)
            elif os.path.isdir(os.path.join(path, file)):
                print('     '+colorama.Fore.MAGENTA+file+colorama.Fore.GREEN+' - [ TYPE: DIR ]'+colorama.Fore.RESET)
            else: print('     '+colorama.Fore.RED+file+colorama.Fore.GREEN+' - [TYPE: UNKNOWN ]'+colorama.Fore.RESET)
    @classmethod
    def ren(cls,path, content):
        content = [ i.strip(' ') for i in content.split(':') ] 
        if len(content) != 2:
            colors.p_error("You've entered more or less than 2 path. Remember the seperator is \":\"")
            return
        if os.path.exists(f'{path}/{content[0]}') is False:
            colors.p_error('Source path doesn\'t exist.')
            return
        if os.path.exists(f'{path}/{content[1]}') is True:
            colors.p_error(f'A file named "{content[1]}" already exists.')
            return
        else:
            try: os.rename(f'{path}/{content[0]}', f'{path}/{content[1]}')
            except Exception as e:
                print('Something went wrong. Please mail me the error below at mail@myxi.tk') ; print(e)
            else: colors.cprint('green','Done.')