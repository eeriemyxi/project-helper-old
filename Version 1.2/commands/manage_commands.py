import os
from color_format import Colors as colors
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
        if os.path.exists(pathn) is False and '/' in pathn is False and '\\' in pathn is False:
            open(pathn, 'w').close()
        else:
            colors.p_error('File already exists or '+"you're trying to create the file inside a directory.")