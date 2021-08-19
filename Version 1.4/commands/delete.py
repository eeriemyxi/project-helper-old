import json
from extras.color_format import Colors as c
def command(name):
    with open('data/projects.json', 'r') as i:
        i = json.loads(i.read())
        if not name in i:
            c.p_error("Project doesn't exist.")
            return
        else:
            del i[name]
            write = open('data/projects.json', 'w')
            write.write(json.dumps(i))
            write.close()
            c.cprint('green', 'Done.')