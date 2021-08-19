import colorama as color
import os
import json
os.system('') # Enables color formated text on the Terminal
class Startup:
    def validate_path(self, path):
        if not os.path.exists(path):
            print(color.Fore.RED+'''That path doesn't exist. Please enter a valid path or to exit you can type "exit"''',color.Style.RESET_ALL)
            while True:
                inp = input('Enter: ')
                if len(inp) != "":
                    if inp == 'exit':
                        return False
                    elif not os.path.exists(inp):
                        print(color.Fore.RED+'''That path doesn't exist. Please enter a valid path or to exit you can type "exit"''',color.Style.RESET_ALL)
                    elif os.path.exists(inp):
                        return inp
                else:
                    print(color.Fore.RED+'''That path doesn't exist. Please enter a valid path or to exit you can type "exit"''',color.Style.RESET_ALL)
        else: return path
    @classmethod
    def data_folder_checkup(self):
        if os.path.exists('data/settings.json'):
            return True
        elif not os.path.exists('data/settings.json'):
            return None
    @classmethod
    def creator(self, a):
        if a:
            print('Hey welcome back!')
            return True
        elif not a:
            print('Welcome!')
            print("""So, for me to work, you've to tell me where you want to create the projects. 
Simply enter "Yes" to continue. To cancel, you can type anything you want that doesn't start with "Y".""")
            if input("Enter: ").lower().startswith('y'):
                print('Alright, pick the path then.')
                path = input('Path: ')
                if len(path) != "":
                    try:
                        if os.path.exists('data/') is not True:
                            os.mkdir('data')
                        with open('data/settings.json', 'w') as i:
                            path = self.validate_path(path)
                            if path is not None:
                                i.write(
                                    json.dumps({
                                    "path": path
                                }))
                            else:
                                try:
                                    i.close()
                                    os.remove('data/settings.json')
                                except Exception as e: print(e)
                                finally: exit()
                        with open('data/settings.json', 'r') as i:
                            try:
                                object = json.loads(i.read())
                            except Exception as e:
                                if isinstance(e, FileNotFoundError):
                                    print('The settings file is now missing. Please start the script again and setup the file again.')
                                    return False
                                else:
                                    print('An unknown error occured. I will try my best to fix it.')
                                    try:
                                        i.close()
                                        os.remove('data/settings.json')
                                        os.rmdir('data')
                                    except FileNotFoundError:
                                        print('The file is missing. Please restart the app to recreate it.')
                                        return False
                                    else:
                                        print('Alright. Now please restart the script.')
                            else:
                                if 'path' in object is False:
                                    print('The path setting is missing from the file. Please enter it again below.')
                                    path = input('Enter: ')
                                    if self.validate_path(path):
                                        print('Alright. Let me get the settings file working again. Wait.')
                                        object['path'] = path
                                        try:
                                            with open('data/settings.json', 'a') as i:
                                                i.write(json.dumps({"path":path}))
                                        except Exception as e:
                                            message = 'Something is wrong, Please copy the error below and email it to me at mail@myxi.tk'
                                            print(message+'\n'+"="*len(message))
                                        else:
                                            print('Alright, now you can continue.')
                                            return True
                                    else:
                                        return False
                    except Exception as e: 
                        print('Sorry, something went wrong while trying to create the settings file. If you want to see the error, enter "yes". Contact me here: mail@myxi.tk')
                        if input('Enter: ').lower() == 'yes': 
                            print(e)
                            return None
                        else: exit()
                    else:
                        if not self.environ_check():
                            print("We tried to create the settings file and it didn't return any errors still the environment variable is missing. Contact me here: mail@myxi.tk")
                            return None
                        else: 
                            print("Alright. Congrats now you can continue.")
                            return True
                else: 
                    print("Can't find that path.")
                    return None
            else: print('Bye!')