class Lists:
    @classmethod
    def main_help(cls):
        return {
            'change_folder':{
                'alts':['cf', 'change-folder'],
                'desc':'Change the folder where your projects are created.'
            },
            'manage':{
                'alts':['m'],
                'desc':'Manage your projects. You can use this command this way: manage <project_name>.'
            },
            'help':{
                'alts':['h'],
                'desc':'Shows this message.'
            },
            'create':{
                'alts':['c'],
                'desc':'Start a new project.'
            },
            'exit':{
                'desc':'Exit this script.'
            }
        }
    @classmethod
    def manage_help(cls):
        return {
            'rm':{
                'desc':'Remove a file.'
            },
            'rmdir':{
                'alts':['rmd'],
                'desc':'Remove a directory.'
            },
            'mk':{
                'desc':'Create a file.'
            },
            'mkdir':{
                'alts':['mkd'],
                'desc':'Create a directory.'
            },
            'exit':{
                'desc':'Exit from manage mode.'
            },
            'help':{
                'alts':['h'],
                'desc':'Shows this message. Entering "help -c" will terminate the script.'
            }
        }