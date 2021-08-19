import os
import json
def command(settings, Colors):
    try:
        print('Which path do you want to change it to? Enter the path below. You can enter "exit" to cancel this operation.')
        inp = input('Enter path: ')
        if inp != '':
            if inp.lower() == 'exit': return
            if os.path.exists(inp):
                settings['path'] = inp
                with open('data/settings.json', 'w') as i:
                    i.write(json.dumps(settings))
                if json.loads(open('data/settings.json', 'r').read())['path'] == inp:
                    print('Alright, path has been changed.')
            else:
                print("That path doesn't exist.")
        else:
            print('Empty input!')
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            Colors.p_error("That path doesn't exist.")
        else:
            print('An unknown error occured. Please copy the error log below and send it at mail@myxi.tk'); print(e)