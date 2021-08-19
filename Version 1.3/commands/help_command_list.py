class Lists:
    @classmethod
    def main_help(cls):
        json_unsorted = {
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
            },
            'projects':{
                'alts':['p'],
                'desc':'Shows a list of all your projects.'
            }, 
            'suggest':{
                'desc':'Suggest me new commands and stuff.'
            }
        }
        json = {}
        for i in sorted(json_unsorted):
            json[i] = json_unsorted[i]
        return json
    @classmethod
    def manage_help(cls):
        json_unsorted = {
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
            },
            'cd':{
                'desc':'Changes the current directory to a folder inside the current folder. Use it this way: cd <foldername>. You can enter "cd.." to go back.'
            },
            'mv':{
                'alts':['move'],
                'desc':'Move file from the current directory to another. Lets say the project name is "Myxi" and there\'s a folder named "database".\n            | Inside it, there is a file named "file.db" and you want to move it to root folder "Myxi" then you have to do the command like this: "mv /database/file.db : /file.db".\n            | The seperator of both path is ":".'
            },
            'cp':{
                'alts':['copy'],
                'desc':'Same as the move command but you can copy them instead.'
            }
        }
        json = {}
        for i in sorted(json_unsorted):
            json[i] = json_unsorted[i]
        return json