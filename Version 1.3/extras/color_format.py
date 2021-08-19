from colorama import Style, Fore
class Colors:
    @classmethod
    def cprint(cls,color, str):
        exec(f"print(Fore.{color.upper()}+'''{str}'''+Style.RESET_ALL)")
    @classmethod
    def p_error(cls,str):
        exec(f"print(Fore.RED+'''{str}'''+Style.RESET_ALL)")