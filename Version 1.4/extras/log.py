import os
import json
def start(logging):
    log = logging.info
    logw = logging.warning
    loge = logging.error
    log('Logging started.')
    if os.path.exists('data'):
        log('Found data folder')
        log('Verifying files inside it.')
        if os.path.exists('data/settings.json'):
            log('Found settings file.')
            log('Now verifying it.')
            with open("data/settings.json", 'r') as sets:
                data = json.loads(sets.read())
                if 'path' in data:
                    log('Found path')
                    log('Now verifying path.')
                    try: path = data['path']
                    except Exception as e:
                        print(e)
                        loge('Settings file is not valid json.')
                        print('Settings file is corrupted. Please delete it and restart the script.')
                        exit()
                    if os.path.exists(path):
                        log('Path exists.')
                        log('Settings file is working.')
                        log(f'Path: {path}')
                    else:
                        logw("Path isn't valid.")
                        print('Settings file is corrupted. Please delete it and restart the script.')
                        exit()
                else:
                    loge('Path is missing from the settings file.')
                    print('Settings file is corrupted. Please delete it and restart the script.')
                    exit()
        else:
            loge('Settings file is missing.')
            print('Settings file is missing. Please restart the script.')
            exit()
        if os.path.exists('data/projects.json'):
            log('Projects file found')
            log('Now checking it.')
            with open("data/projects.json", 'r') as sets:
                try: file = json.loads(sets.read())
                except Exception:
                    loge('Projects file is not valid json.')
                    print('Project file is corrupted. Please delete it and restart the script.')
                    exit()
                if len(file.keys()) > 0:
                    for i in file.copy():
                        if 'path' in file[i] and os.path.exists(file[i]['path']):
                            log(f'[ {i} ] : path exists. Checking next project if any.')
                        else:
                            logw(f'Project "{i}" Doesn\'t contain path or it doesn\'t exist..')
                            while True:
                                log('Asking user to either delete it or enter a path for it.')
                                print(f'Project "{i}" contains path that doesn\'t exist. Either enter "delete" to delete it or enter a path below. I will create a folder for the project automatically.')
                                answer = input('Enter: ')
                                log(f'User entered "{answer}"')
                                if answer == 'delete':
                                    del file[i]
                                    try:
                                        with open('data/projects.json', 'w') as delete:
                                            delete.write(json.dumps(file, indent=4))
                                            log(f'{i} has been removed from projects.json')
                                            log('Checking other keys if availaible.')
                                            print('Alright. Removed it.')
                                            delete.close()
                                            break
                                    except Exception as e:
                                        logw('Failed to delete it.')
                                        loge(f'Error:\n{e}')
                                        print('Failed to remove it.')
                                        break
                                elif answer != 'delete':
                                    if os.path.exists(answer) and os.path.isdir(answer) and os.path.exists(answer+'/'+i) is False:
                                        log('Entered path exists.')
                                        log(f'Changing the path for {i}')
                                        os.mkdir(answer+'/'+i) ; file[i]['path'] = answer+'/'+i
                                        log(f'Changed path. Now saving it.')
                                        with open('data/projects.json', 'w') as save:
                                            save.write(json.dumps(file, intent=4))
                                            log('Saved.')
                                            print('Done.')
                                        log('Checking other keys.')
                                        break
                                    else:
                                        logw(f'Path doesn\'nt exist or it\'s not a directory or a folder named "{i}" already exists. Asking user again.')
                                        print(f'Path doesn\'t exist or it\'s not a directory or a folder named "{i}" already exists.')
                    log('Project file is working fine.')
                else:
                    logw('No projects found. It could be because the user hasn\'t created any project yet.')
        else:
            logw('Projects file is missing. It could be because the user hasn\'t created any project yet.')
    else:
        try: logging.critical('Data folder not found.')
        except Exception: loge('Data folder not found.')
        print('Data folder is missing. Please restart the script.')
        exit()
    log('Startup complete')