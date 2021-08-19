import argparse
import os
import json
import sys
import shutil
parser = argparse.ArgumentParser()
parser.add_argument("--path",metavar='"PATH"', help="Specify the path for main file of my project.")
args = parser.parse_args()
if args.path:
    if os.path.exists(args.path) and str(args.path).endswith('main.py'):
        if os.path.exists('startup.json') is False:
            with open('startup.json', 'w') as i:
                i.write(json.dumps({'path': args.path}))
                print('Path set.')
        else:
            try:
                with open('startup.json', 'r') as i:
                    try: object = json.loads(i.read())
                    except Exception: print('Corrupted startup file. Please delete "startup.json" and retry.') ; exit()
                    else: 
                        if 'path' in object:
                            object['path'] = args.path
                            open('startup.json', 'w').write(json.dumps(object))
                            print('Path set.')
                        else:
                            print('Corrupted startup file. Please delete "startup.json" and retry.') ; exit()
            except Exception as e:
                print('Something is wrong. Please mail me at mail@myxi.tk with the error below.')
                print(e)
    else:
        print('The given path doesn\'t exist or doesn\'t end with "main.py"')
else:
    try:
        with open('startup.json', 'r') as i:
            try: object = json.loads(i.read())
            except Exception: print('Corrupted startup file. Please delete "startup.json" and retry.') ; exit()
            else: 
                if 'path' in object:
                    if os.path.exists(object['path']):
                        path = object['path']
                        os.chdir(f'{os.path.split(path)[0]}')
                        os.system(f'py "{path}"')
                    else:
                        print('Path provided in startup file, doesn\'t exist. Please delete it and retry.')
                else:
                    print('Corrupted startup file. Please delete "startup.json" and retry.') ; exit()
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print('Please provide path of the main file of my project by executing this file with argument "--path"')
        else:
            print('Something is wrong. Please mail me at mail@myxi.tk with the error below.')
            print(e)