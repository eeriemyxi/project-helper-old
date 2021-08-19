import json
class save_project:
    @classmethod
    def save(cls, i:bool, settings, folder, answer=None):
        if i:
            if os.path.exists('data/projects.json') is False:
                with open('data/projects.json', 'w') as i:
                    path = f"{settings['path']}/{folder}"
                    i.write(json.dumps(
                        {
                            folder: {
                                'path': path,
                                'files': [" ".join(answer.split()[1:])]
                            }
                        }, indent=4
                    ))
            else:
                with open('data/projects.json', 'r') as i:
                    path = f"{settings['path']}/{folder}"
                    text = json.loads(open('data/projects.json', 'r').read())
                    text[folder] = {
                            'path': path,
                            'files': [" ".join(answer.split()[1:])]
                        }
                    write = open('data/projects.json', 'w')
                    write.write(json.dumps(text, indent=4)) ; write.close()
        else:
            if os.path.exists('data/projects.json') is False:
                with open('data/projects.json', 'w') as i:
                    path = f"{settings['path']}/{folder}"
                    i.write(json.dumps(
                        {
                            folder: {
                                'path': path
                            }
                        },indent=4
                    ))
            else:
                with open('data/projects.json', 'r') as i:
                    path = f"{settings['path']}/{folder}"
                    text = json.loads(open('data/projects.json', 'r').read())
                    text[folder] = {
                            'path': path
                        }
                    write = open('data/projects.json', 'w')
                    write.write(json.dumps(text, indent=4)) ; write.close()


from color_format import Colors
import os
def command(settings):
    try:
        print('Welcome to the project creating wizard. To create a folder, Type the name of the project below. You can always type "exit" to cancel the operation.')
        folder = input('Folder name: ')
        if folder.lower() == 'exit': return
        os.mkdir(os.path.normpath(settings['path']) + '/' + folder)
        print(
            'Alright, we created the folder. Next is the main file where you would want to start coding.\nIf you want us to create it for you then type "true <filename>" or "false" to cancel. ')
        answer = input('Answer: ')
        if answer.lower().startswith('true'):
            if len(answer.split()) >= 2:
                open(
                    os.path.normpath(settings['path']) + '/' + folder + '/' + " ".join(answer.split()[1:]), 'w'
                ).close()
                print('Saving the project...')
                save_project.save(True, settings, folder, answer)
                print('Alright done!')
                return
            else:
                print("We've accepted your input as a negetive answer. That's all we can do right now. Big changes are coming in version 1.2!")
                return
        else:
            print('Saving project...')
            save_project.save(False, settings, folder)
            print("Alright. That's all we can do right now. Big changes are coming in version 1.2!")
            return
    except Exception as e:
        if isinstance(e, FileExistsError):
            Colors().p_error('That directory or file already exists.')
            return
        else:
            Colors().p_error('An unknown error occured. Please contact me at mail@myxi.tk with the error log below.') ; print(e)
            return