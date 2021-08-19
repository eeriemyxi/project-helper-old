from commands.help_command_list import Lists
def command(Colors):
    print("""Alternative words that does the same thing has been seperated by "|""")
    json = Lists.main_help()
    for name in json:
        alts = ''
        if 'alts' in json[name]:
            alts = ' | '+" | ".join(json[name]['alts'])
        print(f"""{name}{alts}
        - {json[name]['desc']}""")